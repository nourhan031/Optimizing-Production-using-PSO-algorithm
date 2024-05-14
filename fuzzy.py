import numpy as np
import matplotlib.pyplot as plt

def triangular_membership(x, min_val, peak_val, max_val):
    y = np.zeros_like(x)
    mask_left = np.logical_and(x >= min_val, x <= peak_val)
    mask_right = np.logical_and(x >= peak_val, x <= max_val)
    y[mask_left] = (x[mask_left] - min_val) / (peak_val - min_val)
    y[mask_right] = (max_val - x[mask_right]) / (max_val - peak_val)
    return np.clip(y, 0, 1)

# Define the range of values for the cost
x_P1 = np.linspace(170, 195, 225)
x_P2 = np.linspace(200, 225, 250)

# Parameters for the triangular membership functions for C1
P1_min = 180  # a
P1_peak = 195  # b
P1_max = 210  # c

# Parameters for the triangular membership functions for C2
P2_min = 200  # a
P2_peak = 225  # b
P2_max = 250  # c

# Calculate membership degrees for C1 and C2
membership_P1 = triangular_membership(x_P1, P1_min, P1_peak, P1_max)
membership_P2 = triangular_membership(x_P2, P2_min, P2_peak, P2_max)

# Plot the triangular membership functions
plt.figure(figsize=(10, 6))
plt.plot(x_P1, membership_P1, label='P1 Membership Function')
plt.plot(x_P2, membership_P2, label='P2 Membership Function')
plt.xlabel('Price ($)')
plt.ylabel('Membership Degree')
plt.title('Triangular Membership Functions for price Parameters')
plt.legend()
plt.grid(True)
plt.show()

# Alpha cut and defuzzification
alpha_cut = 0.5
# Generate random numbers for r1 and r2
r1_P1 = np.random.uniform(P1_min, P1_max)
r1_P2 = np.random.uniform(P2_min, P2_max)
r2 = np.random.uniform(0, 1)

# Defuzzification for P1
try:
    if r2 >= alpha_cut:
        difuzzification_value_P1 = r1_P1
        result_P1 = True
    else:
        raise ValueError("Defuzzification  value for P1 is not valid")
except ValueError as ve:
    print(ve)
    result_P1 = False
    difuzzification_value_P1 = None

# Defuzzification for P2
try:
    if r2 >= alpha_cut:
        difuzzification_value_P2 = r1_P2
        result_P2 = True
        
    else:
        raise ValueError("Defuzzification  value for P2 is not valid")
except ValueError as ve:
    print(ve)
    result_P2 = False
    difuzzification_value_P2 = None

def calculate_profit(s1, s2, p1, p2, F, difuzzification_crisp_P1, difuzzification_crisp_P2):
    if difuzzification_crisp_P1 is None or difuzzification_crisp_P2 is None:
        return None

    P = s1 * (p1 - difuzzification_value_P1) + s2 * (p2 - difuzzification_value_P2) - F
    return P

# Perform Monte Carlo simulation
num_simulations = 5
defuzzified_price1 = []
defuzzified_price2 = []
alphacuts=[]

for _ in range(num_simulations):
  while True:
    r1_P1 = np.random.uniform(P1_min, P1_max)
    r1_P2 = np.random.uniform(P2_min, P2_max)
    r2 = np.random.uniform(0, 1)
    alpha_cut= np.random.uniform(0,1)
    
    
    
    if alpha_cut <= r2:
        defuzzified_price1.append(r1_P1)
        defuzzified_price2.append(r1_P2)
        alphacuts.append(alpha_cut)
        break



print("Result for P1:", result_P1)
print("Defuzzification Crisp Value for P1:", difuzzification_value_P1)
print("Result for P2:", result_P2)
print("Defuzzification Crisp Value for 2:", difuzzification_value_P2)
# Calculate average defuzzified price values
average_defuzzified_price1 = np.mean(defuzzified_price1)
average_defuzzified_price2 = np.mean(defuzzified_price2)
print("MONTO CARLOS SIMULATION VALUES")

print("list of defuzzified value for price 1",defuzzified_price1)

print("-----------------------------------------")

print("Average Defuzzified Price 1 (p1):", average_defuzzified_price1)

print("-----------------------------------------")

print("list of defuzzified value for price 2",defuzzified_price2)

print("-----------------------------------------")

print("Average Defuzzified Price 2 (p2):", average_defuzzified_price2)

print("-----------------------------------------")



print("-----------------------------------------")

print("print list of the alpha cut ",alphacuts)



s1 = 1000  # number of units of the 19-inch set produced per year
s2 = 1000  # number of units of the 21-inch set produced per year
p1 = 339  # sales price per unit of the 19-inch set ($)
p2 = 339  # sales price per unit of the 21-inch set ($)
F = 400000  # additional fixed costs per year
# Calculate profit with average defuzzified price values
profit = calculate_profit(s1, s2, p1, p2, F, average_defuzzified_price1, average_defuzzified_price2)

if profit is not None:
    print("Profit (P):", profit)



   

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
x_C1 = np.linspace(170, 195, 225)
x_C2 = np.linspace(200, 225, 250)

# Parameters for the triangular membership functions for C1
C1_min = 180  # a
C1_peak = 195  # b
C1_max = 210  # c

# Parameters for the triangular membership functions for C2
C2_min = 200  # a
C2_peak = 225  # b
C2_max = 250  # c

# Calculate membership degrees for C1 and C2
membership_C1 = triangular_membership(x_C1, C1_min, C1_peak, C1_max)
membership_C2 = triangular_membership(x_C2, C2_min, C2_peak, C2_max)

# Plot the triangular membership functions
plt.figure(figsize=(10, 6))
plt.plot(x_C1, membership_C1, label='C1 Membership Function')
plt.plot(x_C2, membership_C2, label='C2 Membership Function')
plt.xlabel('Cost ($)')
plt.ylabel('Membership Degree')
plt.title('Triangular Membership Functions for price Parameters')
plt.legend()
plt.grid(True)
plt.show()

# Alpha cut and defuzzification
alpha_cut = 0.5
# Generate random numbers for r1 and r2
r1_C1 = np.random.uniform(C1_min, C1_max)
r1_C2 = np.random.uniform(C2_min, C2_max)
r2 = np.random.uniform(0, 1)

# Defuzzification for C1
try:
    if r2 >= alpha_cut:
        difuzzification_value_C1 = r1_C1
        result_C1 = True
    else:
        raise ValueError("Defuzzification  value for C1 is not valid")
except ValueError as ve:
    print(ve)
    result_C1 = False
    difuzzification_value_C1 = None

# Defuzzification for C2
try:
    if r2 >= alpha_cut:
        difuzzification_value_C2 = r1_C2
        result_C2 = True
        
    else:
        raise ValueError("Defuzzification  value for P2 is not valid")
except ValueError as ve:
    print(ve)
    result_C2 = False
    difuzzification_value_C2 = None

def calculate_profit(s1, s2, p1, p2, F, difuzzification_value_C1, difuzzification_value_C2):
    if difuzzification_value_C1 is None or difuzzification_value_C2 is None:
        return None

    P = s1 * (p1 - difuzzification_value_C1) + s2 * (p2 - difuzzification_value_C2) - F
    return P

# Perform Monte Carlo simulation
num_simulations = 5
defuzzified_COST1 = []
defuzzified_COST2 = []
alphacuts=[]

for _ in range(num_simulations):
  while True:
    r1_C1 = np.random.uniform(C1_min, C1_max)
    r1_C2 = np.random.uniform(C2_min, C2_max)
    r2 = np.random.uniform(0, 1)
    alpha_cut= np.random.uniform(0,1)
    
    
    
    if alpha_cut <= r2:
        defuzzified_COST1.append(r1_C1)
        defuzzified_COST2.append(r1_C2)
        alphacuts.append(alpha_cut)
        break



print("Result for C1:", result_C1)
print("Defuzzification  Value for C1:", difuzzification_value_C1)
print("Result for C2:", result_C2)
print("Defuzzification  Value for C2:", difuzzification_value_C2)
# Calculate average defuzzified price values
average_defuzzified_COST1 = np.mean(defuzzified_COST1)
average_defuzzified_COST2 = np.mean(defuzzified_COST2)
print("MONTO CARLOS SIMULATION VALUES")

print("list of defuzzified value for COST 1",defuzzified_COST1)

print("-----------------------------------------")

print("Average Defuzzified COST 1 (C1):", average_defuzzified_COST1)

print("-----------------------------------------")

print("list of defuzzified value for CSOT 2",defuzzified_COST2)

print("-----------------------------------------")

print("Average Defuzzified COST 2 (p2):", average_defuzzified_COST2)

print("-----------------------------------------")



print("-----------------------------------------")

print("print list of the alpha cut ",alphacuts)



s1 = 1000  # number of units of the 19-inch set produced per year
s2 = 1000  # number of units of the 21-inch set produced per year
p1 = 339  # sales price per unit of the 19-inch set ($)
p2 = 339  # sales price per unit of the 21-inch set ($)
F = 400000  # additional fixed costs per year
# Calculate profit with average defuzzified price values
profit = calculate_profit(s1, s2, p1, p2, F, average_defuzzified_COST1, average_defuzzified_COST2)

if profit is not None:
    print("Profit (P):", profit)



   

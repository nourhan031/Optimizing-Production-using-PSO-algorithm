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
plt.title('Triangular Membership Functions for Cost Parameters')
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
        difuzzification_crisp_C1 = r1_C1
        result_C1 = True
    else:
        raise ValueError("Defuzzification crisp value for C1 is not valid")
except ValueError as ve:
    print(ve)
    result_C1 = False
    difuzzification_crisp_C1 = None

# Defuzzification for C2
try:
    if r2 >= alpha_cut:
        difuzzification_crisp_C2 = r1_C2
        result_C2 = True
    else:
        raise ValueError("Defuzzification crisp value for C2 is not valid")
except ValueError as ve:
    print(ve)
    result_C2 = False
    difuzzification_crisp_C2 = None

print("Result for C1:", result_C1)
print("Defuzzification Crisp Value for C1:", difuzzification_crisp_C1)

print("Result for C2:", result_C2)
print("Defuzzification Crisp Value for C2:", difuzzification_crisp_C2)

s1 = 1000  # number of units of the 19-inch set produced per year
s2 = 1000  # number of units of the 21-inch set produced per year
p1 = 339  # sales price per unit of the 19-inch set ($)
p2 = 339  # sales price per unit of the 21-inch set ($)
F = 400000  # additional fixed costs per year

if (result_C1 == True and result_C2 == True):
    P = s1 * (p1 - difuzzification_crisp_C1) + s2 * (p2 - difuzzification_crisp_C2) - F
    print("Profit (P):", P)

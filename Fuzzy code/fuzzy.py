import math
import random
import numpy as np
import matplotlib.pyplot as plt

def triangular_membership(x, min_val, peak_val, max_val):
    if isinstance(x, (float, int)):
        if x >= min_val and x <= peak_val:
            return (x - min_val) / (peak_val - min_val)
        elif x > peak_val and x <= max_val:
            return (max_val - x) / (max_val - peak_val)
        else:
            return 0
    else:
        y = np.zeros_like(x)
        mask_left = np.logical_and(x >= min_val, x <= peak_val)
        mask_right = np.logical_and(x > peak_val, x <= max_val)
        y[mask_left] = (x[mask_left] - min_val) / (peak_val - min_val)
        y[mask_right] = (max_val - x[mask_right]) / (max_val - peak_val)
        return np.clip(y, 0, 1)

# Define the range of values for the cost
x_C1 = np.linspace(180, 210, 10)
x_C2 = np.linspace(200, 250, 10)

# Parameters for the triangular membership functions for C1 and C2
C1_min = 180
C1_peak = 195
C1_max = 210
C2_min = 200
C2_peak = 225
C2_max = 250

# Calculate membership degrees for C1 and C2
membership_C1 = triangular_membership(x_C1, C1_min, C1_peak, C1_max)
membership_C2 = triangular_membership(x_C2, C2_min, C2_peak, C2_max)

# Plot the triangular membership functions
plt.figure(figsize=(10, 6))
plt.plot(x_C1, membership_C1, label='C1 Membership Function')
plt.plot(x_C2, membership_C2, label='C2 Membership Function')
plt.xlabel('Cost ($)')
plt.ylabel('Membership Degree')
plt.title('Triangular Membership Functions for Price Parameters')
plt.legend()
plt.grid(True)
plt.show()

# Monte Carlo simulation
num_simulations = 10
defuzzified_COST1 = []
defuzzified_COST2 = []
alphacuts_c1 = []
alphacuts_c2 = []
memb_val_cost1=[]
memb_val_cost2=[]


for i in range(num_simulations):
    while True:
        # Defuzzify C1
        x_c1 = random.uniform(C1_min, C1_max)
        u_c1 = triangular_membership(x_c1, C1_min, C1_peak, C1_max)
        alpha_cut_c1 = random.uniform(0, 1)
        if alpha_cut_c1 <= u_c1:
            defuzzified_COST1.append(x_c1)
            alphacuts_c1.append(alpha_cut_c1)
            memb_val_cost1.append(u_c1)
            break

    while True:
        # Defuzzify C2
        x_c2 = random.uniform(C2_min, C2_max)
        u_c2 = triangular_membership(x_c2, C2_min, C2_peak, C2_max)
        alpha_cut_c2 = random.uniform(0, 1)
        if alpha_cut_c2 <= u_c2:
            defuzzified_COST2.append(x_c2)
            alphacuts_c2.append(alpha_cut_c2)
            memb_val_cost2.append(u_c2)
            break

# Print defuzzified values for COST1
print("Defuzzified Values for COST1:")
for i, val in enumerate(defuzzified_COST1):
    print(f"Simulation {i+1}: ${val:.2f}")

# Print defuzzified values for COST2
print("\nDefuzzified Values for COST2:")
for i, val in enumerate(defuzzified_COST2):
    print(f"Simulation {i+1}: ${val:.2f}")



# Calculate average defuzzified price values
average_defuzzified_COST1 = np.mean(defuzzified_COST1)
average_defuzzified_COST2 = np.mean(defuzzified_COST2)

print("MONTE CARLO SIMULATION VALUES")
print(f"List of defuzzified values for COST 1: {defuzzified_COST1}")
print(f"Average Defuzzified COST 1 (C1): {average_defuzzified_COST1:.2f}")
print(f"List of defuzzified values for COST 2: {defuzzified_COST2}")
print(f"Average Defuzzified COST 2 (C2): {average_defuzzified_COST2:.2f}")
print(f"List of the alpha cut values for c1: {alphacuts_c1}")
print(f"List of the alpha cut values for c2: {alphacuts_c2}")
print(f"List of the membership  values for c1: {memb_val_cost1}")
print(f"List of the membership values for c2: {memb_val_cost2}")



print("\nRANGE OF VALUES:")
print(f"Range of C1: {x_C1}")
print(f"Range of C2: {x_C2}")


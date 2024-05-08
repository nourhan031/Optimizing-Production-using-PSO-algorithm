#fuzzification of Crisp value of cost producing tv 19 inches uncertianty paratmeter
from logging import raiseExceptions
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
x = np.linspace(170, 195, 225)

# Parameters for the triangular membership functions for C1
C1_min = 180 #a
C1_peak = 195 #b
C1_max = 210 #c

# Calculate membership degrees for C1 and C2
membership_C1 = triangular_membership(x, C1_min, C1_peak, C1_max)


# Plot the triangular membership functions
plt.figure(figsize=(10, 6))
plt.plot(x, membership_C1, label='C1 Membership Function')
#plt.plot(x, membership_C2, label='C2 Membership Function')
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
#r1_C2 = np.random.uniform(C2_min, C2_max)
r2 = np.random.uniform(0, 1)

try:
    if r2 >= alpha_cut:
        difuzzification_crisp = r1_C1
        result = True
    else:
        raise ValueError("This defuzzification crisp value is not valid")
except ValueError as ve:
    print(ve)
    result = False
    difuzzification_crisp = None

print("Result:", result)
print("Defuzzification Crisp Value:", difuzzification_crisp)

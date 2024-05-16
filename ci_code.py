

import math
import random
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
x_C1 = np.linspace(160, 210, 100)
x_C2 = np.linspace(210, 250, 100)

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








#Parameters
c1 = 2
c2 = 2
num_particles= 50
iterations = 50
radius = 1000

#Lists
position = []
velocities = []
xBest = []
bounds = [(0, 5000), (0, 8000)]
velocity_bounds = [(-10, 100), (-10, 100)]
num_iterations = 30
optimal = []
bestS1 = []
bestS2 = []
#function to generate random variable for r1, r2
def Generate_random():
    r = random.uniform(0,1)
    return r

#Function to Evaluate fitness
def Evaluate_fitness(s1, s2):
    linear_constraint = s1 + s2 - 10000
    if linear_constraint <= 0:
        penality = 0
    else:
        penality = max(0,linear_constraint)

    obj = -400000+ (difuzzification_value_C1 * s1) + (difuzzification_value_C2 * s2) - (0.01) * (s2**2) - (0.007 * s1 * s2)  - (0.01) * (s2 ** 2)
    return obj-penality

#Function to calculate velocity
def Calculate_velocity(x,oldVelocity,xBest,lBest):
    r1 = Generate_random()
    r2 = Generate_random()
    newVelocity = oldVelocity + c1 * r1 * (xBest-x) + c2 * r2 * (lBest-x)
    return newVelocity

#Function to calculate distance between two particles
def Calculate_distance(s1,s2):
    distance = math.dist(s1,s2)
    return distance

#Function to calculate local best
def Calculate_lBest(particles,target,indexOfTarget):
    lBest = xBest[indexOfTarget]
    for i in range(num_particles):
        distance = Calculate_distance(target,particles[i])
        if distance <= radius:
            lBest = max(lBest,xBest[i])

    return lBest

#************************************************************************************************************************
#Generate position
# for _ in range(num_particles):
#     random_row = [random.uniform(bound[0], bound[1]) for bound in bounds]                                                                     #random.randint-->generate integers
#     particle_velocity = [random.uniform(velocity_bounds[dim][0], velocity_bounds[dim][1]) for dim in range(len(velocity_bounds))]             #random.unifrom-->generate floating point
#     velocities.append(particle_velocity)
#     position.append(random_row)
#
# #Evaluate fitness and set xBest
# for i in range(num_particles):
#     fitness = Evaluate_fitness(position[i][0],position[i][1])
#     xBest.append(fitness)
#
# bestFitness = max(xBest)

#************************************************************************************************************************
#Iterations
for n in range(num_iterations):
    #Generate position
    for _ in range(num_particles):
        random_row = [random.uniform(bound[0], bound[1]) for bound in bounds]                                                                     #random.randint-->generate integers
        particle_velocity = [random.uniform(velocity_bounds[dim][0], velocity_bounds[dim][1]) for dim in range(len(velocity_bounds))]             #random.unifrom-->generate floating point
        velocities.append(particle_velocity)
        position.append(random_row)

    #Evaluate fitness and set xBest
    for i in range(num_particles):
        fitness = Evaluate_fitness(position[i][0],position[i][1])
        xBest.append(fitness)

    bestFitness = max(xBest)
    best_index = xBest.index(max(xBest))
    s1 = position[best_index][0]
    s2 = position[best_index][1]
    for i in range(iterations):
        for j in range(num_particles):
            #Calculate new position
            position[j][0] += velocities[j][0]
            position[j][1] += velocities[j][1]

            #Check bounds
            if position[j][0] > bounds[0][1]:
                position[j][0] = bounds[0][1]
            if position[j][0] < bounds[0][0]:
                position[j][0] = bounds[0][0]

            if position[j][1] > bounds[1][1]:
                position[j][1] = bounds[1][1]
            if position[j][1] < bounds[1][0]:
                position[j][1] = bounds[1][0]

            #Calculate local best
            lBest = Calculate_lBest(position,position[j],j)

            #Calculate velocity for s1
            velocities[j][0] = Calculate_velocity(position[j][0],velocities[j][0],xBest[j],lBest)
            velocities[j][1] = Calculate_velocity(position[j][0],velocities[j][1],xBest[j],lBest)

            #Evaluate fitness and update xBest
            fitness = Evaluate_fitness(position[j][0],position[j][1])
            xBest[j] = max(xBest[j],fitness)
            if fitness > bestFitness:
                bestFitness = fitness
                s1 = position[j][0]
                s2 = position[j][1]

    optimal.append(bestFitness)
    bestS1.append(s1)
    bestS2.append(s2)
    position.clear()
    velocities.clear()
    xBest.clear()





print(optimal)
print(bestS1)
print(bestS2)
print("****************")
solution = sum(optimal)/len(optimal)
s1 = sum(bestS1)/len(bestS1)
s2 = sum(bestS2)/len(bestS2)
print("Average of average best fitness = ", solution)
print("Average of average S1 = ",s1)
print("Average of average S2 = ",s2)
print("********************")
print("The best solution = ",max(optimal))
best_index = optimal.index(max(optimal))
print("s1 for best solution = ", bestS1[best_index])
print("s2 for best solution = ", bestS2[best_index])

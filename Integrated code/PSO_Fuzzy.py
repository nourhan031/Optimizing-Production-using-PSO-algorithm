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



#print("\nRANGE OF VALUES:")
#print(f"Range of C1: {x_C1}")
#print(f"Range of C2: {x_C2}")













#Parameters
c1 = 2
c2 = 2
num_particles= 50
num_solo_iterations = 500
num_runs = 20
radius = 1000
bounds = [(0, 5000), (0, 8000)]
velocity_bounds = [(-10, 100), (-10, 100)]

#Lists
position = []
velocities = []
xBest = []
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
    obj = -400000+ ((339-average_defuzzified_COST1) * s1) + ((399-average_defuzzified_COST2) * s2) - (0.01) * (s1**2) - (0.007 * s1 * s2)  - (0.01) * (s2 ** 2)
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
#Iterations
for n in range(num_solo_iterations):
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
    for i in range(num_runs):
        for j in range(num_particles):
            #Calculate local best
            lBest = Calculate_lBest(position,position[j],j)

            #Calculate velocity for s1
            velocities[j][0] = Calculate_velocity(position[j][0],velocities[j][0],xBest[j],lBest)
            velocities[j][1] = Calculate_velocity(position[j][0],velocities[j][1],xBest[j],lBest)

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





# print(optimal)
# print(bestS1)
# print(bestS2)
print("======================================================================================")
solution = sum(optimal)/len(optimal)
s1 = sum(bestS1)/len(bestS1)
s2 = sum(bestS2)/len(bestS2)
print("Average of average best fitness = ", solution)
print("Average of average S1 = ",s1)
print("Average of average S2 = ",s2)
print("======================================================================================")
print("The best solution = ",max(optimal))
best_index = optimal.index(max(optimal))
print("s1 for best solution = ", bestS1[best_index])
print("s2 for best solution = ", bestS2[best_index])
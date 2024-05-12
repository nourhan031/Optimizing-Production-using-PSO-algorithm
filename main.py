import math
import random

# Parameters
c1 = 2
c2 = 2
num_particles= 50
iterations = 500
radius = 1000

# Lists
position = []
velocities = []
xBest = []
bounds = [(0, 5000), (0, 8000)]
velocity_bounds = [(-10, 100), (-0.1, 1)]
num_iterations = 20
optimal = []
bestS1 = []
bestS2 = []

# Function to generate r1 and r2
def Generate_random():
    r = random.uniform(0, 1)
    return r

#vFunction to evaluate fitness
def Evaluate_fitness(s1, s2):
    linear_constraint = s1 + s2 - 10000

    if linear_constraint <= 0:
        penalty = 0
    else:
        penalty = max(0, linear_constraint)

    obj = -400000 + (144 * s1) + (174 * s2) - (0.01) * (s2**2) - (0.007 * s1 * s2)  - (0.01) * (s2 ** 2)
    return obj - penalty

# Function to calculate velocity
def Calculate_velocity(x, oldVelocity, xBest, lBest):
    r1 = Generate_random()
    r2 = Generate_random()
    newVelocity = oldVelocity + c1 * r1 * (xBest-x) + c2 * r2 * (lBest-x)
    return newVelocity

# Function to calculate distance between two particles
def Calculate_distance(s1, s2):
    distance = math.dist(s1, s2)
    return distance

# Function to calculate local best
def Calculate_lBest(particles, target, indexOfTarget):
    lBest = xBest[indexOfTarget]

    for i in range(num_particles):
        distance = Calculate_distance(target,particles[i])

        if distance <= radius:
            lBest = max(lBest,xBest[i])

    return lBest

# ************************************************************************************************************************

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

# ************************************************************************************************************************

# Iterations
for n in range(num_iterations):
    s1 = 0
    s2 = 0
    # Generate position
    for _ in range(num_particles):
        random_row = [random.uniform(bound[0], bound[1]) for bound in bounds]                                                                     # random.randint-->generate integers
        particle_velocity = [random.uniform(velocity_bounds[dim][0], velocity_bounds[dim][1]) for dim in range(len(velocity_bounds))]             # random.uniform-->generate floating point
        velocities.append(particle_velocity)
        position.append(random_row)

    # Evaluate fitness and set xBest
    for i in range(num_particles):
        fitness = Evaluate_fitness(position[i][0],position[i][1])
        xBest.append(fitness)

    bestFitness = max(xBest)

    for i in range(iterations):
        for j in range(num_particles):
            # Calculate new position
            position[j][0] += velocities[j][0]
            position[j][1] += velocities[j][1]

            # Check bounds
            if position[j][0] > bounds[0][1]:
                position[j][0] = bounds[0][1]
            if position[j][0] < bounds[0][0]:
                position[j][0] = bounds[0][0]

            if position[j][1] > bounds[1][1]:
                position[j][1] = bounds[1][1]
            if position[j][1] < bounds[1][0]:
                position[j][1] = bounds[1][0]

            # Calculate local best
            lBest = Calculate_lBest(position,position[j],j)

            # Calculate velocity for s1
            velocities[j][0] = Calculate_velocity(position[j][0],velocities[j][0],xBest[j],lBest)
            velocities[j][1] = Calculate_velocity(position[j][0],velocities[j][1],xBest[j],lBest)

            # Evaluate fitness and update xBest
            fitness = Evaluate_fitness(position[j][0],position[j][1])
            xBest[j] = max(xBest[j],fitness)

            if fitness > bestFitness:
                bestFitness = fitness
                s1 = position[j][0]
                s2 = position[j][1]

    optimal.append(bestFitness)
    bestS1.append(s1)
    bestS2.append(s2)





print(optimal)
print(bestS1)
print(bestS2)
print("****************")

solution = sum(optimal) / len(optimal)
s1 = sum(bestS1) / len(bestS1)
s2 = sum(bestS2) / len(bestS2)

print("Average of average = ", solution)
print("S1 = ", s1)
print("S2 = ", s2)




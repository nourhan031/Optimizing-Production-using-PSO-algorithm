#c1 + c2 = 4
#xBest of size i --> to get the best global for each particle
#radis --> for get global best for each group
#STEP1: Initialization:
#1)Intialize paramteres
#2)Intialize Population:
#i particles
#initialize position(i*j list for position)- j dimension according to our problem
#initialize velocity for each dimension (i*j list for velocity)
#STEP 2: Evaluate fitness:
#if the new is better than the gBest, set gBest = new
#STEP 3: for each particle calculate velocity and position
#calculate position (for each dimension): xi(t+1) = xi(t) + vi(t)
#calculate local best (for each particle): calculate distance between i and each particle in swarm and get the best of them
#calculate velocity (for each dimension): vi(t+1) = v(t) + c1 * r1(0,1) * (xBest - xi(t)) + c2 * r2(0,1) * (lBest - xi(t))
#STEP 4: evaluate fitness and update xBest
#STEP 5: update t = t+1
import random

#NOTES: if it exceed the constraints --> objective - penality
#if it exceed the bounds --> make it = bounds

#Parameters
c1 = 2
c2 = 2
#n --> number of particles
#radis --> according to the problem

#Lists
position = []
velocity = []
xBest = []

#function to generate random variable for r1, r2
def generate_random():
    r = random.Random()
    return r




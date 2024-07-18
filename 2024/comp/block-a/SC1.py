### Squared circle (25 points) ###
import math
import random
def solve(rayon, L, nbrPoints):
    amountOfPointsInTheCircle = 0
    right, left = L/2, -L/2
    for x in range(nbrPoints):
        spot = (random.uniform(left, right), random.uniform(left, right))
        if math.sqrt(spot[0]*spot[0]+spot[1]*spot[1]) < rayon:
            amountOfPointsInTheCircle = amountOfPointsInTheCircle+1
    return amountOfPointsInTheCircle/nbrPoints
        
print(abs(solve(3, 4, 100000)))
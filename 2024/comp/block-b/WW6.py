### Colossus of Rhodes (40 points) ###
import math

def solve(distance, distance_uncertainty, angle, angle_uncertainty):
    minimal_distance = distance * (1 - distance_uncertainty)
    minimal_angle = angle - angle_uncertainty
    minimal_hypotenuse = minimal_distance/math.cos(math.radians(minimal_angle))
    minimal_height = math.sqrt((minimal_hypotenuse**2) - (minimal_distance**2))

    maximal_distance = distance * (1 + distance_uncertainty)
    maximal_angle = angle + angle_uncertainty
    maximal_hypotenuse = maximal_distance/math.cos(math.radians(maximal_angle))
    maximal_height = math.sqrt((maximal_hypotenuse**2) - (maximal_distance**2))

    return [round(minimal_height, 3), round(maximal_height, 3)]


print(solve(80, 0.01, 15, 2))

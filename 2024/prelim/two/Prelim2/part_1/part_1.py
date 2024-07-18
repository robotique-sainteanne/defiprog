# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_1.py
This is the template file for the part 1 of the Prelim 2.
Ceci est le fichier template pour la partie 1 du Prelim 2.
"""
import math
import matplotlib
import numpy
def part_1(groupments_and_rests: [(int, int)]) -> str:
    """
    Count the minimal number of tools using the rest of groupments.

    Parameters:
        groupments_and_rests [(int, int)]: An array of the tuple of the groupments sizes and the rest for each groupment.

    Returns:
        str: The minimum number of tools using for digits
    """
    minimum_number_of_tools = -1
    ### You code goes here ###
    ### Votre code va ici ###
    
    def find_m(group):
        g, r = group
        product = 1
        for x in groupments_and_rests:
            if x != group:
                product *= x[0]
        m = 1
        while (m * product) % g != 1:
            m += 1
        return m

    product_g = 1
    for x in groupments_and_rests:
        product_g *= x[0]
    
    x = sum([(product_g // group[0] * group[1] * find_m(group)) for group in groupments_and_rests])
    
    minimum_number_of_tools = x % product_g
    minimum_number_of_tools = str(minimum_number_of_tools).zfill(4)
    return minimum_number_of_tools


# Uncomment the following print to test your function without pytest
# Décommenter la suite pour des tests sans pytest

print(part_1([(3,2), (5,3), (7,2)])) # Expected: '0023'
print(part_1([(21, 5), (2, 1), (19, 7), (5, 2)])) # Expected: '3617'
print(part_1([(7,4), (11,2), (23,14), (3,2)])) # Expected: '5051'
print(part_1([(3,1), (7, 5)])) # Expected: '0019'
print(part_1([(7,4), (11,1), (23,15), (3,1)])) # Expected: '3994'

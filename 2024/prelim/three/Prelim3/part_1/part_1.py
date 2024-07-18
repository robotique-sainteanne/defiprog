# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_1.py
This is the template file for the part 1 of the Prelim 3.
Ceci est le fichier template pour la partie 1 du Prelim 3.
"""

def part_1(number: int) -> [str]:
    """
    Expand and reduce a number with alternating sign.

    Parameters:
        number (int): The number to expand

    Returns:
        [str]: An array containing all the expansions of the number
    """
    expansions = []
    ### You code goes here ###
    ### Votre code va ici ###
    for x in range(number):
        y = x
        currentString = ""
        while y >= 1:
            currentString = currentString+f" {number-x}-{number-x}"
            y = y-1
        currentString = currentString+f" {number-x}"
        
        expansions.append(str(currentString))
    
    currentString = ""
    for w in range(number*2+1):
        currentString = currentString+f" {0}"
    expansions.append(str(currentString))
    return expansions

# Uncomment the following print to test your function without pytest
# Décommenter la suite pour des tests sans pytest


print(part_1(number=300))
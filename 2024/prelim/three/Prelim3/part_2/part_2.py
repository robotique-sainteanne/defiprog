# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_3.py
This is the template file for the part 3 of the Prelim 3.
Ceci est le fichier template pour la partie 3 du Prelim 3.
"""
import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def part_2(nbr_steps: int, row: str) -> [str]: # type: ignore
    """
    Find the drop and simulate propagation for n steps

    Parameters:
        nbr_steps (int): The number of steps for the simulation.
        row (str): The state of th row at the drop.

    Returns:
        [str]: the sequence of the expansion after a drop for n steps.
    """
    sequence = []
    ### You code goes here ###
    ### Votre code va ici ###
    currentString = ""
    putDash = False
    splitRow = row.split()
    currentSequence = splitRow
    for i in range(len(splitRow)):
        if splitRow[i] != "0":
            relativeMiddle = i
            maxValue = int(splitRow[i])
            break

    for i in range(nbr_steps):
        if i == 0 and splitRow[0] != "0":
            putDash = True
        currentString = ""
        currentSequence = row.split()
        currentSequence[relativeMiddle] = str(maxValue-i-1)
        for x in range(i+1):
            if relativeMiddle+x+1 < len(currentSequence): 
                currentSequence[relativeMiddle+x+1] = str(maxValue-i-1)
            if relativeMiddle-x > 0: 
                currentSequence[relativeMiddle-(x+1)] = str(maxValue-i-1)        
        
        for x in currentSequence:
            if x != "0" and putDash:
                currentString = currentString+f"-{x}"
                putDash = False
            elif x != "0" and not putDash:
                currentString = currentString+f" {x}"
                putDash = True
            else:
                currentString = currentString+f" {x}"
        
        sequence.append(currentString)
        if currentSequence[0] != "0" and currentString[0] == " ":
            putDash = True
        else:
            putDash = False

    return sequence

# Uncomment the following print to test your function without pytest (more tests using pytest)
# Décommenter la suite pour des tests sans pytest (il y a plus de tests avec pytest)

print(part_2(3, ' 0 0 0 0 0 0 0 9 0 0'))
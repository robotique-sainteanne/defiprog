# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_2.py
This is the template file for the part 2 of the Prelim 3.
Ceci est le fichier template pour la partie 2 du Prelim 3.
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def part_3(nbr_steps: int, grid: [str]) -> [[str]]: # type: ignore
    """
    This simulates a drop of water on a calm surface.

    Parameters:
        nbr_steps (int): The number of steps of the simulation you need to run
        grid ([str]): The grid containing the drop point and strength

    Returns:
        [[str]]: The grids with the wave for the number of steps specified
    """
    results = []
    ### You code goes here ###
    ### Votre code va ici ###
    splitStrList = []
    putDash = False
    otherRows = []
    def transformToString(putDash: bool, currentSequence: [str]) -> str: # type: ignore
        currentString = ""
        for x in currentSequence:
            if x != "0" and putDash:
                currentString = currentString+f"-{x}"
                putDash = False
            elif x != "0" and not putDash:
                currentString = currentString+f" {x}"
                putDash = True
            else:
                currentString = currentString+f" {x}"
        return currentString
    def createSequence(rangeInt: int, middleColumn: int, currentSequence: [str], maxValue: int): # type: ignore
        currentSequence[middleColumn] = str(maxValue-i-1)
        for x in range(rangeInt):
            if middleColumn+x+1 < len(currentSequence): 
                currentSequence[middleColumn+x+1] = str(maxValue-i-1)
            if middleColumn-x > 0: 
                currentSequence[middleColumn-(x+1)] = str(maxValue-i-1)
        return currentSequence
    #splitting the main grid
    for i in range(len(grid)):
        splitStrList.append(grid[i].split())
    #finding the center row, center column and the number in that position
    for i in range(len(splitStrList)):
        for x in range(len(splitStrList[i])):
            if splitStrList[i][x] != "0":
                middleRow = int(i)
                middleColumn = int(x)
                maxValue = int(splitStrList[i][x])
                break
    #creating each grid for the output
    for i in range(nbr_steps):
        #resetting the variables
        otherRows = []
        currentSequence = splitStrList[0]
        currentGrid = []
        #making the dashes get properly placed
        if i == 0 and splitStrList[middleRow][0] != "0":
            putDash = True           
        #creating the rows above and beneath the main one(center one)
        for w in range(nbr_steps-1+i):
            #reseting the sequence
            currentSequence = splitStrList[middleRow]
            #making the dashes get properly placed
            if i == 0 and splitStrList[middleRow][0] != "0":
                putDash = True
            if w == 0:
                    putDash = False
            #create the rows
            if middleRow+i+1< len(grid) or middleRow -(i+1)>0:
                sequence = createSequence(w, middleColumn, currentSequence, maxValue) 
                string = transformToString(putDash, sequence)
                #making the dashes get properly placed
                if sequence[0] != "0" and string[0] == " ":
                    putDash = True
                else:
                    putDash = False
                #appending them to a list
                otherRows.append(string)
        #creating the main row(center)      
        currentSequence = splitStrList[0]
        sequence = createSequence(i+1, middleColumn, currentSequence, maxValue)
        string = transformToString(putDash, sequence) 
        #making the dashes get properly placed
        if currentSequence[0] != "0" and string[0] == " ":
            putDash = True
        else:
            putDash = False
        #creating a blank row (with only 0s) for the extras on top and bottom of the "diamond"
        emptyString = ""
        for i in string:
            if i.isnumeric():
                emptyString = emptyString+"0"
            else: 
                emptyString = emptyString+" "
        #creating each grid
        while len(currentGrid)  < middleRow - len(otherRows):
            currentGrid.append(emptyString)
        for x in range(len(otherRows)*2+1):
            if x < len(otherRows) and len(currentGrid) < len(grid):
                currentGrid.append(otherRows[x])
            elif x == len(otherRows) and len(currentGrid) < len(grid):
                currentGrid.append(string)
            elif x > len(otherRows) and len(currentGrid) < len(grid):
                currentGrid.append(otherRows[(len(otherRows))-x])
            else:
                break
        while len(currentGrid) < len(grid):
            currentGrid.append(emptyString)
        #appending each grid    
        results.append(currentGrid)
    return results

# Uncomment the following print to test your function without pytest
# Décommenter la suite pour des tests sans pytest

#print(part_2(2,[' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 9 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0'])) # Expected: '8111'



#print(part_3(2,[' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 9 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0']))
for i in part_3(2,[' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 5 0 0 0 0 0 0 0 0']):
    print("\n")
    print("\n")
    for x in i:
        print(x)

# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_4.py
This is the template file for the part 4 of the Prelim 3.
Ceci est le fichier template pour la partie 4 du Prelim 3.
"""

def part_4(nbr_steps: int, grid: [str]) -> [[str]]:
    """
    Simulate the drop of water from many sources interractiong together

    Parameters:
        nbr_steps (int): The number of steps in the simulation.
        grid ([str]): The grid of starting info

    Returns:
        [[str]]: A list of grids for the number of steps.
    """
    answer = []
    ### You code goes here ###
    ### Votre code va ici ###
    grids = []
    splitStrList = [] 
    middleRow = []
    middleColumn = []
    startingValues = []
    
    def createGridsForOneNumber(splitStrList, middleRow, middleColumn, maxValue, nbr_steps, grid):
        putDash = False
        results = []
        def createSequence(rangeInt: int, middleColumn: int, maxValue: int):
            currentSequence = ["0" if x.isnumeric() else " " for x in splitStrList[0]]
            if maxValue-i-1 >=0:
                currentSequence[middleColumn] = str(maxValue-i-1)
            for x in range(rangeInt):
                if middleColumn+x+1 < len(currentSequence) and maxValue-i-1 >=0 : 
                    currentSequence[middleColumn+x+1] = str(maxValue-i-1)
                if middleColumn-x > 0 and maxValue-i-1 >=0: 
                    currentSequence[middleColumn-(x+1)] = str(maxValue-i-1)
            return currentSequence
        def transformToString(putDash: bool, currentSequence: [str]) -> str:
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
        #create a grid
        for i in range(0, nbr_steps):
            #resetting the variables
            currentGrid = []
            otherRows = []
            #making the dashes get properly placed
            if i == 0 and splitStrList[middleRow][0] != "0":
                putDash = True           
            #creating the rows above and beneath the main one(center one)
            for w in range(1+i):
                #making the dashes get properly placed
                if i == 0 and splitStrList[middleRow][0] != "0":
                    putDash = True
                if w == 0:
                        putDash = False
                #create the rows
                if middleRow+i+1< len(grid) or middleRow -(i+1)>0:
                    sequence = createSequence(w, middleColumn, maxValue) 
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
            sequence = createSequence(i+1, middleColumn, maxValue)
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

    #splitting the main grid
    for i in range(len(grid)):
        splitStrList.append(grid[i].split())

    #finding the center row, center column and the number in that position
    for i in range(len(splitStrList)):
        for x in range(len(splitStrList[i])):
            if splitStrList[i][x] != "0":
                middleRow.append(int(i))
                middleColumn.append(int(x))
                startingValues.append(int(splitStrList[i][x]))

    #creating each grid
    for i in range(len(middleColumn)):
        grids.append(createGridsForOneNumber(splitStrList, middleRow[i], middleColumn[i], startingValues[i], nbr_steps, grid))
    
    def mergeGrids(allGrids, currentStep, singleGrid):
        
        mergedGrid = []
        
        amountOfGrids = len(allGrids)
        
        lengthOfAGrid = len(allGrids[0][0])
        
        lengthOfEachLine = len(allGrids[0][0][0])
        
        #each line
        for i in range(lengthOfAGrid):
            currentString = ""
            #each character
            for j in range(lengthOfEachLine):
                #only getting the numbers
                if singleGrid[i][j] != " ":
                    #creating/resetting the variables
                    numbersInPlace = []
                    numberInPlace = 0
                    #adding the numbers to a list
                    for x in range(amountOfGrids):
                        numbersInPlace.append(int(str(allGrids[x][currentStep][i][j-1]) + str(allGrids[x][currentStep][i][j])))
                    #adding up all the numbers together
                    for x in numbersInPlace:
                        numberInPlace = x+numberInPlace
                    
                    #formatting them into a string
                    match int(numberInPlace):
                        case _ if int(numberInPlace) < 0:
                            currentString = currentString + str(numberInPlace)
                        case _ if int(numberInPlace) >= 0:
                            currentString = currentString + str(f" {numberInPlace}")
            #appending each string to get a grid  
            mergedGrid.append(currentString)    
                
        
        return mergedGrid
    
    
    #putting each merged grid into the answer       
    for i in range(nbr_steps):
        answer.append(mergeGrids(grids, i, grid))
        
    
    return answer


# Uncomment the following print to test your function without pytest
# Décommenter la suite pour des tests sans pytest

#TESTING
for x in part_4(2,[' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 9 0 0',
                    ' 0 0 0 0 0 0 0 7 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0']):
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    for i in x:
        print(i)

#print(part_4(2,[' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 5 0 0 0 0 0 0 0 0']))
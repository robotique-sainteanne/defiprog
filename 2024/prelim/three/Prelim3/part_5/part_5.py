# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_5.py
This is the template file for the part 5 of the Prelim 3.
Ceci est le fichier template pour la partie 5 du Prelim 3.
"""

def part_5(grid: [str]) -> str:
    """
    Find the actions to take from x to the $.

    Parameters:
        grid (str): The grid with all relevant positions and water drops

    Returns:
        str: A list of actions to take to get to the $
    """
    answer = ""
    ### You code goes here ###
    ### Votre code va ici ###
    def mergeGrids(allGrids, currentStep, singleGrid):
        splitStrList = []

        mergedGrid = []
        
        amountOfGrids = len(allGrids)
        
        lengthOfAGrid = len(allGrids[0][0])
        
        lengthOfEachLine = len(allGrids[0][0][0])

        longest = max(allGrids)
        
        # Fill the difference between the smallest and biggest lists in allGrids with arrays of 0s
        delta = len(max(allGrids)) - len(min(allGrids))
        for i in range(len(allGrids)):
            if allGrids[i] != max(allGrids):
                for j in range(delta):
                    allGrids[i].append([f'{' ' + ('0 ' * (len(max(allGrids[0])) - 1)) + '0'}'] * len(longest[len(longest)-1]))

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

        for x in range(len(mergedGrid)):
            strList = []
            for i in range(len(mergedGrid[x])):
                if mergedGrid[x][i].isnumeric():
                    strList.append(f"{mergedGrid[x][i-1]}{mergedGrid[x][i]}")
            splitStrList.append(strList)

        return splitStrList
    
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
    available_directions_damage = {}
    available_directions_distance = {}
    waves = True
    splitStrList = []
    middleRow = []
    middleColumn = []
    startingValues = []
    grids = []
    # Split the grid like in part_3
    for i in range(len(grid)):
        splitStrList.append(grid[i].split())
    
    # Retrieve the positions of both the boat and the destination
    for k in range(len(splitStrList)):
        for j in range(len(splitStrList[k])):
            if splitStrList[k][j] != '0' and splitStrList[k][j] != 'x' and splitStrList[k][j] != '$':
                middleRow.append(k)
                middleColumn.append(j)
                startingValues.append(int(splitStrList[k][j]))
            elif splitStrList[k][j] == '$':
                destinationRow = k
                destinationColumn = j
            elif splitStrList[k][j] == 'x':
                boatRow = k 
                boatColumn = j

    # Retrieve the grids
    for i in range(len(middleColumn)):
        grids.append(createGridsForOneNumber(splitStrList, middleRow[i], middleColumn[i], startingValues[i], startingValues[i], grid))

    # The algorithm itself. Heres how it works:
    """
    First off, we assess the distance between the boat and the destination by a formula I created. Then,
    we check if there are still waves. The way this algorithm works is by evading all the waves and then going to the destination once the waves die out.
    After this, we move on to assessing how much damage will be taken if we move in all 4 directions. This is done using a dictionary in which the keys are the directions
    and the values are the amount of damage we would take going to that position. We then make a list of the directions that moving into would give us minimal damage. If
    staying stationnary is among the options in this list, we also must check that there is no waves surrounding the boat to make sure that when the wave moves next step, 
    the boat doesn't come into contact with it. If there are no surrounding waves that would hit in the next step, we choose the stationary option and don't alter the values 
    of the boatRow and boatColumn and we add 'S' to the answer. If however, staying stationary is not a good option since there are waves that will hit in the next step, we 
    then choose one of the directions that causes minimal value while also decreasing the distance between the boat and the destination. If there are no more waves detected,
    we simply write out the path to the destination in answer.
    """
    step = 0
    while boatRow != destinationRow and boatColumn != destinationColumn:
        # Calculate the number of squares that separate the boat and the destination. If this value is 10, the boat is right ontop
        distanceToDestination = 10*(abs(destinationRow-boatRow)) + 1*(abs(destinationColumn-boatColumn))
        splitStrList = mergeGrids(grids, step, grid)
        best_option = ''
        chooseStationary = False
        # Check if there are still waves
        for i in range(len(splitStrList)):
            for j in range(len(splitStrList[i])):
                if splitStrList[i][j] != ' 0' and splitStrList[i][j] != ' 1' and splitStrList[i][j] != '-1':
                    waves = True
                    break
            if waves == True:
                break
            waves = False
        
        # If there are still waves, do the best job at evading them.
        if waves == True:
            # Map the damages to the different possible directions
            available_directions_damage['U'] = int(splitStrList[boatRow-1][boatColumn]) if boatRow != 0 else 'Direction not available'
            available_directions_damage['D'] = int(splitStrList[boatRow+1][boatColumn]) if boatRow < len(splitStrList)-1 else 'Direction not available'
            available_directions_damage['R'] = int(splitStrList[boatRow][boatColumn+1]) if boatColumn > 0 else 'Direction not available'
            available_directions_damage['L'] = int(splitStrList[boatRow][boatColumn-1]) if boatColumn < len(splitStrList[0])-1 else 'Direction not available'
            available_directions_damage['S'] = int(splitStrList[boatRow][boatColumn])

            # Determine which directions deal the least damage
            minimal_directions = [dmg for dmg in available_directions_damage if available_directions_damage[dmg] == min(available_directions_damage.values())]

            if 'S' in minimal_directions and int(splitStrList[boatRow-1][boatColumn]) <= 1 and int(splitStrList[boatRow+1][boatColumn]) <= 1 and int(splitStrList[boatRow][boatColumn+1]) <= 1 and int(splitStrList[boatRow][boatColumn-1]) <= 1:
                chooseStationary = True
            
            # Calculate how far we would be from the destination for each choice of direction
            for k in range(len(minimal_directions)):
                if minimal_directions[k] == 'U':
                    available_directions_distance['U'] = 10*(abs(destinationRow-(boatRow-1))) + 1*(abs(destinationColumn-boatColumn))
                elif minimal_directions[k] == 'D':
                    available_directions_distance['D'] = 10*(abs(destinationRow-(boatRow+1))) + 1*(abs(destinationColumn-boatColumn))
                elif minimal_directions[k] == 'R':
                    available_directions_distance['R'] = 10*(abs(destinationRow-boatRow)) + 1*(abs(destinationColumn-(boatColumn+1)))
                elif minimal_directions[k] == 'L':
                    available_directions_distance['L'] = 10*(abs(destinationRow-boatRow)) + 1*(abs(destinationColumn-(boatColumn-1)))
            
            # Determine the best option. If we default to stationary, make the best option Stationary, represented by 'S'
            best_option = min(available_directions_distance, key=available_directions_distance.get) if chooseStationary == False else 'S'
            answer = answer + best_option

            if best_option == 'U':
                boatRow = boatRow - 1
            elif best_option == 'D':
                boatRow = boatRow + 1
            elif best_option == 'R':
                boatColumn = boatColumn + 1
            elif best_option == 'L':
                boatColumn = boatColumn - 1
            elif best_option == 'S':
                boatColumn = boatColumn
                boatRow = boatRow

        # If there are no more waves append to answer the instructions to get to the target as fast as possible      
        else:
            while boatRow != destinationRow and boatColumn != destinationColumn:
                if boatRow < destinationRow:
                    answer = answer + 'D'
                    boatRow = boatRow + 1
                elif boatRow > destinationRow:
                    answer = answer + 'U'
                    boatRow = boatRow - 1
                if boatColumn < destinationColumn:
                    answer = answer + 'R'
                    boatColumn = boatColumn + 1
                elif boatColumn > destinationColumn:
                    answer = answer + 'L'
                    boatColumn = boatColumn - 1
        step += 1
    
    



    return answer


# Uncomment the following print to test your function without pytest
# Décommenter la suite pour des tests sans pytest

grid1 = [' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 x 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 7 0 0',
' 0 0 3 0 0 0 0 0 0 0',
' 0 0 0 0 0 $ 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0']

grid2 = [' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 $ 0 0 0 0 0 5 0',
' 0 0 0 9 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 7 0 x',
' 0 0 0 0 5 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0']

grid3 = [' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 6 0 0 0 0',
' 0 5 0 0 0 0 0 0 $ 0',
' 0 0 0 3 0 0 0 0 0 0',
' 0 0 0 0 0 0 4 0 0 0',
' 0 x 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 8 0 0 0 0 0']

print(part_5(grid1))
print(part_5(grid2))
print(part_5(grid3))

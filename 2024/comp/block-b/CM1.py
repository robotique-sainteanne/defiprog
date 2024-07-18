### Queens everywhere (50 points) ###
import random
def solve(size):
    fullBoard = []
    coordinates = []
    testedCoordinates = []
    for x in range(size):
        currentRow = []
        for i in range(size):
            currentRow.append(0)
        fullBoard.append(currentRow)

    while len(coordinates)<size:
        testedCoordinates = []
        while True:
            foundCoordinate = False
            isOnDiagonal = False
            queenX, queenY = random.randint(1, size)-1, random.randint(1, size)-1
            queenCoordinates = [queenX, queenY]
            testedCoordinates.append(queenCoordinates)
            if queenCoordinates not in coordinates:
                foundCoordinate = True
                if queenCoordinates[0]+queenCoordinates[1]+1 == size:
                    foundCoordinate = False
                    isOnDiagonal = True
                if queenCoordinates[0] == queenCoordinates[1]:
                    foundCoordinate = False
                    isOnDiagonal = True
                
                if isOnDiagonal == False:
                    queenFrontDiagonal = queenCoordinates[1]-queenCoordinates[0]
                    queenBackDiagonal = queenCoordinates[0]+queenCoordinates[1]
                    for coordinate in coordinates:
                        if coordinate[0] == queenCoordinates[0] or coordinate[1] == queenCoordinates[1]:
                            foundCoordinate = False
                            break
                        frontDiagonal = coordinate[1]-coordinate[0]
                        backDiagonal = coordinate[0]+coordinate[1]

                        if frontDiagonal == queenFrontDiagonal or backDiagonal == queenBackDiagonal:
                            foundCoordinate = False
                            break

            if len(testedCoordinates) == size*size-len(coordinates):
                coordinates = []
                testedCoordinates = []    
            
                            
            if foundCoordinate == True:
                break          
        coordinates.append(queenCoordinates)

    return coordinates

n = 4

for x in range(10):
    print(solve(n))
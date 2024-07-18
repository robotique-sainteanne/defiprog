### Vertical horizon (15 points) ###

def solve(array):
    finalArray = []
    for j in range(len(array[0])):
        currentArray = []
        for i in array:
            currentArray.append(i[j])
        finalArray.append(currentArray)
        

    return finalArray

print(solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
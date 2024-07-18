### Palindrole (30 points) ###

def solve(L):
    index = 0
    wordLength = len(L)
    order = 0
    firstHalf, secondHalf = "", ""
    actualMiddle = int(wordLength/2) if (wordLength/2)%2 ==0 else int(wordLength/2-0.5)
    if (wordLength/2)%2 !=0:
        previousHalf = L
        while True:
            middle = actualMiddle
            firstHalf = ""
            secondHalf = ""
            for x in range(index):
                middle = int(middle/2)

            if (len(previousHalf)/2)%2 !=0:
                previousHalf = previousHalf[:middle] + previousHalf[middle+1:]
            
            currentString = previousHalf[:middle*2]
            previousHalf = currentString
            print(currentString)
            for i in range(middle):
                firstHalf = firstHalf+currentString[i]
                secondHalf = secondHalf+ currentString[len(currentString)-i-1]
            if(len(firstHalf)) == 0:
                break
            print(firstHalf)
            print(secondHalf)
            if secondHalf == firstHalf:
                order = order+1
            else:
                break
            index = index+1
    else:
        while True:
            middle = actualMiddle
            firstHalf = ""
            secondHalf = ""
            for x in range(index):
                middle = int(middle/2)
            currentString = L[:middle*2]
            print(currentString)
            for i in range(middle):
                firstHalf = firstHalf+currentString[i]
                secondHalf = secondHalf+ currentString[len(currentString)-i-1]
            if(len(firstHalf)) == 0:
                break
            print(firstHalf)
            print(secondHalf)
            if secondHalf == firstHalf:
                order = order+1
            else:
                break
            index = index+1
        
    return order

print(solve('ooroo'))
### Squaresception (20 points) ###

def solve(n):
    fullLength = n*2+1
    totalLength = n*2-1
    currentLineArray = []
    previousLine = ""
    for i in range(fullLength):
        currentLine = ""
        if i<n:
            amountOfDashes = (n-i)*2-1
        elif i == n:
            amountOfDashes = 0
        else:
            amountOfDashes = (i-n)*2-1
        
        amountOfStraights = totalLength-amountOfDashes
        if i == n:
            amountOfStraights = n*2
        

        
        currentLine = ""
        for j in range(int(amountOfStraights/2)):
            currentLine = currentLine+"│"
        
        if i<n:
            currentLine = currentLine+"┌"
        elif i == n:
            currentLine = currentLine+" "
        else:
            currentLine = currentLine+"└"
        
        for j in range(amountOfDashes):
            currentLine = currentLine+"─"
        
        if i<n:
            currentLine = currentLine+"┐"
        elif i == n:
            currentLine = currentLine
        else:
            currentLine = currentLine+"┘"

        for j in range(int(amountOfStraights/2)):
            currentLine = currentLine+"│"
        
        currentLineArray.append(currentLine)
            
    return currentLineArray


n = 4
for x in range(len(solve(n))):
    print(solve(n)[x])

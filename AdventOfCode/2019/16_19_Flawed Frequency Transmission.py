##kieran thompson


def getPattern(numberOfDigits, size):
    basePattern=[0,1,0,-1]
    newPattern=[]
    
    for numberInBasePattern in basePattern:
        for i in range(numberOfDigits):
            newPattern.append(numberInBasePattern)

    while( len(newPattern) < size+1):
        newPattern = newPattern + newPattern
        
    newPattern.pop(0)       
    return newPattern

def part1(phaseNo, timesRepeated):

    file = open("input.txt","r")
    line = file.read()
    file.close()
    inputArray = list(line) * timesRepeated

    #TESTS
    #inputArray = [1,2,3,4,5,6,7,8]
    #inputArray = [8,0,8,7,1,2,2,4,5,8,5,9,1,4,5,4,6,6,1,9,0,8,3,2,1,8,6,4,5,5,9,5]
    #inputArray = [1,9,6,1,7,8,0,4,2,0,7,2,0,2,2,0,9,1,4,4,9,1,6,0,4,4,1,8,9,9,1,7]

    answer = []

    resultSum = []
    for phases in range(1, (phaseNo+1)):
        
        answer=[]
        for lines in range(1,len(inputArray)+1):
            resultSum = []
            pattern = getPattern(lines, len(inputArray))
            
            for index in range(len(inputArray)):
                resultSum.append( int(inputArray[index]) * pattern[index])
                            
            phaseTemp = (abs(sum(resultSum)) % 10)
            #print(phaseTemp)
            answer.append(phaseTemp)
        inputArray=[]
        inputArray=answer
        
    
    
    print("one is : " + str(  inputArray[0:8]))

print("---")
part1(100, 1)

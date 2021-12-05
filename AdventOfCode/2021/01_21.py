def part1():
    with open('input21.txt') as f:
        depthReadings = f.readlines()
    measuredIncreases = 0

    currentValue = depthReadings[0]
    for reading in depthReadings:
        if int(reading) > int(currentValue):
            measuredIncreases+=1
        currentValue = reading

    return measuredIncreases
    
print("Part 1: The number of increasing readings is: " + str(part1()))

def part2():
    with open('input21.txt') as f:
        depthReadings = f.readlines()
    measuredIncreases = 0

    currentWindowSum = sum([int(depthReadings[0]), int(depthReadings[1]), int(depthReadings[2])])
    for startingWindowIndex in range(1, len(depthReadings)-2):
        nextSum = sum([int(depthReadings[startingWindowIndex]), int(depthReadings[startingWindowIndex+1]), int(depthReadings[startingWindowIndex+2])])
        if nextSum > currentWindowSum:
            measuredIncreases+=1
        currentWindowSum = nextSum
        
    return measuredIncreases
print("Part 2: The number of increasing window readings is: " + str(part2()))

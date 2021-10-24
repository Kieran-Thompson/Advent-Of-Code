def part1():
    level = 0

    inputBracketList = list(open("Input15.txt","r").read())
    for bracket in inputBracketList:
        if ("(" == bracket):
            level+=1
        elif (")" == bracket):
            level-=1
    return level
    
print("Part 1 Ans: Level = " + str(part1()))


def part2():
    position = 0
    level = 1

    inputBracketList = list(open("Input15.txt","r").read())
    for bracket in inputBracketList:
        if ("(" == bracket):
            level+=1
        elif (")" == bracket):
            level-=1

        if (-1 == level):
            return position
        else:
            position+=1
    return -1

print("Part 2 Ans: Position = " + str(part2()))

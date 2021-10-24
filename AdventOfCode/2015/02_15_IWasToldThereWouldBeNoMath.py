def part1():
    totalAreaOfAllBoxes = 0
    dimensionsOfBoxInput = list(open("Input15.txt","r").readlines())

    for box in dimensionsOfBoxInput:
        box.replace('\n','')
        dimensions = box.split('x')

        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])

        totalBoxAreaWithSlack = 0
        boxSideAreas = [l*w, w*h, h*l]
        boxSideAreas.sort()

        boxAreaWithSlack = (2 * sum(boxSideAreas)) + boxSideAreas[0]

        totalAreaOfAllBoxes += boxAreaWithSlack

    return totalAreaOfAllBoxes
print("Part 1 Ans: total area = " + str(part1()))


def part2():
    totalRibbonLength = 0
    dimensionsOfBoxInput = list(open("Input15.txt","r").readlines())

    for box in dimensionsOfBoxInput:
        box.replace('\n','')
        dimensions = box.split('x')

        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])

        boxSideLengths = [l, w, h]
        boxSideLengths.sort()

        minLengthAroundBox = 2 * (boxSideLengths[0] + boxSideLengths[1])
        cubicLengthRibbon =  l * w * h

        boxRibbonLength = minLengthAroundBox + cubicLengthRibbon
        totalRibbonLength += boxRibbonLength

    return totalRibbonLength

print("Part 2 Ans: total ribbon = " + str(part2()))

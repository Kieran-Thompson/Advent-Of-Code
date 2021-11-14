def part1():
    slopeMap = open("input2020.txt", "r").readlines()
    treeHit = 0
    crossSectionLength = len(slopeMap[0])-1
    along = 0 

    for height in range(0, len(slopeMap)):
        if (str(slopeMap[height][along]) == '#'):
            treeHit+=1
        along = (along + 3) % crossSectionLength 
    return treeHit

print("Part 1: Trees hit = " + str(part1()))

def part2():
    slopeMap = open("input2020.txt", "r").readlines()
    treeHitAns = []
    crossSectionLength = len(slopeMap[0])-1 

    movement = [ (1, 1), (3, 1), (5, 1) , (7, 1) , (1 ,2)  ]

    for index in range(len(movement)):
        treeHit = 0
        along = 0
        drop = movement[index][1]
        moveRight = movement[index][0] 
        for height in range(0, len(slopeMap), drop):
            if (str(slopeMap[height][along]) == '#'):
                treeHit+=1
            along = (along + moveRight) % crossSectionLength 
        treeHitAns.append(treeHit)
    product = 1
    for x in treeHitAns:
        product *= x
    return product

print("Part 2: Trees array answer = " + str(part2()))
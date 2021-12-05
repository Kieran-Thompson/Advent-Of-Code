def part1():
    with open('input21.txt') as f:
        courseSteps = f.readlines()
    depth = 0
    horizontal = 0

    for step in courseSteps:
        stepParts = step.replace('\n','').split(' ')

        if stepParts[0] == 'forward':
            horizontal+= int(stepParts[1])
        elif stepParts[0] == 'down':
            depth += int(stepParts[1])
        elif stepParts[0] == 'up':
            depth -= int(stepParts[1])
    return (depth * horizontal)


print('Part 1: Horizontal * depth = ' + str(part1()))

def part2():
    with open('input21.txt') as f:
        courseSteps = f.readlines()
    depth = 0
    horizontal = 0
    aim = 0
    

    for step in courseSteps:
        stepParts = step.replace('\n','').split(' ')

        if stepParts[0] == 'forward':
            horizontal+= int(stepParts[1])
            depth += aim * int(stepParts[1])
        elif stepParts[0] == 'down':
            aim += int(stepParts[1])
        elif stepParts[0] == 'up':
            aim -= int(stepParts[1])
    return (depth * horizontal)
    
print('Part 2: Horizontal * depth (with aim) = ' + str(part2()))
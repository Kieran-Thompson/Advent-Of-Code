def part1(target):
    lines = open("intput2020.txt","r").read().splitlines()
    for number in range(len(lines)):

        for secNum in range(number + 1, len(lines)):

            if target == int(lines[number]) + int(lines[secNum]):
                return int(lines[number]) * int(lines[secNum])

def part2(target):
    lines = open("intput2020.txt","r").read().splitlines()
    for number in range(len(lines)):

        for secNum in range(number + 1, len(lines)):
            for thirdNum in range(secNum + 1, len(lines)):
                if target == int(lines[number]) + int(lines[secNum]) + int(lines[thirdNum]):
                    return int(lines[number]) * int(lines[secNum]) * int(lines[thirdNum])

print(part1(2020))

print(part2(2020))

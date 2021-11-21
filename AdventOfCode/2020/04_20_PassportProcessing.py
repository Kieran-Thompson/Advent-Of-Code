def part1(passportString):
    ans = 0
    passportPart = ""
    completePassports = []

    for fragement in passportString:
        if fragement == "\n":
            completePassports.append(passportPart[:-1])
            passportPart = ""
        else:
            passportPart = passportPart + fragement.replace("\n"," ")

    completePassports.append(passportPart)

    for passport in completePassports:
        count = passport.count(":")

        if count == 8:
            ans = ans + 1
        elif count == 7 and passport.count("cid") == 0:
            ans = ans + 1

    return ans


passportList = open("input2020.txt", "r").readlines()

print("Part 1: Number of valid passports =  " + str(part1( passportList)))

def part2(passportString):
    passportPart = ""
    completePassports = []
    ans = 0

    for fragement in passportString:
        if fragement == "\n":
            completePassports.append(passportPart[:-1])
            passportPart = ""
        else:
            passportPart = passportPart + fragement.replace("\n"," ")

    completePassports.append(passportPart)

    heightScale = ['in', 'cm']
    eyeColours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] 
    hexChars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f'  ]
    for passport in completePassports:
        count = passport.count(":")

        if count == 8 or (count == 7 and passport.count("cid") == 0):
            passportSectionList = passport.split(' ')
            PassportDico = {}
            validPassportSection = True
            for section in passportSectionList:
                parts = section.split(':')
                if parts[0] == 'byr':
                    if (int(parts[1]) not in range(1920,2003)):
                        validPassportSection = False
                elif parts[0] == 'iyr':
                    if (int(parts[1]) not in range(2010,2021)):
                        validPassportSection = False
                elif parts[0] == 'eyr':
                    if (int(parts[1]) not in range(2020,2031)):
                        validPassportSection = False
                elif parts[0] == 'hgt':
                    if (parts[1][-2:] not in heightScale):
                        validPassportSection = False
                    elif( parts[1][-2:] == 'in' and int(parts[1][:-2]) not in range(59, 77)):
                        validPassportSection = False
                    elif( parts[1][-2:] == 'cm' and int(parts[1][:-2]) not in range(150, 194)):
                        validPassportSection = False
                elif parts[0] == 'hcl':
                    if(parts[1][0] != '#'):
                        validPassportSection = False
                    elif(len(parts[1][1:]) != 6):
                        validPassportSection = False
                    else:
                        for character in parts[1][1:]:
                            if character not in hexChars:
                                validPassportSection = False
                elif parts[0] == 'ecl':
                    if (parts[1] not in eyeColours):
                        validPassportSection = False
                elif parts[0] == 'pid':
                    if (len(parts[1]) != 9):
                        validPassportSection = False
            if validPassportSection: 
                ans = ans + 1
    return ans

            
print("Part 2: The number of valid passports = " + str(part2(passportList)))





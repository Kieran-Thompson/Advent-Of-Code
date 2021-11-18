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


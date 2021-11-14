passwordList = open("input2020.txt", "r").readlines()

def part1():
    validPasswords = 0

    for passwordScheme in passwordList:
        passwordScheme = passwordScheme.split(" ")

        frequencies = passwordScheme[0].split("-")
        minFreq = int(frequencies[0])
        maxFreq = int(frequencies[1])

        letter = (passwordScheme[1]).replace(":","")

        password = passwordScheme[2]

        letterFreq = password.count(letter)
        if (letterFreq <= maxFreq and letterFreq >= minFreq):
            validPasswords+=1

    return validPasswords

print("Part 1: The number of vaild passwords is: " + str(part1()))

def part2():
    validPasswords = 0

    for passwordScheme in passwordList:
        passwordScheme = passwordScheme.split(" ")
        
        positions = passwordScheme[0].split("-")
        positionA = int(positions[0])-1
        positionB = int(positions[1])-1
        
        letter = (passwordScheme[1]).replace(":","")

        password = passwordScheme[2]
    
        if (password[positionA] == letter and password[positionB] != letter
            or password[positionB] == letter and password[positionA] != letter):
            validPasswords+=1

    return validPasswords

print("Part 2: The number of vaild passwords is: " + str(part2()))
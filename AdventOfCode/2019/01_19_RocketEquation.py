###Kieran Thompson
###02/12/19

def getInputFromFile():
    data = []
    file = open("input.txt","r")
    
    for item in file:
        data.append(item.replace("\n",""))
    file.close()
    return data


def getSumOfModuleFuel():

    ##modules
    modulesInSpaceCraft = getInputFromFile()
    fuelForModule = []
    

    for module in modulesInSpaceCraft:
        tempAns = round(int(module)//3)-2        
        fuelForModule.append(tempAns)
        
    return sum(fuelForModule)

def getTotalOfAllFuel():
    total = 0
    modulesInSpaceCraft = getInputFromFile()
    for module in modulesInSpaceCraft:
        while 1:
            module = round(int(module)//3)-2
            if module <= 0:
                break
            total += module
    return total

##Part 1
print("part 1 = " + str(getSumOfModuleFuel()))

##Part 2    
print("part 2 = " + str(getTotalOfAllFuel()))

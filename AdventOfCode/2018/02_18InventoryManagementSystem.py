##Kieran Thompson

##append each row to a list
def readfile():
    data = []
    file = open("input.txt","r")
    for row in file:
        row = str(row)
        row = row.replace("\n","")
        data.append(str(row))
    return data


##Part 1

##given input, return the number of element repeated 2 and 3 times, multipled together
def checkSum():
    
    two = 0
    three=0
    data = readfile()
    
    for row in data:
        dico={}
        
        for letter in row:
            if letter in dico.keys():
                dico[letter] = dico[letter]+1
            else:
                dico[letter] = 1
        if 2 in dico.values():
            two = two + 1
            
        if 3 in dico.values():
            three = three + 1
            
    return three*two

##Part 2
def loopThroughlist(listOfStrings):
    for i in range(len(listOfStrings)-1):
        hamming_set(listOfStrings, listOfStrings[i])


def hamming_set(listOfStrings, string1):
    for item in listOfStrings:
        if (1 == hamming_distance(item, string1)):
            print(item, string1)
        

def hamming_distance(string1, string2): 
    distance = 0
    for i in range(len(string1)-1):
        if string1[i] != string2[i]:
            distance += 1
    return distance

file = open("input.txt", "r")
readlist = file.readlines()
loopThroughlist(readlist)

##Strings easy to compare


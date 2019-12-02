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


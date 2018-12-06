##Kieran Thompson

##part 1


##get the polymer, removing reacting elements
def reacting(a,A):
    
    if a.lower() == a and A == A.upper():
        if a.upper() == A:
            return True
        else:
            return False
    elif A.lower() == A and a == a.upper():
        if A.upper() == a:
            return True
        else:
            return False
    return False

##main run    

def polymers():
    file = open("input.txt","r")
    l = file.readline()
    ans = []
    ans.append(l[0])
    for i in l[1:]:
        if len(ans) == 0:
            ans.append(i)
        else:
            if reacting(ans[-1],i) == True:
                ans.pop()                    
            else:
                ans.append(i)
    return len(ans)

##part 2

##get the polymer that does the most reduction, when it has been removed

###get the best polymer
def bestpolymer():
    alphabet="abcdefghijklmnopqrstuvwxyz"
    values = []
    file = open("input.txt","r")
    l = file.readline()
    for letter in alphabet:
        a =l.replace(letter,"")
        a = a.replace(letter.upper(),"")
        ans = []
        ans.append(a[0])
        for i in a[1:]:
            if len(ans) == 0:
                ans.append(i)
            else:
                if reacting(ans[-1],i) == True:
                    ans.pop()                    
                else:
                    ans.append(i)
        values.append(len(ans))
    return min(values)
print(bestpolymer())






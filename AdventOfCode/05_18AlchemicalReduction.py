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
        
        
print(len(ans))
    
    









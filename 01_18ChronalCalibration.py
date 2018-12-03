###Kieran Thompson

##Part 1

###get the frequency, starting at 0, changing from values in a list
def frequencyChanges(changes):
    frequency = 0
    for i in changes:
        frequency = frequency + i

    return frequency


##Part 2

##get the frequency that appears twice, when go through the list, possibly mulitple time

def dupChanges(data):
    ans=0
    flag =True
    freqList = {}
    frequency = 0
    while(flag==True):
        for i in data:       

            if frequency in freqList.keys():
                freqList[frequency] = freqList[frequency] +1
                ans = frequency
                
                return ans
            else:
                freqList[frequency] = 0
        
            frequency = frequency + i
        
    


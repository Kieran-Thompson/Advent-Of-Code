##Kieran Thompson

##part 1


##get the areas of the duplicate claims 
def overlapClaims():
    cloth={}
    dup={}
    a=0
    
    file=open("input.txt","r")
    for line in file:
        line = line.split()
        
        point = line[2].split(",")       
        
        x = point[0]
        y = point[1].replace(":","")
        xrange = line[3].split("x")[0]
        yrange = line[3].split("x")[1]
        for row in range(0, int(xrange)):
            for col in range(0,int(yrange)):
                tempx = int(x) + row
                tempy = int(y) +col
                coor = (tempx,tempy)
                if coor in cloth.keys():
                    dup[coor] = 1
                else:
                    cloth[coor] = 1
        
    return len(dup.keys())









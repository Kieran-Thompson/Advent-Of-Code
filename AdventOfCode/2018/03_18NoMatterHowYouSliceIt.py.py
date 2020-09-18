##Kieran Thompson

##part 1


##get the areas of the duplicate claims 
def overlapClaims():
    cloth={}
    dup={}
    a=0

    file=open("3_18.txt","r")
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
                tempy = int(y) + col
                coor = (tempx,tempy)
                if coor in cloth.keys():
                    dup[coor] = 1
                else:
                    cloth[coor] = 1

    return len(dup.keys())

#get the line that is not overlapped onto
def GetIDOfNoDoubleClaims():
    cloth={}
    dup={}
    a=0

    file=open("3_18.txt","r")
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
                tempy = int(y) + col
                coor = (tempx,tempy)
                if coor in cloth.keys():
                    cloth[coor] = cloth[coor] + 1 
                else:
                    cloth[coor] = 1

    file=open("3_18.txt","r")
    flag = True
    for line in file:
        flag = True
        line = line.split()

        point = line[2].split(",")

        x = point[0]
        y = point[1].replace(":","")
        xrange = line[3].split("x")[0]
        yrange = line[3].split("x")[1]
        for row in range(0, int(xrange)):
            for col in range(0,int(yrange)):
                tempx = int(x) + row
                tempy = int(y) + col
                coor = (tempx,tempy)
                if cloth[coor] > 1:
                    flag = False
        if flag == True:
            print(line)

##call to get answer to part1 
print("Part 1 answer = " + str(overlapClaims()))

##call to get answer to part2
print("The answer to part 2 is:")
GetIDOfNoDoubleClaims()
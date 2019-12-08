####Kieran Thompson
####08/12/19

from collections import Counter


def neverDecrease(value):
     number = list(str(value))
     for i in range(len(number)-1):
          if number[i] > number[i+1]:
               return False
     return True
          
def repeatedpair(value):
     number = list(str(value))
     for i in range(len(number)-1):
          if number[i] == number[i+1]:
               return True
     return False

def repeatedpairNoGroup(value):
     number = list(str(value))
     for i in range(len(number)-1):
          if number[i] == number[i+1]:
               frequency = Counter(number)
               if(frequency[str(number[i])]==2):
                    return True
     return False

def main1():
     low = 165432
     high = 707912 +1

     valid = []

     for number in range(low, high):
          if(repeatedpair(number)and neverDecrease(number)):
               valid.append(number)   
          

     return len(valid)

def main2():
     low = 165432
     high = 707912 +1

     valid = []

     for number in range(low, high):
          if(repeatedpairNoGroup(number)and neverDecrease(number)):
               valid.append(number)   
          

     return len(valid)

print("part1: " + str(main1()))
print("part2: " + str(main2()))

####Kieran Thompson
####08/12/19

from collections import Counter

def getImageData():
     imageData = open('input.txt','r').read()
     return imageData

def getConstants():
     ##tuple with demensions (width,"tall(height)")
     dimensions = (25,6)
     return dimensions

def getImageRows():
     image = getImageData()
     imageDimensions = getConstants()
     imageRows = []
     layerNo = 0

     i = 0
     step = imageDimensions[0] * imageDimensions[1]

     for layer in range(len(image)//step):
          imageRows.append([])
          
          for pixel in range(i,i+step):
               imageRows[layerNo].append(image[pixel])

          i = i+step
          layerNo = layerNo +1       

     return imageRows

def getMinValue(valueN, imageDataRows):
     currentMinRow = []
     minValueN = 99999
          
     for row in imageDataRows:
          tempRowCount = Counter(row)
          #print(tempRowCount)
          if tempRowCount[str(valueN)] < minValueN:
              currentMinRow = tempRowCount
              minValueN = tempRowCount[str(valueN)]
          
     return currentMinRow

def getMultipledValues_A_B(CountedList, a, b):
     ans = CountedList[str(a)] * CountedList[str(b)]
     return ans 

print("part1: "+ str(getMultipledValues_A_B(getMinValue(0,getImageRows()), 1, 2)))

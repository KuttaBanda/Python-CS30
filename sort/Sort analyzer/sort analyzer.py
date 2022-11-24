import time

def bubbleSort(list1):  
    for numcompare in range(len(list1)-1, 0, -1):  
        for j in range(numcompare):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  


def selectionSort(anArray):
    for i in range(len(anArray)-1):
        minposition=i
        for j in range(i+1, len(anArray)):
            if anArray[j]<anArray[minposition]:
                minposition=j

        anArray[minposition], anArray[i]=anArray[i], anArray[minposition]
    return anArray


def insertionSort(anArray):
    for i in range(1, len(anArray)):
        temp=anArray[i]
        j=i-1
        while j>=0 and temp<anArray[j]:
            anArray[j+1]=anArray[j]
            j-=1
        anArray[j+1]=temp
    return anArray


# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
print(randomData[0:50])
print(reversedData[0:50])
print(nearlySortedData[0:50])
print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")
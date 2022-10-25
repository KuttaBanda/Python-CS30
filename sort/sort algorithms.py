def bubbleSort(anArray):  
    for i in range(0,len(anArray)-1):  
        for j in range(len(anArray)-1):  
            if(anArray[j]>anArray[j+1]):  
                temp = anArray[j]  
                anArray[j] = anArray[j+1]  
                anArray[j+1] = temp  
    return anArray  

def selectionSort(anArray):
    for i in range(len(anArray)-1):
        minIndex=i
        for j in range(i+1, len(anArray)):
            if anArray[j]<anArray[minIndex]:
                minIndex=j
        anArray[i], anArray[minIndex]=anArray[minIndex], anArray[i]
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




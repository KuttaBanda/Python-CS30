import random
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


#randomArray=[]
#for i in range(10000):
#    randnum=random.randint(1,10000)
#    randomArray.append(randnum)

#start=time.time()
#bubbleSort(randomArray)
#print(time.time()-start)
#--------------------------------------------------
# reversedArr=[]
# for i in range(10000, 0, -1):
#     reversedArr.append(i)

# start=time.time()
# insertionSort(reversedArr)
# print(time.time()-start)
#---------------------------------------------------
# nearly=[]
# for i in range(1, 10001):
#     nearly.append(i)

# for i in range(5):
#     rand1=random.randint(0,9999)
#     rand2=random.randint(0,9999)
#     nearly[rand1], nearly[rand2]=nearly[rand2], nearly[rand1]

# start=time.time()
# selectionSort(nearly)
# print(time.time()-start)
#------------------------------------------------------------------
# fewunique=[]
# for i in range(1, 5001):
#     fewunique.append(i)

# for i in range(50):
#     rand1=random.randint(-10000, 10000)
#     randind=random.randint(0,4999)
#     fewunique[randind]=rand1
    
# start=time.time()
# selectionSort(fewunique)
# print(time.time()-start)
from operator import index

from numpy import append


test=[1, 2, 3, 4, 5, 6, 7, 8, 9]

def contains(aList, item):
    for elem in aList:
        if elem==item:
            return True
    return False


def indexOf(list, element):
    for i in range(len(list)):
        if list[i]==element:
            return i
    return -1

def reverse(aList):
    reverseList=[]
    for i in range(len(aList)-1, -1, -1):
        #have to do len(aList)-1 because start is inclusive and -1 for end as end is exclusive
        reverseList.append(aList[i])
    return reverseList
        


def swap(aList, index1, index2):
    item1swap=aList[index1]
    aList[index1]=aList[index2]
    aList[index2]=item1swap



def indexOfMin(aList):
    current=aList[0]
    indexmin=0
    for i in range(len(aList)):
        if aList[i]<current:
            indexmin=i
            current=aList[i]
    return indexmin


print(contains(test,10))
print(indexOf(test,4))
print(reverse(test))
swap(test, 0, 3)
print(indexOfMin(test))

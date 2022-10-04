from cgi import test
from operator import index


test=[1, 2, 3, 4, 5, 6, 7, 8, 9]
reverselist=[]

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
print(indexOf(test, 4))

def reverse(aList):
    for item in aList[::-1]:
        reverselist.append(item)
    return reverselist
print(reverse(test))

def swap(aList, index1, index2):
    item1swap=aList[index1]
    item2swap=aList[index2]
    aList[index1]=item2swap
    aList[index2]=item1swap
    print(aList)
swap(test, 0, 3)

def indexOfMin(aList):
    current=aList[0]
    indexmin=0
    for i in range(len(aList)):
        if aList[i]<current:
            indexmin=i
            current=aList[i]
    return indexmin
print(indexOfMin(test))
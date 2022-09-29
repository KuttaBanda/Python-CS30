from operator import index


array=[1, 2, 3, 4, 5, 6, 7, 8, 9]
reverselist=[]

def contains(aList, item):
    l1 = [item]
    for i in l1:
        if i in aList:
            print(item, " is in the list")
        else:
            print(item, " is not in the list")


contains(array, 1)

def indexOf(list, element):
    for i in list:
        if list[i]==element:
            return i
        return -1

print(indexOf(array, 4))

def reverse(aList):
    for item in aList[::-1]:
        reverselist.append(item)
    return reverselist

print(reverse(array))

def swap(aList, index1, index2):
    item1swap=aList[index1]
    item2swap=aList[index2]
    aList[index1]=item2swap
    aList[index2]=item1swap
    print(aList)

swap(array, 0, 3)

def indexOfMin(aList):
    current=aList[0]
    indexmin=0
    for i in range(len(aList)-1):
        if aList[i]<current:
            indexmin=i
            current=aList[i]
        elif aList[i]>current:
            indexmin=aList.index(current)
    print(indexmin)

print(indexOfMin(array))
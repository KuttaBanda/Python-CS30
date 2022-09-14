array=[1, 2, 3]

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
            print(element, " is in the list at index", i)
            break
        elif i==len(list):
            print(element, " is not in the list")

indexOf(array, 2)


from math import floor


nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]

def linearSearch(list, element):
    for i in range(len(list)):
        if list[i]==element:
            return i
    return -1


def binarySearch(list, element):
    low=0
    high=len(list)-1
    mid=0

    while low <= high:
        mid = floor((low+high)/2)
        if element == list[mid]:
            return mid
        elif element < list[mid]:
            high=mid-1
        elif element > list[mid]:
            low=mid+1
    return -1



nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]


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


print(insertionSort(nums))
print(insertionSort(words))

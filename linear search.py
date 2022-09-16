nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]

def linearSearch(list, element):
    for i in range(len(list)):
        if list[i]==element:
            print(i)
            break
        elif i==len(list)-1 and i!=element:
            print("-1")
            break

linearSearch(nums, 70)
linearSearch(words, "at")
linearSearch(unsorted, 100)
linearSearch(words, "cow")

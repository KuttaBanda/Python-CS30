nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]

def linearSearch(list, element):
    for i in range(len(list)):
        if list[i]==element:
            return i
    return -1


print(linearSearch(nums, 70))
print(linearSearch(words, "at"))
print(linearSearch(unsorted, 100))
print(linearSearch(words, "cow"))


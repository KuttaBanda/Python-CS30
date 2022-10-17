# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re
import time
from math import floor

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

def main():
    # Load data files into lists
    global dictionary
    dictionary = loadWordsFromFile("spell check/data-files/dictionary.txt")
    global aliceWords
    aliceWords = loadWordsFromFile("spell check/data-files/AliceInWonderLand.txt")
    for i in range(len(aliceWords)):
      aliceWords[i]=aliceWords[i].lower()

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])
# end main()

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()
    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()

loop = True
while loop:
  # Print Main Menu
  print("")
  print("Main Menu")
  print("1: Spell Check a Word (Linear Search)")
  print("2: Spell Check a Word (Binary Search)")
  print("3: Spell Check Alice in Wonderland (Linear Search)")
  print("4: Spell Check Alice in Wonderland (Binary Search)")
  print("5: Exit")
  selection = input("What Option? (1-5): ")

  if selection=="1":
    linearword=input("Please enter a word: ")
    start_lin1=time.time()
    linearSearch(dictionary, linearword)
    print("")
    print("Linear search is starting...")
    if linearSearch(dictionary, linearword) != -1:
      print(linearword, "is IN the dictionary at position",str(linearSearch(dictionary, linearword))+"."+"("+ str(time.time()-start_lin1), "seconds"+ ")")
    else:
      print(linearword, "is NOT IN the dictionary.")
  
  elif selection=="2":
    binaryword=input("Please enter a word: ")
    start_bin1=time.time()
    binarySearch(dictionary, binaryword)
    print("")
    print("Binary search is starting...")
    if binarySearch(dictionary, binaryword) != -1:
      print(binaryword, "is IN the dictionary at position",str(binarySearch(dictionary, binaryword))+"."+"("+ str(time.time()-start_bin1), "seconds"+ ")")
    else:
      print(binaryword, "is NOT IN the dictionary.")  
  
  elif selection=="3":
    linCount=0
    start_lin2=time.time()
    print("")
    print("Linear search is starting...")
    for i in range(len(aliceWords)):
      linearSearch(dictionary, aliceWords[i])
      if linearSearch(dictionary, aliceWords[i]) == -1:
        linCount += 1
    print("Number of words not found in dictionary: "+str(linCount),"("+str(time.time()-start_lin2), "seconds"+")")
  
  elif selection=="4":
    binCount=0
    start_bin2=time.time()
    print("")
    print("Binary search is starting...")
    for i in range(len(aliceWords)):
      binarySearch(dictionary, aliceWords[i])
      if binarySearch(dictionary, aliceWords[i]) == -1:
        binCount += 1
    print("Number of words not found in dictionary: "+str(binCount),"("+str(time.time()-start_bin2), "seconds"+")")

  elif selection=="5":
    loop=False
    print("EXITED PROGRAM")

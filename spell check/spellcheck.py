# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re 

from search.searchfunction import linearSearch, binarySearch   


def main():
    # Load data files into lists
    global dictionary
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    global aliceWords
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

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
  print("1: Spell Check a Word (Linear Search")
  print("2: Spell Check a Word (Binary Search)")
  print("3: Spell CHeck Alice in Wonderland (Linear Search)")
  print("4: Spell Check Alice in Wonderland (Lineae Search)")
  print("5: Exit")
  selection = input("What Option? (1-5): ")

  if selection=="1":
    linearword=input("Please enter a word: ")
    linearSearch(dictionary, linearword)
    if linearSearch(dictionary, linearword) != -1:
      print(linearword, "is in the dictionary at position, ", linearSearch(dictionary, linearword),".")
    else:
      print(linearword, "is not in the dictionary.")
    

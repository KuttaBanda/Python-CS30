import pip


import random
import numpy as np
randnums = np.random.randint(1, 100, 35)
honours = randnums[randnums > 80]
max_value = numpy.max(randnums)
print(max_value)

loop = True
while loop:
    print("")
    print("Main Menu")
    print("1. Display all Grades")
    print("2. Display Honours")
    print("3. Stats")
    print("4. Randomize Grades")
    print("5. Exit")
    selection = input("What Option? (1-5): ")

    if selection == "1":
        print("ALL GRADES: ")
        print(*randnums, sep='\n')
    elif selection == "2":
        print("HONOURS: ")
        print(*honours, sep='\n')


import pip


import random
import numpy as np
randnums = np.random.randint(1, 100, 35)
honours = randnums[randnums > 80]
max_value = np.max(randnums)
min_value = np.min(randnums)
avg_value = round(np.average(randnums))

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
    elif selection == "3":
        print("STATS")
        print("Highest Grade: " , max_value)
        print("Lowest Grade: " , min_value)
        print("Average Grade: " , avg_value)
    elif selection == "4":
        newrandnums = np.random.randint(1, 100, 35)
        print("GRADES HAVE BEEN RANDOMIZED")
    elif selection == "5":
        print("EXITED")
        loop = False

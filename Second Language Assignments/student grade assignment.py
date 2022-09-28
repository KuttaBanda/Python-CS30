import pip
import random

randnums=[]
for i in range(35):
    randnum=random.randint(0,100)
    randnums.append(randnum)

max_value = max(randnums)
min_value = min(randnums)
avg_value = round(sum(randnums)/len(randnums))

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
        for element in randnums:
            print(element,"%")
    elif selection == "2":
        print("HONOURS: ")
        for elem in randnums:
            if elem >= 80:
             print(elem,"%")
    elif selection == "3":
        print("STATS")
        print("Highest Grade: " , max_value, "%")
        print("Lowest Grade: " , min_value, "%")
        print("Average Grade: " , avg_value, "%")
    elif selection == "4":
        newrandnums = []
        for i in range(35):
                       
    elif selection == "5":
        print("EXITED")
        loop = False

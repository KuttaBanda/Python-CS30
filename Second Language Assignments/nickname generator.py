import pip


import random

nickname_list=["Crusher", "Che", "Dimes", "Captain", "Prez"]

print("Set Your Name: ")
first_name=input("Please enter first name: ")
last_name=input("Please enter last name: ")

loop = True
while loop:
    print("")
    print("Main Menu", "(", first_name, last_name, ")")
    print("1. Change Name")
    print("2. Display a Random Nickname")
    print("3. Display All Nicknames")
    print("4. Add a Nickname")
    print("5. Remove a Nickname")
    print("6. Exit")
    selection = input("What Option? (1-6): ")

    if selection=="1":
        print("CHANGE NAME")
        first_name=input("Please enter first name: ")
        last_name=input("Please enter last name: ")
        print("Current name is " + first_name + " " + last_name + ".")
    elif selection=="2":
        print("RANDOM NICKNAME")
        print(first_name + " " + "'" + random.choice(nickname_list) + "'" + " " + last_name)
    elif selection=="3":
        print("ALL NICKNAMES")
        for elem in nickname_list:
            print(first_name + " '" , elem, "' " + last_name)
    elif selection=="4":
        print("ADD A NICKNAME")
        new_name=input("Please enter a nickname to add: ")
        
        if new_name not in nickname_list:
                nickname_list.append(new_name)
                print(new_name, " has been added to the nickname list.")
        else:
                print(new_name, " is already in the nickname list.")
    elif selection=="5":
        print("REMOVE A NICKNAME")
        old_name=input("Please enter a nickname to remove: ")
        if old_name in nickname_list:
                nickname_list.remove(old_name)
                print(old_name, " has been removed from the nickname list.")               
        else:
                print(old_name, " was not found in the nickname list.")
    elif selection == "6":
        print("EXITED")
        loop = False
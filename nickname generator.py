from tkinter import N
import pip


import random
import numpy as np

nickname_list=["Crusher", "Che", "Dimes", "Captain", "Prez"]

loop = True
while loop:
    print("")
    print("Main Menu")
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
    if selection=="3":
        print("ALL NICKNAMES")
        for elem in nickname_list:
            print(first_name + " " , elem, " " + last_name)
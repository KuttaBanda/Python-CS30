from turtle import shape


import pip
import numpy as np
import random

names=["Kyrie", "LeBron", "Luka"]
phone=["578-389-2891", "389-289-2783", "366-287-2378"]
email=["bestdriibles@hotmail.com", "theking@yahoo.com", "sloveniandude@gmail.com"]

contacts=np.matrix([names, phone, email])

loop = True
while loop:
    print("")
    print("Main Menu")
    print("1. Display Contact Names")
    print("2. Search for Contact")
    print("3. Edit Contact")
    print("4. New Contact")
    print("5. Remove Contact")
    print("6. Exit")
    selection = input("What Option? (1-6): ")

    if selection=="1":
        print("DISPLAY CONTACT NAMES")
        for elem in names:
            print(elem)

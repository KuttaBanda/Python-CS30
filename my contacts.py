from turtle import shape


import pip
import numpy as np
import random

names=["Kyrie", "LeBron", "Luka"]
phone=["578-389-2891", "389-289-2783", "366-287-2378"]
email=["bestdribbles@hotmail.com", "theking@yahoo.com", "sloveniandude@gmail.com"]

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
    elif selection=="2":
        print("SEARCH FOR CONTACT")
        name_search=input("Who's contact name do you want to search?: ")
        l1=[name_search]
        for i in l1:
            if i in names:
                index_name=names.index(name_search)
                print("")
                print(name_search)
                print(contacts[1, index_name])
                print(contacts[2, index_name])
            else:
                print("Name doesn't exist in contact list.")
    elif selection=="3":
        print("EDIT CONTACT")
        edit_name=input("Who's contact info do you want to change?: ")
        l2=[edit_name]
        for i in l2:
            if i in names:
                indexof_name=names.index(edit_name)
                edited_num=input("What is the new number?: ")
                contacts[1,indexof_name]=edited_num
                edited_email=input("What is the new email?: ")
                contacts[2, indexof_name]=edited_email
    elif selection=="4":
        print("NEW CONTACT")
        new_name=input("What is the name of your new contact?: ")
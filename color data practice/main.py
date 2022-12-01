# COLOR DATA PRACTICE

import json

# Load Color Data from JSON file
file = open("F:\Python-CS30\color data practice\color-data.json", "r")
dataStr = file.read()
file.close()

color_data = json.loads(dataStr)


loop = True
while loop:
    print("")
    print("1. Print name and family")
    print("2. Print name and brightness if > 200")
    print("3. Print colours in 'Red' or 'Pink' families")
    print("4. Print colours from one family")
    print("5. Print colours based on letter")
    print("6. Exit")
    selection=input("What Option?: ")

    if selection=="1":
        for color in color_data:
            print(color["name"]+","+color["family"])
    elif selection=="2":
        for color in color_data:
            if color["brightness"]>200:
                print(color["name"]+","+str(color["brightness"]))
    elif selection=="3":
        countPorR=0
        for color in color_data:
            if color["family"]=="Red" or color['family']=="Pink":
                countPorR+=1
        print(countPorR)
    elif selection=="4":
        countfam=0
        familyname=input("What family do you want to display?:  ")
        for color in color_data:
            if color["family"]==familyname:
                countfam+=1
                print(color["name"]+","+color["family"])
        print(countfam)
    elif selection=="5":
        letter=input("What letter do you want to search up by?: ")
        countLet=0
        for color in color_data:
            if color["name"][0]==letter
                    countLet+=1
                    print(color["name"])
        print(countLet)
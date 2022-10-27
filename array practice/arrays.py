months=["January", "June", "July"]

joy=[]
for i in range(700):
    joy.append("joy")

number7=[]
for i  in range(500):
    number7.append("7")

import random
randomfloat=[]
for i in range(5000):
    randdec=round(random.uniform(0.0,99.9),1)
    randomfloat.append(randdec)

randomdecimal=[]
for i in range(300):
    randdec=round(random.uniform(0.0,39.9),1)
    randomdecimal.append(randdec)

multiples4=[range]
for i in range(20, 801, 4):
    multiples4.append(i)

evens=[]
for i in range(100, 9, -2):
    evens.append(i)

colors_str = "red,orange,yellow,green,blue,indigo,violet"
colors=colors_str.split(",")

cities_str = "Edmonton;Calgary;Vancouver;Saskatoon;Winnipeg"
cities=cities_str.split(";")


name=[]
loop = True
while loop:
    print("")
    selection=input("Enter Name(write 'done' if want to end input): ")

    if selection!="done":
        name.append(selection)
    elif selection=="done":
        loop=False
        print(name)
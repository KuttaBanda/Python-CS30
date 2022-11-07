songs=[
    {
        "title": 'Majhail',
        "artist": 'AP Dhillon',
        "genre": 'Punjabi Rap'
    },
    {
        "title": "MooseDrilla",
        "artist": 'Sidhu Moosewala',
        "genre": 'Punjabi Drill'
    },
    {
        "title": 'Heyy',
        "artist": 'Lil Baby',
        "genre": "Rap"
    },
    {
        "title": 'Doja',
        "artist": 'Central Cee',
        "genre": 'British Drill'
    }
]

favs=[]

loop=True
while loop:
    print("")
    print("Main Menu")
    print("1. Display all Data")
    print("2. Display data based on criteria")
    print("3. Sort by a property")
    print("4. Add to favourites")
    selection=input("What option?: ")

    if selection=="1":
        for i in range(len(songs)):
            print("")
            print(songs[i]["title"])
            print(songs[i]["artist"])
            print(songs[i]["genre"])
    elif selection=="2":
        properties=input("Which property do you want displayed?: ")
        properties2=input("Do you wish to have another criteria? (if not, type 'No'): ")
        for i in range(len(songs)):
            if properties2!="No":
                print("")
                print(songs[i][properties])
                print(songs[i][properties2])
            else:
                print("")
                print(songs[i][properties])
    elif selection=="3":
        propertysort=input("What property do you want to sort by?: ")
        sortarr=sorted(songs, key=lambda i: i[propertysort])
        for i in range(len(songs)):
            print("")
            print(sortarr[i]["title"])
            print(sortarr[i]["artist"])
            print(sortarr[i]["genre"])
    elif selection=="4":
        favsong=input("Which song do you want to add to your favorites list?: ")
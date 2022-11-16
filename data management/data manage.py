import json
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
    },
    {
        "title": "Vaar",
        "artist": "Sidhu Moosewala",
        "genre": "Folk"
    }
]

favs=[]

loop=True
while loop:
    print("")
    print("Main Menu")
    print("1. Display all data")
    print("2. Display data based on criteria")
    print("3. Sort by a property")
    print("4. Add to favourites")
    print("5. Remove from favourites")
    print("6. Display favourites")
    print("7. Exit")
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
        for i in songs:
            if i['title']==favsong:
                favs.append(i)
    elif selection=="5":
        removesong=input("What song do you want to remove from the favourites?: ")
        for i in favs:
            if i['title']==removesong:
                favs.remove(i)
    elif selection=="6":
        f = open('F:\Python-CS30\data management\mydata.json')
        favs=json.load(f)
        if len(favs)==0:
            print("No songs in favourites list")
        else:
            for i in range(len(favs)):
                print("")
                print(favs[i]['title'])
                print(favs[i]['artist'])
                print(favs[i]['genre'])
        f.close()              
    elif selection=="7":
        loop=False
        print("EXITED")
    
    #After every time the menu shows up, dump the list to stay up to date
    with open('F:\Python-CS30\data management\mydata.json', 'w') as f:
        json.dump(favs, f)

    
    

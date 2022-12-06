import json
loop=False

#Login System
users=[]
def newUser(username, password):
    return{
        "username": username,
        "password": password,
        "favs": []
    }

loopSignIn=True
while loopSignIn:
    print("")
    print("1. Register")
    print("2. Sign-in")
    selectionUser=input("What option?: ")

    if selectionUser=="1":
        print("")
        userName=input("Username: ")
        password=input("Password: ")
        users.append(newUser(userName,password)) 
        print("Registered!")
        with open('F:\Python-CS30\data management\mydata.json', 'w') as file:
            json.dump(users, file)
    elif selectionUser=="2":
        file = open('F:\Python-CS30\data management\mydata.json')
        users=json.load(file)
        print("")
        userNameLog=input("Username: ")
        passwordLog=input("Password: ")
        for i in range(len(users)):
            if users[i]["username"]==userNameLog and users[i]["password"]==passwordLog:
                print("Login Successful!")
                loggedIn=i
                loopSignIn=False
                loop=True
        else:
            print("Login Unsuccesful :(")


                

 
#SONGS
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
    },
    {
        "title": "Her Loss",
        "artist": "Drake & 21 Savage",
        "genre": "Rap"
    },
    {
        "title": "Jatt Life Zone",
        "artist": "Varinder Brar",
        "genre": "Punjabi Trap"
    }
]



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
        for song in songs:
            if song['title']==favsong:
                users[loggedIn]["favs"].append(song)
                print(song['title']+" added to favourites")
    elif selection=="5":
        removesong=input("What song do you want to remove from the favourites?: ")
        for song in users[loggedIn]["favs"]:
            if song["title"]==removesong:
                i=list(users[loggedIn]["favs"]).index(song)
                del users[loggedIn]['favs'][i]
                print(song['title']+" removed from favourites")
    elif selection=="6":
        f = open('F:\Python-CS30\data management\mydata.json')
        favs=json.load(f)
        if len(favs)==0:
            print("No songs in favourites list")
        else:
            for i in range(len(users[loggedIn]["favs"])):
                print("")
                print(users[loggedIn]["favs"][i]['title'])
                print(users[loggedIn]["favs"][i]['artist'])
                print(users[loggedIn]["favs"][i]['genre'])
        f.close()              
    elif selection=="7":
        loop=False
        print("EXITED")
    
    #After every time the menu shows up, dump the list to stay up to date
    with open('F:\Python-CS30\data management\mydata.json', 'w') as file:
        json.dump(users, file)
    
    

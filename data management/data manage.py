from turtle import title


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
    }
]


loop=True
while loop:
    print("")
    print("Main Menu")
    print("1. Display all Data")
    print("2. Display data based on criteria")
    selection=input("What option?: ")

    if selection=="1":
        for i in range(len(songs)):
            print(songs[i]["title"])
            print(songs[i]["artist"])
            print(songs[i]["genre"])
            print("")
    elif selection=="2":
        properties=input("Which property do you want displayed?: ")
        for i in range(len(songs)):
            print(songs[i][properties])
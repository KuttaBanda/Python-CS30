import matplotlib.pyplot as plt

#data
#goals by season data
season_in_league=[1,2,3,4,5,6,7,8]
mcDavidGoals=[16,30,41,41,34,33,44,35]
eichelGoals=[24,24,25,28,36,2,14,15]
connorGoals=[0,2, 31, 34, 38, 26, 47, 21]

#careerpoints
players=["Connor McDavid", "Alex Ovechkin", "Auston Matthews", "Leon Draisaitl"]
points=[79,48,47,63]
nameInput=input("What is your name?: ")


class User:
    def __init__(self,name):
        self.name=name

    def goalsBySeason(self):
        plt.plot(season_in_league,mcDavidGoals, label="Connor McDavid")
        plt.plot(season_in_league,eichelGoals, label="Jack Eichel")
        plt.plot(season_in_league,connorGoals, label="Kyle Connor")
        plt.legend()
        plt.show()

    def pointsThisSeason(self):
        plt.bar(players, points)
        plt.show()

userName=User(nameInput)

def mainMenu():
    print("")
    print("HELLO", nameInput+"!")
    print("Welcome to the Python Hockey Stats Catalog main menu!")
    print("1. Line chart for goals vs seasons in league")
    print("2. Bar chart comparing current points for players in the 22-23 season")
    selection=int(input("What option do you choose?: "))

    if selection==1:
        userName.goalsBySeason()
    elif selection==2:
        userName.pointsThisSeason()
    else:
        print("Input is not valid")
    
    mainMenu()

mainMenu()
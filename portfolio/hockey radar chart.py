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

#goalie scatter
svPercent=[.921,.905,.912,.897,.896,.883,.918,.906,.913,.896,.895,.968,.915,.903,.897,.895,.894,.893,.919,.918,.892,.907,.904,.904,.885,.883,.908,.905,.902,.875,.936,.926,.912,.894,.893,.891,.917,.917,.908,.895,.868,.867,.927,.919,.918,.918,.918,.914,.902,.883,.883,.880,.880,.915,.910,.907,.902,.900,.898,.895,.888,.870,.923,.914,.913,.907,.889,.925,.924,.914,.910,.905,.924,.913,.907,.906,.894,.894,.919,.909,.906,.886]
ages=[41,38,37,37,37,37,35,35,34,34,34,33,33,33,33,33,33,33,32,32,32,31,31,31,31,31,30,30,30,30,29,29,29,29,29,29,28,28,28,28,28,28,27,27,27,27,27,27,27,27,27,27,27,27,26,26,26,26,26,26,26,26,26,25,25,25,25,25,24,24,24,24,24,23,23,23,23,23,23,22,22,21]

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
    
    def ageVsSavPercent(self):
        plt.scatter(ages, svPercent)
        plt.show()

userName=User(nameInput)

def mainMenu():
    print("")
    print("HELLO", nameInput+"!")
    print("Welcome to the Python Hockey Stats Catalog main menu!")
    print("1. Line chart for goals vs seasons in league")
    print("2. Bar chart comparing current points for players in the 22-23 season")
    print("3. Scatter plot comparing goalie save percentage vs age")
    print("4. Exit")
    selection=int(input("What option do you choose?: "))

    if selection==1:
        userName.goalsBySeason()
        mainMenu()
    elif selection==2:
        userName.pointsThisSeason()
        mainMenu()
    elif selection==3:
        userName.ageVsSavPercent()
        mainMenu()
    elif selection==4:
        print("EXITED")
    else:
        print("Input is not valid")
        mainMenu()
        
    

mainMenu()
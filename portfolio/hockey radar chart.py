import matplotlib.pyplot as plt

#data
season_in_league=[1,2,3,4,5,6,7,8]
mcDavidGoals=[16,30,41,41,34,33,44,35]
eichelGoals=[24,24,25,28,36,2,14,15]
connorGoals=[0,2, 31, 34, 38, 26, 47, 21]

nameInput=input("What is your name?: ")


class Graphs:
    def __init__(self,name):
        self.name=name

    def goalsBySeason(self):
        plt.plot(season_in_league,mcDavidGoals, label="Connor McDavid")
        plt.plot(season_in_league,eichelGoals, label="Jack Eichel")
        plt.plot(season_in_league,connorGoals, label="Kyle Connor")
        plt.legend()
        plt.show()

userName=Graphs(nameInput)


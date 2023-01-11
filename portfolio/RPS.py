from random import randint


choices=["rock", "paper","scissors"]

class player:
    def __init__(self):
        self.choice="None"
        self.score= 0

    def getInput(self, choice, run):
        for item in choices:
            if item==choice:
                print('Item selected')
                self.choice=choice
                return run
        print("Game Ended")
        run=False
        return run    

        





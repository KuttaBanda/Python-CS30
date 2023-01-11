from random import randint

runCode=False
choices=["rock", "paper","scissors"]

class player:
    def __init__(self):
        self.choice="None"
        self.score= 0

    def getInput(self, choice):
        for item in choices:
            if item==choice:
                print('Item selected')
                self.choice=choice
        print("That is not an item in RPS")
        





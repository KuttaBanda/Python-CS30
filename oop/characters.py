class Characters:
    def __init__(self, name, phrase1, phrase2):
        self.name=name
        self.phrase1=phrase1
        self.phrase2=phrase2
        self.level=0
    
    def speak(self, phraseNum):
        if phraseNum==1:
            print(self.phrase1)
        elif phraseNum==2:
            print(self.phrase2)

    def setLevel(self, newLevel):
        self.level=newLevel
        print(self.level)   

po=Characters("Po", "Skadoosh", "You have been blinded by pure awesomeness!")
mcqueen=Characters("McQueen", "I am speed", "Kachow!")

po.speak(1)
mcqueen.setLevel(2)
mcqueen.speak(2)
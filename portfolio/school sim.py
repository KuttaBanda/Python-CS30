import random

class Backpack:
    def __init__(self, color, size):
        self.color=color
        self.size=size
        self.items=[]
        self.open=False

    def openBag(self):
        self.open=True
        print("Bag Open")
    
    def closeBag(self):
        self.open=False
        print("Bag Closed")

    def putin(self, item):
        self.items.append(item)
        print(item + " in bag")

    def takeout(self, item):
        for object in self.items:
            if object==item:
                self.items.remove(object)
        print(item+" taken out")

gradeSelect=int(input("What grade are you in?(1-6): "))


if gradeSelect<=2:
    colourSelect=input("What colour bag do you have?: ")
    bag=Backpack(colourSelect, "small")
if gradeSelect>2 and gradeSelect<=4:
    colourSelect=input("What colour bag do you have?: ")
    bag=Backpack(colourSelect, "medium")
if gradeSelect>4 and gradeSelect<=6:
    colourSelect=input("What colour bag do you have?: ")
    bag=Backpack(colourSelect, "large")

possibleClasses=["Math", "Science", "Social", "Music", "English", "French", "Gym"]
todaySchedule=[]
print("Your Schedule for Today:")

for i in range(7):
    randomClass=(random.randint(0,6))
    if i!=3:
        print(possibleClasses[randomClass])
        todaySchedule.append(possibleClasses[randomClass])
    else: 
        print("Lunch Time!")
        todaySchedule.append("Lunch")

print("")
print("Pack your bag!")
bag.openBag()
print("Add items you need for all your classes.(Lunch has already been packed) When everything is packed and ready to go to school, type 'done'")
bag.putin("Lunch Kit")
packingloop = True
while packingloop:
    print("")
    itemAdd=input("What item do you want to add?: ")
    if itemAdd!="done":
        bag.putin(itemAdd)
    elif itemAdd=="done":
        packingloop=False
        bag.closeBag()
        print("Going to school...At school")
        

for currentClass in todaySchedule:
    randQuiz=random.randint(0,10)
    mathQ1=random.randint(0,12)
    mathQ2=random.randint(0,12)
    if currentClass!="Lunch":
        print("")
        print("You now have "+ currentClass)
        removeItem=input("Take out the item needed for this class: ")
        bag.openBag()
        bag.takeout(removeItem)
        print("Class Begins...Class proceeding...")
        if  randQuiz==10:
            print("SURPRISE! You have a district wide diagnostic test. Mandatory for all students")
            mathQ=input("What is ", mathQ1,"x", mathQ2," ?: ")
            if mathQ==str(mathQ1*mathQ2):
                print("Correct!")
            else:
                print("Incorrect.")
            socialQ=input("What year was Canada officially a country?: ")
            if socialQ=="1867":
                print("Correct1")
            else:
                print("Incorrect.")
            englishQ=input("What is this called?(,): ")
            if englishQ=="comma":
                print("Correct!")
            else:
                print("Incorrect.")
            scienceQ=input("What gas do plants produce?: ")
            if scienceQ=="CO2" or scienceQ=="carbon dioxide":
                print("Correct!")
            else:
                print("Incorrect.")
            print("Thank you for partaking in the this test")
            print("Class has ended. Pack your bags")
        else:
            print("Class has ended. Pack your bags")
        print("Packing bag...")
        bag.putin(removeItem)
        bag.closeBag()
        print("Bag has been packed. Go to your next class")
    else:
        print("It is Lunch Time!")
        bag.openBag()
        removeLunch=input("Remove Lunch(Y or N)?: ")
        if removeLunch=="Y":
            bag.takeout("Lunch Kit")
            print("Socializing...Eating Lunch...Joking around with friends...")
        else:
            print("Don't want lunch? Go take this time to socialize")
        print("Lunch is over. Time for class")
        bag.putin("Lunch Kit")
        bag.closeBag()


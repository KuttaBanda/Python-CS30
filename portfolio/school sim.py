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
    else: 
        print("Lunch Time!")

print("")
print("Pack your bag!")
bag.openBag()
print("Add items you need for all your classes. When everything is packed and ready to go to school, type 'done'")

packingloop = True
while packingloop:
    print("")
    itemAdd=input("What item do you want to add?: ")
    bag.putin(itemAdd)
    if itemAdd=="done":
        packingloop=False
        print("Going to school...At school")


    

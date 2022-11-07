# results=["Yes", "No", "No", 'Maybe', "No", "Yes","No", "Maybe"]

# countY=0
# countN=0
# CountMay=0
# for i in range(len(results)):
#     if results[i]=="Yes":
#         countY += 1
#     elif results[i]=="No":
#         countN += 1
#     else:
#         CountMay+=1

# print(countY, countN, CountMay)

ages=[1, 2, 3, 16, 18, 55, 96, 60, 10, 35]

countUnder=0
countOver=0
for i in range(len(ages)):
    if ages[i]< 18:
        countUnder += 1
    else:
        countOver += 1

print(countOver, countUnder)

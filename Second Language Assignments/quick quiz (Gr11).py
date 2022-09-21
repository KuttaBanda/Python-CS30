score = 0
print("WELCOME TO SPORTS QUIZ")
#Q1
ans1 = input("What sport uses a puck?")
if ans1.lower() == "hockey":
  print("CORRECT")
  score = score + 1
else:
  print("INCORRECT")
#Q2
ans2 = input("What sport does Lionel Messi play?")
if ans2.lower() == "soccer" or ans2.lower() == "football":
  print("CORRECT")
  score = score + 1
else:
  print("INCORRECT")
#Q3
ans3 = input("What sport is the NBA?")
if ans3.lower() == "basketball":
  print("CORRECT")
  score = score + 1
else:
  print("INCORRECT")
#Q4
ans4 = input("What league does Tom Brady play in?")
if ans4.lower() == "nfl":
  print("CORRECT")
  score = score + 1
else:
  print("INCORRECT")


#OUTPUT
finalScore = (score / 4) * 100

print ("Results" , score , "/4" , "(" , finalScore , "%)")

if score == 4:
  print("WOW!")
elif score == 3: 
  print("Good Job!")
elif score == 2:
  print("Good Luck Next Time!")
else:
  print("Please Study...")
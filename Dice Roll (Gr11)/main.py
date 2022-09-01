import random


loop = True
while loop:
  # Print Main Menu
  print("")
  print("DICE ROLL SIMULATOR")
  print("1: Roll Dice Once")
  print("2: Roll Dice 5 Times")
  print("3: Roll Dice 'n' Times")
  print("4: Roll Until Snake Eyes")
  print("5: Exit")
  selection = input("What Option? (1-5): ")

  if selection == "1":
    print("Roll Dice Once")
    randDice1 = random.randrange(1,7)
    randDice2 = random.randrange(1,7)
    sumDie = randDice1 + randDice2
    print(randDice1,"," ,randDice2, "( sum: ", sumDie, ")" )
  elif selection == "2":
    print("Roll Dice 5 Times")
    n = 1
    while n <= 5:
      randDice1 = random.randrange(1,7)
      randDice2 = random.randrange(1,7)
      sumDie = randDice1 + randDice2
      n += 1
      print(randDice1,"," ,randDice2, "( sum: ", sumDie, ")" )
  elif selection == "3":
    print("Roll Dice 'n' Times")
    nTimes = input("How many rolls?: ")
    n = 1
    while n <= int(nTimes):
       randDice1 = random.randrange(1,7)
       randDice2 = random.randrange(1,7)
       sumDie = randDice1 + randDice2
       n += 1
       print(randDice1,"," ,randDice2, "( sum: ", sumDie, ")" )
  elif selection == "4":
    print("Roll Until Snake Eyes")
    loopSnake = True
    while loopSnake:
      randDice1 = random.randrange(1,7)
      randDice2 = random.randrange(1,7)
      sumDie = randDice1 + randDice2
      print(randDice1,"," ,randDice2, "( sum: ", sumDie, ")" )
      if randDice1 == 1 and randDice2 == 2:
        print("1 , 1 ( sum: 2 )")
        print("You Rolled Snake Eyes!")
        loopSnake = False
  elif selection == "5":
    print("EXITED")
    loop = False
import random

choicesList=['P','S','R']   
userStats={'win':0,'lost':0,'tie':0}
winnerCombinations=['SP', 'PR', 'RS']

userChoice=""
compChoice=''
rounds=0
while True:
  try:
    rounds=int(input("How many rounds do you want to play? "))
    if rounds>0:
      break
    else:
      raise ValueError 
  except ValueError:
    print("Wrong input. Enter an integer value > 0.")

for i in range(1,rounds+1):
    print("****** ROUND %d ******" % i)
    compChoice=choicesList[random.randrange(0,3)]
    userChoice=input("Your turn. Input P for paper, S for scissors, R for rock. Wrong input = round is lost ;) ")
    userChoice=userChoice.upper().strip()

    if userChoice in choicesList:
        if userChoice==compChoice:
            userStats['tie']=userStats['tie']+1
            print("Computer has chosen %s too. TIE!" %compChoice)
        elif userChoice+compChoice in winnerCombinations:
            print("Your win! Computer took %s" %compChoice)
            userStats['win']=userStats['win']+1
        else:
            print("You lost! Computer took %s" %compChoice)
            userStats['lost']=userStats['lost']+1
    else:
        print("Wrong input, you have lost this round!")
        userStats['lost']=userStats['lost']+1
print("======= STATISTICS ======")
print("You won %d times.\nYou lost %d times.\nTies: %d" \
      % (userStats['win'],userStats['lost'],userStats['tie']))

      
    
    

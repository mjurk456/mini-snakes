#Hangmab ASCII picture from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
import re
import random
hangmanpic=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
hangmancount=0
wordBank=['notebook','assignment','facebook', 'childhood','computer']
usedLetters=[]
userChoice=''
rounds=7
word=wordBank[random.randrange(0,len(wordBank)-1)]
filler="-"
wordPattern=word[0]+filler*(len(word)-2)+word[-1]
usedLetters.append(word[0])
usedLetters.append(word[-1])
ltrs=[]
print(wordPattern)
while hangmancount < len(hangmanpic):
  userChoice=input("Your letter: ").lower().strip()
  if (not userChoice.isalpha()) or (len(userChoice)>1):
      print("Input a letter a-z.")
      continue
  if userChoice in usedLetters:
    print("This letter has been already used!")
  else:
    usedLetters.append(userChoice)
    print("USED LETTERS: %s" % " ".join(usedLetters))
    ltrs=[l.start() for l in re.finditer(userChoice, word)]
    if len(ltrs)<1:
      print("HANGMAN %s \n" % hangmanpic[hangmancount])
      hangmancount=hangmancount+1
    else:
      for p in ltrs:
        wordPattern=wordPattern[:p]+userChoice+wordPattern[p+1:]
    print(wordPattern)
    if wordPattern.find(filler)<0:
      print("You won!")
      break
if hangmancount==len(hangmanpic):
    print("You lose!")

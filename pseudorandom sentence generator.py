import random

adverb=[]
noun=[]
adjective=[]
verb=[]
sentence=""

fverb=open("verb.txt","r")
verb=fverb.readlines()
fverb.close()

fadverb=open("adverb.txt","r")
adverb=fadverb.readlines()
fadverb.close()

fnoun=open("noun.txt","r")
noun=fnoun.readlines()
fnoun.close()

fadj=open("adjective.txt","r")
adjective=fadj.readlines()
fadj.close()
while True:
    try:
        userAnswer=int(input("How many sentences do you want to generate? "))
        break
    except:
        print("Wrong input, use integer numbers!")
for i in range(userAnswer):
    sentence="A "+adjective[random.randrange(len(adjective))].strip() + \
          " "+noun[random.randrange(len(noun))].strip() + " " +\
          verb[random.randrange(len(verb))].strip() + " a " + \
          adjective[random.randrange(len(adjective))].strip() + \
          " " + noun[random.randrange(len(noun))].strip() + " " +\
          adverb[random.randrange(len(adverb))].strip()+"."
    print(sentence)

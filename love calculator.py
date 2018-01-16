##1. oba imiona zaczynają się na taką samą literę to daje to 20pkt.
##2. oba imiona zaczynają się samogłoską to daje to 10pkt.
##3. oba imiona zaczynają się spółgłoską to daje to 5pkt.
##4. w obu imionach jest taka sama liczba samogłosek to daje to 12 pkt.
##5. w obu imionach jest taka sama liczba spółgłosek to daje to 12 pkt.
##6. w obu imionach jest albo "l" albo "o" albo "v" albo "e" to daje to 7pkt.

def counting(source,example):
    a=0
    for i in range(len(source)):
       if source[i] in example: a=a+1
    return a
        
lovePoints=0
vowels="aeiuo"
consonants="qrtpsdfghjklzxcvbnmy"


while True:
    try:
        name1,name2=input("Input two names divided by comma (e.g. 'Jan, Joanna'): ").split(",")
        name1.lower().strip()
        name2.lower().strip()
        break
    except:
        print("Wrong input")

if name1[0]==name2[0]:
    lovePoints=lovePoints+20
if (name1[0] in vowels) and (name2[0] in vowels):
    lovePoints=lovePoints+10
if (name1[0] in consonants) and (name2[0] in consonants):
    lovePoints=lovePoints+5
if counting(name1,vowels)==counting(name2,vowels):
    lovePoints=lovePoints+12
if counting(name1,consonants)==counting(name2,consonants):
    lovePoints=lovePoints+12
if ((name1.find('l')>0) and (name2.find('l')>0)) \
   or ((name1.find('o')>0) and (name2.find('o')>0)) \
   or ((name1.find('v')>0) and (name2.find('v')>0)) \
   or ((name1.find('e')>0) and (name2.find('e')>0)):
    lovePoints=lovePoints+7

print("Your love points are %d" %lovePoints)
print("REMEMBER: your relationship depends only from you and your partner, not from the stupid love calculator!")

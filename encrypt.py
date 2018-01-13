encryptTable="qwertyuiopasdfghjklzxcvbnm,."
decryptTable="йцукенгшщзфывапролдячсмитьбю"

while True:
    #selecting work mode
    userMode=input("Input 1 to encrypt a sentence, 2 to decrypt a sentence, 3 to exit:")
    if userMode=="1":
        userString=str(input("Input a sentence to encrypt (letter case will be ignored):")).lower()
        transTable=str.maketrans(encryptTable,decryptTable)
        print(userString.translate(transTable))
    elif userMode=="2":
        userString=str(input("Input a sentence to decrypt (letter case will be ignored):")).lower()
        transTable=str.maketrans(decryptTable,encryptTable)
        print(userString.translate(transTable))
    elif userMode=="3":
        break
    else:
        print("Wrong input!")

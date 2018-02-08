#!/usr/bin/env python3

""" User class for Vigener's chipher.
All non-alfabet characters will be deleted.

Public methods:
    .set_key(word) = sets word as a coding word
    .set_text(msg) = sets msg as a text of a chipher 
    .encrypt() = returns encrypt string
    .decrypt() = returns decrypted string
"""


class Vigener():

    def __init__(self, word = "", text = ""):
        self.password = ""
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.msg = "" #final message
        if word:
            self.set_key(word)
        else:
            self.word = ""
        if text:
            self.set_text(text)
        else:
            self.text = ""
        


    def set_key(self, word):
        self.word = word.upper()


    def set_text(self, msg):
        #deleting all non-alphabetical characters
        msg = msg.upper()
        self.text = "".join([a for a in msg if a in self.alphabet])
        

    def __check(self):
        errMsg = ""    
        if not(self.word):
            errMsg = errMsg + "\nCoding word is not set."
        if not (self.text):
            errMsg = errMsg + "\nText is not set."
        if errMsg:
            print(errMsg)
            return False
        else:
            return True


    def __set_password(self, key):
        self.password = key * (len(self.text) // len(key)) \
                            + key[:len(self.text) % len(key)]        

    def __line(self, a):
        b = self.alphabet.find(a)
        return self.alphabet[b:] + self.alphabet[:b]

    
    def encrypt(self):
        if not self.__check():
            return None
        else:
            self.msg = ""
            self.__set_password(self.word)
            for i, letter in enumerate(self.text):
                self.msg = self.msg \
                           + self.__line(self.password[i]) \
                           [self.alphabet.find(letter)]
        return self.msg


    def decrypt(self):
        if not self.__check():
            return None
        else:
            key = ""
            for letter in self.word:
                key = key + self.alphabet[(len(self.alphabet) \
                                          - self.alphabet.find(letter)) \
                                          % len(self.alphabet)]
            self.__set_password(key)
            self.msg = ""
            for i, letter in enumerate(self.text):
                self.msg = self.msg \
                           + self.__line(self.password[i]) \
                           [self.alphabet.find(letter)]
            return self.msg
            

def main():
    a = Vigener()
    a.set_key("tajne")
    a.set_text("to jest bardzo tajny tekst.")
    print(a.encrypt()+"\n")
    b = Vigener("tajne", "MOSRWMBJEHSOCNNGYCROLT")
    print(b.decrypt())

if __name__ == "__main__":
    main()

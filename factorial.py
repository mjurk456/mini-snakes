#!/usr/bin/env python 3
""" Counts factorial n! """
import math

def main():
    userInput = ""
    while not userInput.isdigit():
        userInput = input("Enter n for n!: ")
    print("n! = %d" % math.factorial(int(userInput)))


if __name__ == "__main__":
    main()

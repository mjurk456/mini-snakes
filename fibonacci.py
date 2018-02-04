#!/usr/bin/env python3

"""Counting Fibonacci numbers without recursion"""

def fibonacci(n):
    #returns a list of n Fibonacci numbers
    array = [1, 1]
    for i in range(2, n):
        array.append(array[i-2] + array[i-1])
    return array


def main():
    userInput = ""
    while not userInput.isdigit():
        userInput = input("How many Fibonacci numbers do you want to get? ")
    print(fibonacci(int(userInput)))


if __name__ == "__main__":
    main()

          

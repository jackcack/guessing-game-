#this is a guess the number game

import random

name = input("hello what is your name: ")

print("hello " + name + ", I am thinking of number between 1 and 20 ")
secretNum = random.randint(1, 20)

for guesses in range(1, 7):
    print("take a guess")
    guess = int(input())

    if guess < secretNum:
        print("your guess is too low.")
    elif guess > secretNum:
        print("your guess is too high.")
    else:
        break # this condition is for the correct guess

if guess == secretNum:
    print("good job, " + name + " you guessed correct in " + str(guesses) + " guesses")
else:
    print("nope the number I was thinking of is " + str(secretNum))


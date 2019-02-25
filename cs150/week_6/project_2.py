# This project works with while loops and inputs .  Your program will generate a random value, and ask for your guess.
# Upon submitting your guess, the program will return back if your guess is too high or too low.
# This will continue until you guess the correct number in which the program will output:
# "Correct congratulations you answered in xx number of guess" . The program will then print out all of your guesses."
# Author: Jonathan E. Cirone @ 24 Feb 19

import random

print('Welcome to GuessTen')


def guessChecker(myGuess):
    numbersGuessed = []
    attempts = 0
    while True:
        try:
            randomNumber = random.randint(1, 10)
            userGuess = int(input(myGuess))
            if userGuess < 1 or userGuess > 10:
                print('Invalid Range\n')
                continue
        except ValueError:
            print('Invalid \n')
            continue
        else:
            if userGuess != randomNumber:
                numbersGuessed.append(userGuess)
                attempts += 1
                continue
            else:
                numbersGuessed.append(userGuess)
                attempts += 1
                print("***You guessed correctly!*** \n")
                print("Congratulations, here are your attempts: {} ".format(attempts))
                print('These were your guessed numbers: {}'.format(numbersGuessed))
                break


myGuess = guessChecker('Please guess a number [1-10]: \n')

# edited: JEC @ 2342

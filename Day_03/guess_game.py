# Guess the Number Game

from random import randrange


def guess_the_number(start:int):
    number_to_guess = randrange(start)

    while True:
        guess = input("Enter your guess: ")

        if int(guess) < number_to_guess:
            print("Too low! Try again.")
        elif int(guess) > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed the number.")
            break

guess_the_number(50)
    


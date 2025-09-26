# IC 1st fix the game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        #fixed string with int
        guess = float(input("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
            #changed if to elif
        elif float(guess == number_to_guess):
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif float(guess > number_to_guess):
            print("Too high! Try again.")
            #added attempts when you get it wrong
            attempts = attempts + 1
        elif float(guess < number_to_guess):
            print("Too low! Try again.")
            attempts = attempts + 1
        #no idiot proof added else
        else:
            print("Something went wrong try again later.")
        continue
    print("Game Over. Thanks for playing!")
start_game()
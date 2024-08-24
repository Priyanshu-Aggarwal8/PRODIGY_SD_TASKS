#Task 2: Program that generates a random number and challenges the user to guess it
#As the range of the random number isn't specified, ill be taking it from a range [1,100]

import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
                print(f"It took you {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")
guess_the_number()

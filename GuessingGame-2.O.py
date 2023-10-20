import random

name = input("Enter your name: ")

print(f"Welcome {name} to this Number Guessing Game")

computer_guess = random.randint(1,100)
# make_guess = input("Make a Guess: ")

guess = 0

while True:
    guess += 1
    user_guess = input("Enter your number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Invalid")

    if user_guess == computer_guess:
        print("You Guessed it right")
        break
    elif user_guess < computer_guess:
        print("You were too low")
    else:
        print("You were too high")

print("You guessed in", guess, "guesses")


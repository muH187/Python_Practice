import random

top_of_range = random.randint(1,50)

type_number = input("Type a number: ")
if type_number.isdigit():
    type_number = int(type_number)
    if type_number < 1:
        print("Please enter 1 or larger than 1")
else:
    print("Please enter a number next time")

guess = 0

while True:
    guess += 1
    make_guess = input("Make a guess: ")
    if make_guess.isdigit():
        make_guess = int(make_guess)
        if make_guess < 1:
            print("Please enter 1 or larger than 1")
    else:
        print("Please enter a number next time")

    if top_of_range == make_guess:
        print("You got it")
        break
    elif make_guess < top_of_range:
        print("You were too low")
    else:
        print("You were too high")
print("You got it in", guess, "guesses")


import random

print("Welcome to Rock Paper Scissors Game:)")

options = ('rock', 'paper', 'scissors')


running = True

while running:
    user = None
    computer = random.choice(options)

    while user not in options:
        user = input("Choose: rock, paper or scissors: ")

    print("User:", user)
    print("Computer:", computer)

    if computer == user:
        print("It's a tie")
    elif user == 'rock' and computer == 'paper':
        print("You lost")
    elif user == 'paper' and computer == 'scissors':
        print("You lost")
    elif user == 'scissors' and computer == 'rock':
        print("You lost")
    else:
        print("You win")

    if not input("Play Again? (y/n): ").lower() == 'y':
        running = False
print("Thanks for playing:)")

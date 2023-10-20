import random

print("Welcome to Rock Paper Scissors Game")

options = ("rock", "paper", "scissors")

user = None
computer = random.choice(options)

running = True

while running:
    user_choice = input("Choose: Rock, Paper and Scissors: ")
    print("You:", user_choice)
    print("Computer:", computer)
    if user_choice == computer:
        print("It's a tie")
    elif user_choice == 'rock' and computer == 'paper':
        print("You lost")
    elif user_choice == 'paper' and computer == 'scissors':
        print("You lost")
    elif user_choice == 'scissors' and computer == 'rock':
        print("You lost")
    else:
        print('You win')

    play = input("Play Again? (y/n): ")
    if play.lower() == 'y':
        continue
    else:
        running = False
print('Thanks for playing:)')
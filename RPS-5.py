import random

options = ['rock', 'paper', 'scissors']

user_wins = 0
computer_wins = 0
tie = 0

while True:
    user_choice = input("Type Rock/Paper/Scissors or q for quit: ").lower()
    random_number = random.randint(0,2)
    computer_pick = options[random_number]

    print('Computer picked:', computer_pick)
    print('You picked:', user_choice)

    if user_choice == 'q':
        break
    if user_choice not in options:
        print("Please enter valid option.")
        continue

    if user_choice == computer_pick:
        print("Tie")
        tie += 1
    elif user_choice == 'rock' and computer_pick == 'paper':
        print("You lost")
        computer_wins += 1
    elif user_choice == 'paper' and computer_pick == 'scissors':
        print("You lost")
        computer_wins += 1
    elif user_choice == 'scissors' and computer_pick == 'rock':
        print("You lost")
        computer_wins += 1
    else:
        print("You win")
        user_wins += 1

print("You win", user_wins, 'times' + '.')
print("Computer win", computer_wins, 'times' + '.')
print("Tie", tie, 'times' + '.')
if user_wins > computer_wins:
    print("Congratulation for you.")
else:
    print("Congratulations for computer.")
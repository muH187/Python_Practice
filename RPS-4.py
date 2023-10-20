import random

options = ['rock', 'paper', 'scissors']

user_win = 0
computer_win = 0
tie = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quite: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)

    computer_pick = options[random_number]

    print("Computer picked:", computer_pick + '.')
    print("You picked", user_input + '.')
    if user_input == computer_pick:
        print("It's tie")
        tie += 1
    elif user_input == 'rock' and computer_pick == 'scissors':
        print("You won!")
        user_win += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print("You won!")
        user_win += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print("You won!")
        user_win += 1
    else:
        print("You lost")
        computer_win += 1

print('You won', user_win, 'times')
print('Computer won', computer_win, 'times')
print('Tie', tie, 'times')
print('Goodbye')
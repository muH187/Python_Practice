import random


def check(user, computer):
    if user == computer:
        return 0
    elif user == 1 and computer == 2:
        return 1
    elif user == 2 and computer == 3:
        return 1
    elif user == 3 and computer == 1:
        return 1
    else:
        return -1


computer = random.randint(1,3)
user = input("Type 1 for Snake, 2 for Water, 3 for Gun: ")

score = check(user, computer)

print("You picked", user)
print("Computer picked", computer)

if score == 0:
    print("It's draw")
elif score == 1:
    print("You Won")
else:
    print("Computer Won")

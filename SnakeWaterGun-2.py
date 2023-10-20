import random

def check(user,computer):
    if computer == user:
        return 0
    if computer == 0 and user == 1:
        return -1
    if computer == 1 and user == 2:
        return -1
    if computer == 2 and user == 1:
        return -1
    return 1

computer = random.randint(0,2)
user = input("0 for Snake, 1 for Water, 2 for Gun:\n")

score = check(user,computer)

print('User:', user)
print('Computer:', computer)

if score == 0:
    print("It's draw")
elif score == -1:
    print("You lost")
else:
    print("You win")
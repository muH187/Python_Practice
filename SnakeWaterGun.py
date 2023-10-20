import random

while True:
    def check(computer, user):
        if computer == user:
            return 0
        if computer == 0 and user == 1:
            return -1
        if computer == 1 and user == 2:
            return -1
        if computer == 2 and user == 0:
            return -1
        return 1



    computer = random.randint(0,2)
    user = int(input("0 For Snake, 1 For Water, 2 For Gun:\n"))

    score = check(computer, user)

    print(f"You {user}")
    print(f"Computer {computer}")

    if score == 0:
        print("It's Draw")
    elif score == -1:
        print("You Lose")
    else:
        print("You Win")
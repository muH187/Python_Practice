name = input("Enter your name please: ")
print(f"Welcome to {name} in this Adventure Game")

answer = input("You are on a dirt road, it has come to an end and you can go to left or right, which way you would like to go (left/right)? ").lower()

if answer == 'left':
    answer = input("You come to a river, you can walk around it or swim accross? Type (walk/swim): ")
    if answer == 'swim':
        print("You swam accross river and were eaten by an alligator.")
    elif answer == 'walk':
        print("You walk for many miles, ran out of water and you lose the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == 'right':
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back): ").lower()
    if answer == 'back':
        print("You go back to castle and you asleep.")
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger, do you want to talk to them. (yes/no): ")
        if answer == 'yes':
            print("The stranger became happy and he gave you so many golds and now you became rich and you win the game.")
        elif answer == 'no':
            print("You didn't talk to stranger and he became angry and you lose the game.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")
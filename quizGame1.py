print("Welcome to our Quiz Game")

total_chances = 10

while True:
    while total_chances != 0:
        total_chances -= 1
        question1 = input("CPU stand for: ")
        if question1.lower() == 'central processing unit':
            print("Correct")
        else:
            print("Incorrect")
            print("Your remaining chances:", total_chances)

        question1 = input("GPU stand for: ")
        if question1.lower() == 'graphic processing unit':
            print("Correct")
        else:
            print("Incorrect")
            print("Your remaining chances:", total_chances)

        question1 = input("USA stand for: ")
        if question1.lower() == 'united states of america':
            print("Correct")
        else:
            print("Incorrect")
            print("Your remaining chances:", total_chances)d

        question1 = input("UK stand for: ")
        if question1.lower() == 'united kingdom':
            print("Correct")
        else:
            print("Incorrect")

        question1 = input("PC stand for: ")
        if question1.lower() == 'personal computer':
            print("Correct")
        else:
            print("Incorrect")
            break



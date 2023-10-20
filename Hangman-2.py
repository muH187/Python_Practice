import random

words = ["PAKISTAN", "INDIA", "AMERICA", "JAPAN", "CHINA"]

word = random.choice(words)
total_chances = 7
guessed_word = "-"*len(word)

print("The length of word is", len(word))

while total_chances != 0:

    print(guessed_word)
    letter = input("Guess a letter: ").upper()

    if letter in word:
        for char in range(len(word)):
            if word[char] == letter:
                guessed_word = guessed_word[:char] + letter + guessed_word[char+1:]

        if guessed_word == word:
            print("Congratulations You Won")
            break

    else:
        total_chances -= 1
        print("Incorrect Guess")
        print(f"Your remaining chances: {total_chances}")

else:
    print("Game Over")
    print("You lost")
    print("Your chances are exhausted")
print("The word is", word)

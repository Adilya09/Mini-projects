name = input("Enter your name: ")
print("Good luck, {}".format(name))

word_list = ["computer", "kitchen", "netflix", "tea", "notebook", "city", "window",
             "cozy", "wallpaper", "uncle", "fashion", "shopping", "mexican", "office"]


import random

word = random.choice(word_list)
print("The word has", len(word), "letters")

print("Guess the characters")
guesses = " "
turns = 12

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You win!")

        print("The word is: ", word)
        break

    print()
    guess = input("guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, "more guesses")
    if turns == 0:
        print("You loose")










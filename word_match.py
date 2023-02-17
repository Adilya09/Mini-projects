import random

def get_a_clue():
    clues = ["p-ct-r-", "c-ic-en", "-ti-k", "s-ui--el", "-or-ing", "b-r-hda-", "r--g", "s-ee-"]
    index = random.randint(0, len(clues)-1)
    clue = clues[index]
    return clue

def check_word_match(clue, guess):
    if len(clue) != len(guess):
        return False
    for i in range(len(clue)):
        if clue[i] != "-" and clue[i] != guess[i]:
            return False
    return True

word_clue = get_a_clue()
print("Your word clue:", word_clue)
answer = input("What would be the word: ")

is_matched = check_word_match(word_clue, answer)



if is_matched is True:
    print("Congratulations! You win!")
else:
    print("Oops! You lost.")

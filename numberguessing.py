import math
import random

# Taking inputs
lower = int(input("Enter the lower bound of the range: "))
upper = int(input("Enter the upper bound of the range: "))

# Generating the random number
x = random.randint(lower, upper)

# Calculating the number of guesses
min_guessing = round(math.log((upper - lower + 1), 2))
print("\n\tYou have {} chances to guess!".format(min_guessing))

# Initialiasing the number of guesses
count = 0
while count < min_guessing:
    count += 1
    guess = int(input("\nEnter your guess: "))

    # Condition testing
    if guess > x:
        print("Try again! You guessed too high.")
    elif guess < x:
        print("Try again! You guessed too small.")
    elif guess == x:
        print("Congratulations! You did it in {} try.".format(count))
        break
# if guessing more than required
else:
    print("You are out of chances. \nBetter luck next time! \nThe number is {}".format(x))




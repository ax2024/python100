# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from art import logo
import random
def showLogo():
    print(logo)

# 1 show log and game description
# 2 input level
# 3 generate a number between 1 and 100
# 4 loop for 1)take user input, 2)check if it is, 3)hint low or high, 4)count check

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(logo)
    print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
    target = random.randint(1, 100)
    print(target)
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    count_limit = 5
    count = 0
    if level == "easy":
        count_limit = 10
    user_win = False
    while not user_win and count < count_limit:
        print(f"You have {count_limit - count} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if guess == target:
            user_win = True
        elif guess > target:
            print("Too high.")
        else:
            print("Too low.")
        count += 1

    if user_win:
        print(f"You got it in {count} time(s)! The answer was {target}.")
    else:
        print("You've run out of guesses, you lose.")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

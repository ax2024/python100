# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from art import logo, vs
from game_data import data
import os
import random


def get_item():
    return random.choice(data)


def get_another_item(except_data):
    except_index = -1
    if except_data in data:
        except_index = data.index(except_data)
    is_got_another_data = False
    new_index = 0
    while not is_got_another_data:
        new_index = random.randint(0, len(data))
        if new_index != except_index:
            is_got_another_data = True
    return data[new_index]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_score = 0

    # generate first 2(different) items
    index_compare_a = random.randint(0, len(data))
    compare_a = data[index_compare_a]

    print(logo)

    is_game_end = False
    while not is_game_end:
        index_against_b = random.randint(0, len(data))
        while index_against_b == index_compare_a:
            index_against_b = random.randint(0, len(data))
        against_b = data[index_against_b]

        # print first item
        print(f'Compare A: {compare_a["name"]}, {compare_a["description"]}, from {compare_a["country"]}')
        print(vs)
        print(f'Against B: {against_b["name"]}, {against_b["description"]}, from {against_b["country"]}')

        # get user input
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if compare_a["follower_count"] > against_b["follower_count"] and user_choice == "a":
            os.system('clear')
            print(logo)
            print(f"You're right! Current score: {user_score}.")
            index_compare_a = index_against_b
            compare_a = against_b
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {user_score}")
            is_game_end = True

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

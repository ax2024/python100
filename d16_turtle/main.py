# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# from turtle import Turtle, Screen
from prettytable import PrettyTable

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # eric = Turtle()
    # eric.shape("turtle")
    # eric.color("green")
    # eric.forward(100)
    #
    # my_screen = Screen()
    # print(my_screen.canvheight)
    # my_screen.exitonclick()
    table1 = PrettyTable()
    table1.field_names = ["Pokemon Name", "Type"]
    table1.add_rows([
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ])
    print(table1)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

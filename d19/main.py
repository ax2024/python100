from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
turtle_start_y = 100
for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    # t.speed("fast")
    t.goto(x=-230, y=turtle_start_y)
    turtle_start_y -= 40
    turtles.append(t)


def is_any_turtle_win():
    for t in turtles:
        # print(t.pos())
        if t.pos()[0] >= 230:
            return True
    return False


while not is_any_turtle_win():
    t = random.choice(turtles)
    t.fd(2)

for t in turtles:
    if t.pos()[0] >= 230:
        print(f"winner:{t.pencolor()}")
        if t.pencolor() == user_bet:
            print("You win!")
        else:
            print("You lose!")


screen.exitonclick()

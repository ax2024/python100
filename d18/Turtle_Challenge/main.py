from turtle import Turtle, Screen
import random
import colorgram


def dash_line(turtle, distance, step=5):
    walked = 0
    while walked < distance:
        turtle.pendown()
        turtle.fd(step)
        turtle.penup()
        turtle.fd(step)
        walked += (step * 2)


def draw_shapes1(turtle, line_length=100):
    for n in range(3, 10):
        for i in range(n):
            turtle.fd(line_length)
            turtle.right(360 / n)


def random_walk(turtle, steps=100):
    actions = [0, 90, 180, 270]
    turtle.pensize(5)
    turtle.speed(8)
    for _ in range(steps):
        current_action = random.choice(actions)
        turtle.right(current_action)

        turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.fd(20)


def draw_spirograph(turtle, degree):
    turtle.speed("fastest")
    for _ in range(0, 360, degree):
        turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.left(degree)
        turtle.circle(100)


def draw_hirst(turtle, row, col, image="image.jpg"):
    colors = colorgram.extract(image, 30)
    for _ in range(row):
        for _ in range(col):
            turtle.pendown()
            turtle.color(random.choice(colors).rgb)
            turtle.filling()
            turtle.dot(20)
            turtle.penup()
            turtle.fd(40)
        turtle.left(90)
        turtle.fd(40)
        turtle.left(90)
        turtle.fd(400)
        turtle.right(180)

if __name__ == '__main__':
    eric_the_turtle = Turtle()
    eric_the_turtle.shape("turtle")
    eric_the_turtle.color("green", "red")


    screen = Screen()
    screen.colormode(255)


    # SQUARE
    # for _ in range(4):
    #     dash_line(eric_the_turtle, 100)
    #     eric_the_turtle.right(90)
    #
    # MANY SHAPES
    # draw_shapes1(eric_the_turtle)

    # RANDOM WALK
    # random_walk(eric_the_turtle, 1000)

    # SPIROGRAPH
    # draw_spirograph(eric_the_turtle, 2)
    # eric_the_turtle.fd(200)
    # draw_spirograph(eric_the_turtle, 2)
    # eric_the_turtle.right(120)
    # eric_the_turtle.fd(200)
    # draw_spirograph(eric_the_turtle, 2)

    # HIRST PAINTING
    draw_hirst(eric_the_turtle, 10, 10)



    screen.exitonclick()

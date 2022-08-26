from turtle import  Turtle
import random

MOVE_DISTANCE = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")

        self.reset()

    def reset(self):
        self.setpos(0, 0)
        random_direction = random.randint(0, 360)
        # random_direction = 280
        self.setheading(random_direction)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def bounce_wall(self):
        self.setheading(360 - self.heading())

    def bounce_paddle(self):
        new_heading = 180 - self.heading()
        if self.heading() > 180:
            new_heading += 360
        self.setheading(new_heading)


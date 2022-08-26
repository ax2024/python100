from turtle import Turtle
START_POINT = (0, -280)
MOVE_DISTANCE = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.setheading(90)

        self.reset()

    def reset(self):
        self.setpos(START_POINT)

    def up(self):
        self.fd(MOVE_DISTANCE)

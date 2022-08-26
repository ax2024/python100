from turtle import Turtle

SEG_SIZE = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, size):
        self.size = size
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(self.size):
            seg = self.new_seg()
            seg.goto(i * -SEG_SIZE, 0)
            self.segments.append(seg)

    def new_seg(self):
        seg = Turtle()
        seg.shape("square")
        seg.color("white")
        seg.penup()
        return seg

    def eat(self):
        seg = self.new_seg()
        last_one_pos = self.segments[-1].pos()
        seg.goto(last_one_pos)
        self.segments.append(seg)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].setpos(self.segments[i - 1].pos())
        self.segments[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

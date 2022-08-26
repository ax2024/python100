from turtle import Turtle
PADDLE_LEN = 5
MOVE_DISTANCE = 20
SEG_SIZE = 20
UP = 90
DOWN = 270


def create_paddle(x_pos):
    seg = Turtle()
    seg.shape("square")
    seg.color("white")
    seg.shapesize(stretch_wid=5, stretch_len=1)
    seg.penup()
    seg.setpos(x_pos, 0)
    return seg


class Paddle(Turtle):
    def __init__(self, xpos, board_height):
        super().__init__()
        self.board_height = board_height
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(xpos, 0)

    def up(self):
        if self.ycor() > (self.board_height / 2 - 30):
            return
        self.setpos(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        if self.ycor() < (-self.board_height / 2 + 30):
            return
        self.setpos(self.xcor(), self.ycor() - MOVE_DISTANCE)

    # def __init__(self, board_x, board_y):
    #     self.board_x = board_x
    #     self.board_y = board_y
    #     self.paddle_1 = create_paddle(- self.board_x / 2 + 10)
    #     self.paddle_2 = create_paddle(self.board_x / 2 - 20)
    #
    # def paddle_1_up(self):
    #     self.up(self.paddle_1)
    #
    # def paddle_1_down(self):
    #     self.down(self.paddle_1)
    #
    # def paddle_2_up(self):
    #     self.up(self.paddle_2)
    #
    # def paddle_2_down(self):
    #     self.down(self.paddle_2)
    #
    # def up(self, paddle):
    #     if paddle.ycor() > (self.board_y / 2 - 30):
    #         return
    #     paddle.setpos(paddle.xcor(), paddle.ycor() + MOVE_DISTANCE)
    #
    # def down(self, paddle):
    #     if paddle.ycor() < (-self.board_y / 2 + 30):
    #         return
    #     paddle.setpos(paddle.xcor(), paddle.ycor() - MOVE_DISTANCE)
    #
    # def is_collision_with(self, ball):
    #     if self.paddle_1.distance(ball) < 30:
    #         return True
    #     if self.paddle_2.distance(ball) < 30:
    #         return True
    #     return False

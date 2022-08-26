from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle1 = 0
        self.paddle2 = 0
        self.shape()
        self.goto(0, 250)
        self.hideturtle()
        self.color("white")
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"{self.paddle1} : {self.paddle2}", False, align=ALIGNMENT, font=FONT)

    def add_score_paddle_1(self):
        self.paddle1 += 1
        self.refresh()

    def add_score_paddle_2(self):
        self.paddle2 += 1
        self.refresh()

    def is_game_over(self):
        if self.paddle1 >= 3:
            self.game_over(1)
            return True
        elif self.paddle2 >= 3:
            self.game_over(2)
            return True
        else:
            return False

    def game_over(self, paddle_index):
        self.goto(0, 0)
        self.write(f"Paddle {paddle_index} win!", False, align=ALIGNMENT, font=FONT)

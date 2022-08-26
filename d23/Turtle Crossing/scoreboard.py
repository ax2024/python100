from turtle import Turtle
ALIGNMENT = "center"
POSITION = (-300, 250)
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape()
        self.goto(POSITION)
        self.hideturtle()
        self.color("white")

        self.level = 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level {self.level}", False, align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, align=ALIGNMENT, font=FONT)

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Bong Game")
screen.tracer(0)

paddle1 = Paddle(-380, 600)
paddle2 = Paddle(380, 600)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

game_is_on = True
set_is_on = True
while game_is_on:
    ball.reset()
    set_is_on = True
    while set_is_on:
        screen.update()
        time.sleep(0.1)

        ball.move()

        # detect wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_wall()

        # detect paddle
        if paddle1.distance(ball) < 20 or paddle2.distance(ball) < 20:
            ball.bounce_paddle()

        # detect miss
        if ball.xcor() > 400:
            print("paddle 2 missed")
            scoreboard.add_score_paddle_1()
            set_is_on = False
        elif ball.xcor() < -400:
            print("paddle 1 missed")
            scoreboard.add_score_paddle_2()
            set_is_on = False

    if scoreboard.is_game_over():
        game_is_on = False


screen.exitonclick()

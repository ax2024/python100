import time
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

car_manager = CarManager()

scoreboard = Scoreboard()

player = Player()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.car_moves()

    if player.ycor() > 280:
        player.reset()
        scoreboard.level_up()
        car_manager.level_up()

    if car_manager.is_crash(player):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()

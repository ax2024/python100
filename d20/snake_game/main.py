import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(3)
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.add_score()
        snake.eat()

    # Detect wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect self
    for seg in snake.segments[3:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()
            break

# def is_turtle_in_screen(turtle, user_screen):
#     screen_size = user_screen.screensize()
#     screen_x_max = screen_size[0] / 2
#     screen_y_max = screen_size[1] / 2
#     turtle_pos = turtle.pos()
#     turtle_pos_x = turtle_pos[0]
#     turtle_pos_y = turtle_pos[1]
#     if turtle_pos_x > screen_x_max or turtle_pos_x < -screen_x_max:
#         return False
#     if turtle_pos_y > screen_y_max or turtle_pos_y < -screen_y_max:
#         return False
#     return True
#
#
# while is_turtle_in_screen(turtle_array[0], screen):
#     turtle_array_len = len(turtle_array)
#     for i in range(turtle_array_len - 1):
#         turtle_array[turtle_array_len - 1 - i].setpos(turtle_array[turtle_array_len - 2 - i].pos())
#     turtle_array[0].fd(20)

screen.exitonclick()

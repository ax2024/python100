from turtle import Turtle
import random

START_CAR_AMOUNT = 30
START_CAR_MOVE_DISTANCE = 5
DELTA_CAR_AMOUNT = 10
DELTA_CAR_MOVE_DISTANCE = 5

colors = ["white", "red", "yellow", "blue", "green"]


class CarManager:
    def __init__(self):
        self.car_amount = START_CAR_AMOUNT
        self.car_move_distance = START_CAR_MOVE_DISTANCE
        self.cars = []
        self.generate_cars(self.car_amount)

    def generate_cars(self, amount):
        for _ in range(amount):
            self.generate_one_car()

    def generate_one_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        random_x = random.randint(200, 1000)
        random_y = random.randint(-290, 290)
        new_car.setpos(random_x, random_y)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color("red")
        self.cars.append(new_car)

    def car_moves(self):
        for car in self.cars:
            if car.xcor() < -400:
                random_x = random.randint(300, 1100)
                random_y = random.randint(-290, 290)
                car.setpos(random_x, random_y)
            else:
                car.setpos(car.xcor() - self.car_move_distance, car.ycor())

    def is_crash(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False

    def level_up(self):
        self.car_amount += DELTA_CAR_AMOUNT
        self.generate_cars(DELTA_CAR_AMOUNT)
        self.car_move_distance += DELTA_CAR_MOVE_DISTANCE


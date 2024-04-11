from turtle import Turtle
import random

COLORS: list[str] = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE: int = 5
MOVE_INCREMENT: int = 3


class CarManager(Turtle):

    def __init__(self):
        self.all_cars: list[Turtle] = []
        self.car_speed: int = STARTING_MOVE_DISTANCE

    def create_car(self) -> None:
        random_chance: int = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y: float = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self) -> None:
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self) -> None:
        self.car_speed += MOVE_INCREMENT

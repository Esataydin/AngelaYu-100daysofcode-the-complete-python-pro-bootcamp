from turtle import Turtle
import random

distance: int = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.goto(0, -60)
        self.color('white')
        self.x_move: int = 10
        self.y_move: int = -10
        self.move_speed: float = 0.05
        self.start_move()

    def start_move(self) -> None:
        self.x_move: int = random.randint(5, 20)
        self.y_move = -100/self.x_move

    def move(self) -> None:
        new_x: float = self.xcor() + self.x_move
        new_y: float = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self) -> None:
        self.y_move *= -1

    def bounce_x(self) -> None:
        self.x_move *= -1

    def reset_position(self) -> None:
        self.start_move()
        self.goto(0, -60)
        self.move_speed = 0.05
        self.bounce_x()

from turtle import Turtle
distance = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.goto(0, 0)
        self.color('white')
        self.x_move: float = 10
        self.y_move: float = 10
        self.move_speed: float = 0.05

    def move(self) -> None:
        new_x: float = self.xcor() + self.x_move
        new_y: float = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self) -> None:
        self.y_move *= -1

    def bounce_x(self) -> None:
        self.x_move *= -1
        # Speeds up ball everytime it hits a paddle
        self.move_speed *= 0.9

    def reset_position(self) -> None:
        self.goto(0, 0)
        self.move_speed: float = 0.1
        self.bounce_x()

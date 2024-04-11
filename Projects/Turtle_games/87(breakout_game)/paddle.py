from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.color('white')

    def go_right(self) -> None:
        new_x: float = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self) -> None:
        new_x: float = self.xcor() - 20
        self.goto(new_x, self.ycor())

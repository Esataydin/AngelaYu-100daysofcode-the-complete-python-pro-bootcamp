from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position: tuple[float, float]):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.color('white')

    def go_up(self) -> None:
        new_y: float = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self) -> None:
        new_y: float = self.ycor() - 20
        self.goto(self.xcor(), new_y)


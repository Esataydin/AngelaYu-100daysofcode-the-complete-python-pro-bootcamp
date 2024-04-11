from turtle import Turtle


class Ship(Turtle):

    def __init__(self, position: tuple[int, int]):
        super().__init__()
        self.shape('arrow')
        self.left(90)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(position)
        self.color('white')

    def go_right(self) -> None:
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self) -> None:
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

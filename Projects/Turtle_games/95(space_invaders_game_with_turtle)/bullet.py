from turtle import Turtle


class Bullet(Turtle):

    def __init__(self, x_cor: float, y_cor: float, direction: int):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')

        self.shapesize(stretch_wid=0.8, stretch_len=0.2)
        self.goto(x_cor, y_cor)
        self.y_move = int(direction) * 10
        self.move_speed = 0.05

    def move(self) -> None:
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)





from turtle import Turtle

STARTING_POSITION: tuple[int, int] = (0, -280)
MOVE_DISTANCE: float = 10
FINISH_LINE_Y: float = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self) -> None:
        new_y: float = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def go_to_start(self) -> None:
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self) -> bool:
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


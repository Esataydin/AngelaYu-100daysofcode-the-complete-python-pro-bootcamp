import turtle
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments: list[Turtle] = []
        self.create_snake()
        self.head: Turtle = self.segments[0]
        self.head.color('brown')

    def create_snake(self) -> None:
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position: tuple[int, int]) -> None:
        square = Turtle(shape='square')
        square.color('white')
        square.penup()
        square.goto(position)
        self.segments.append(square)

    def reset_snake(self) -> None:
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head: Turtle = self.segments[0]
        self.head.color('brown')

    def extend(self) -> None:
        self.add_segment(self.segments[-1].position())


    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x: float = self.segments[seg_num - 1].xcor()
            new_y: float = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)


    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
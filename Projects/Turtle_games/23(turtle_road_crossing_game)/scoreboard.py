from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level: int = 0
        self.hideturtle()
        self.penup()
        self.clear()
        self.goto(-200, 260)
        self.write(f'Level = {self.level}', align='center', font=FONT)

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f'Level = {self.level}', align='center', font=FONT)

    def increase_level(self) -> None:
        self.level += 1

    def game_over(self) -> None:
        self.goto(0, -290)
        self.write('GAME OVER', align='center', font=("Courier", 32, "normal"))
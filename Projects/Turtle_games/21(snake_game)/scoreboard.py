from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score: int = 0
        with open('data.txt') as data:
            self.high_score: int = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(f'Score = {self.score}  High Score = {self.high_score}', align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f'Score = {self.score}  High Score = {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))

        self.score: int = 0
        self.update_scoreboard()

    def increase_score(self) -> None:
        self.score += 1
        self.update_scoreboard()

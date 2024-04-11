from turtle import Turtle, Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


turtle = Turtle()
screen = Screen()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up,'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up,'w')
screen.onkeypress(l_paddle.go_down, 's')

game_is_on = True
distance = 10
while game_is_on:
    screen.update()

    # detects collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detects collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() > -350):
        ball.bounce_x()

    # detects when paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    ball.move()

    time.sleep(ball.move_speed)
































screen.exitonclick()
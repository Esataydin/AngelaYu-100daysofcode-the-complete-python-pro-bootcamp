from turtle import Turtle, Screen
import time

from paddle import Paddle
from ball import Ball
from block_manager import BlockManager


turtle = Turtle()
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

width, height = screen.screensize()

paddle = Paddle((0, -(height - 60)))
ball = Ball()
block_manager = BlockManager((width, height))

screen.listen()
screen.onkeypress(paddle.go_right, 'd')
screen.onkeypress(paddle.go_left, 'a')


def main() -> None:
    game_is_on = True
    distance = 10
    while game_is_on:
        screen.update()
        # detects collision with block
        for blocks_row in block_manager.all_rows:
            for block in blocks_row:
                if ball.distance(block) < 30:
                    ball.bounce_y()
                    block.hideturtle()
                    blocks_row.remove(block)
                    block_manager.block_num -= 1
                    break
        if block_manager.block_num == 0:
            print("Finished")
            game_is_on = False
        # detects collision with wall
        if ball.xcor() > width or ball.xcor() < -width:
            ball.bounce_x()

        # detects collision with upper wall
        if ball.ycor() > height:
            ball.bounce_y()

        # detects collision with paddle
        if (ball.distance(paddle) < 40 and ball.ycor() > -260):
            ball.bounce_y()
            ball.move_speed *= 0.9

        # detect when paddle misses
        if ball.ycor() < -height:
            ball.reset_position()

        ball.move()

        time.sleep(ball.move_speed)


if __name__ == '__main__':
    main()

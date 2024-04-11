from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Keybinds to move the snake to the direction we want
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


def main() -> None:
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detects collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detects collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

        # Detects collision wth tail
        # if head collides with any segment in the tail:
        # triggers game_over and resets snake
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset_scoreboard()
                snake.reset_snake()

    scoreboard.file.close()

    screen.exitonclick()


if __name__ == '__main__':
    main()

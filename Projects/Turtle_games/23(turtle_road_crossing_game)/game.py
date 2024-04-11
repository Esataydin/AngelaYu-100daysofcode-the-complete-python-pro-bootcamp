import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('lightgrey')

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

#Keybind to move the turtle up
screen.listen()
screen.onkeypress(player.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()

    # Detects collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detects if turtle crossed the road, if it did levels up cars speed up.
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
        car_manager.level_up()

    screen.update()

screen.exitonclick()

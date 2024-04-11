from turtle import Turtle, Screen

import time
import random

from enemy_manager import EnemyManager
from ship import Ship
from bullet import Bullet


ship_bullets: list[Bullet] = []
enemy_bullets: list[Bullet] = []


def create_ship_bullet() -> None:
    bullet = Bullet(ship.xcor(), ship.ycor(), 1)
    ship_bullets.append(bullet)


def create_enemy_bullet() -> None:
    random_enemy_ship = random.choice(random.choice(list(block_manager.all_rows.items()))[1])
    bullet = Bullet(random_enemy_ship.xcor(), random_enemy_ship.ycor(), -1)
    enemy_bullets.append(bullet)


def check_is_win() -> bool:
    for row in list(block_manager.all_rows.items()):
        if len(row[1]) == 0:
            return True
        else:
            return False


screen = Screen()

screen.setup(width=1200, height=900)
screen.bgcolor('black')
screen.title('Space Invaders')
screen.tracer(0)

width, height = screen.screensize()

ship = Ship((0, -(height - 60)))
block_manager = EnemyManager((width, height))


screen.listen()
screen.onkeypress(ship.go_right, 'd')
screen.onkeypress(ship.go_left, 'a')
# Creates our bullets, in other words we shoot
screen.onkeypress(create_ship_bullet, 's')
# Creates enemy bullets, in other words enemies shoot. It's for test.
screen.onkeypress(create_enemy_bullet, 'w')

move_speed = 0.03


def main() -> None:
    global ship
    game_is_on = True
    while game_is_on:
        if check_is_win():
            turtle = Turtle('square')
            turtle.color('white')
            turtle.hideturtle()
            turtle.write("You Won", move=False, align="center", font=("Arial", 48, "normal"))
        for bullet in ship_bullets:
            bullet.move()
            if bullet.ycor() > height:
                bullet.hideturtle()
                ship_bullets.remove(bullet)
            else:
                try:
                    for block in block_manager.all_rows[bullet.ycor()]:
                        if bullet.distance(block) < 25:
                            block.hideturtle()
                            bullet.hideturtle()
                            ship_bullets.remove(bullet)
                            block_manager.all_rows[bullet.ycor()].remove(block)
                except:
                    continue

        # It's for creating enemy bullets randomly. Disable it if you want to test on your own.
        if random.randint(0, 8) == 1:
            create_enemy_bullet()

        for bullet in enemy_bullets:
            bullet.move()
            if bullet.ycor() < -height:
                bullet.hideturtle()
                enemy_bullets.remove(bullet)
            else:
                if ship:
                    if bullet.distance(ship) < 25:
                        ship.goto(0, ship.ycor())
                        ship.write("You Lost", move=False, align="center", font=("Arial", 48, "normal"))
                        ship.hideturtle()
                        bullet.hideturtle()
                        enemy_bullets.remove(bullet)
                        screen.update()
                        time.sleep(2)
                        print("YOU LOST")
                        return

        screen.update()
        time.sleep(move_speed)


if __name__ == '__main__':
    main()

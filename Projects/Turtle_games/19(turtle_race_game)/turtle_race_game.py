from turtle import Turtle, Screen
import random


screen = Screen()
screen.bgcolor('lightgrey')
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
user_bet = screen.textinput(title='Make your bet', prompt=f'Which turtle will win the race? Enter a color: \n{colors}')
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles: list[Turtle] = []

is_race_on = False
is_going = False


# Creates turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_going = True

while is_going:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_going = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
            break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

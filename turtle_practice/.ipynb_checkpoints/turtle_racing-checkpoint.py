from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=800, height=650)
turtle_color = ["red", "blue", "green", "yellow", "orange"]
user_bet = screen.textinput(title="Turtle bet.", prompt="Enter turtle color name for race bet: ")
turtle_pos = [-250, -100, 0, 100, 250]
all_turtle = []

for turtle in range(0, 5):
    jerry = Turtle()
    jerry.speed(0)
    jerry.color(turtle_color[turtle])
    jerry.shapesize(2)
    jerry.shape("turtle")
    jerry.penup()
    jerry.goto(-350, turtle_pos[turtle])
    all_turtle.append(jerry)


race_start = False

if user_bet:
    race_start = True

while race_start:
    for turtle in all_turtle:
        if turtle.xcor() > 380:
            race_start = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You win, {user_bet}")
            else:
                print(f"You lost, Winner is {winner} turtle")
        rand = randint(1, 10)
        turtle.forward(rand)


screen.exitonclick()

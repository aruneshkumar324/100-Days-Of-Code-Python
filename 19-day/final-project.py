from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
user = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red","orange", "yellow","green", "blue","purple"]
turtle_position = [-150, -100, -50, 50, 100, 150]

is_race_on = False
all_turtles = []

for index in range(0, 6):
    tom = Turtle(shape="turtle")
    tom.speed(0)
    tom.penup()
    tom.color(colors[index])
    tom.goto(x=-280, y=turtle_position[index])
    all_turtles.append(tom)

if user:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user:
                print(f"You won race, {winner}")
            else:
                print(f"You lost race, {winner}")
        rand_num = randint(0, 10)
        turtle.forward(rand_num)




screen.exitonclick()
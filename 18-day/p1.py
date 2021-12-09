import turtle
from turtle import Turtle, Screen

from random import choice

timmy = Turtle()

timmy.shape("turtle")
timmy.shapesize(2)
timmy.color("red", "blue")

# timmy.speed(1)

colors = ["light salmon", "red", "purple", "plum", "pink", "yellow", "cornflower blue"]

# TURTLE MOVEING
def turtule_steps(a, b, c, d):
    timmy.color(choice(colors))
    timmy.forward(a)
    timmy.right(90)
    timmy.forward(b)
    timmy.right(90)
    timmy.forward(c)
    timmy.right(90)
    timmy.forward(d)

steps = 0
a = 20
b = 25
c = 30
d = 35

while steps < 50:
    a += 5
    b += 5
    c += 5
    d += 5
    turtule_steps(a, b, c, d)
    steps += 1





screen = Screen()

# screen.bgpic("demo.gif")
# EXIT FROM SCREEN
screen.exitonclick()


import random
# from turtle import Turtle, Screen

import turtle as t

tom = t.Turtle()
t.colormode(255)


tom.speed(0)
tom.pensize(10)

directions = [0, 90, 180, 270]
# colors = ["light salmon", "red", "purple", "plum", "pink", "yellow", "cornflower blue"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

# print(random_color())

for _ in range(200):
    # tom.color(choice(colors))
    tom.color(random_color())
    tom.forward(30)
    tom.setheading(random.choice(directions))







#   EXIT
screen = t.Screen()
screen.exitonclick()
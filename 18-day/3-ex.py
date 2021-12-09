from turtle import Turtle, Screen

import random

tom = Turtle()

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tom.forward(5)
#         tom.right(angle)
#
# draw_shape(5)

colors = ["light salmon", "red", "purple", "plum", "pink", "yellow", "cornflower blue"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tom.forward(100)
        tom.right(angle)


for shape_side in range(3, 11):
    tom.color(random.choice(colors))
    draw_shape(shape_side)




























#EXIT
Screen().exitonclick()
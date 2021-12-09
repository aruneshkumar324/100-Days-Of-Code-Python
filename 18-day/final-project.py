# import colorgram
# colors = colorgram.extract("hirst.jpg", 30)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r, g, b))
# print(color_list)

import turtle as t
from random import choice

color_list = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

t.colormode(255)
tom = t.Turtle()
t.speed(0)
tom.up()
tom.setpos(-300, -300)
tom.hideturtle()

y = -300

def steps():
    for _ in range(0, 10):
        color = choice(color_list)
        tom.dot(20, color)
        tom.forward(50)


for _ in range(0, 10):
    steps()
    y = y + 50
    tom.setpos(-300, y)


t.Screen().exitonclick()



























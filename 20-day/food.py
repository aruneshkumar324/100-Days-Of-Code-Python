from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.speed(0)
        self.refresh()

    def refresh(self):
        x_pos = randint(-280, 280)
        y_pos = randint(-280, 280)
        self.goto(x_pos, y_pos)


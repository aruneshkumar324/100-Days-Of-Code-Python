from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

obj_position = [(0, 0), (-20, 0), (-40, 0)]

all_objects = []

for pos in obj_position:
    obj = Turtle("square")
    obj.color("white")
    obj.penup()
    obj.goto(pos)
    all_objects.append(obj)


game_start = True

while game_start:
    screen.update()
    time.sleep(1)
    for obj in range(len(all_objects)-1, 0, -1):
        x_pos = all_objects[obj - 1].xcor()
        y_pos = all_objects[obj - 1].ycor()
        all_objects[obj].goto(x_pos, y_pos)
    all_objects[0].forward(10)



screen.exitonclick()


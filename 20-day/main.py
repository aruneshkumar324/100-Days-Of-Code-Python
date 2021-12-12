from turtle import Turtle, Screen

screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)


turtle_pos = [(0, 0), (-20, 0), (-40, 0)]


for turtle in turtle_pos:
    tom = Turtle("square")
    tom.color("white")
    tom.goto(turtle)
    print(tom.position())







































screen.exitonclick()
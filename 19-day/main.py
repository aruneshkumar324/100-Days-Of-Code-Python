from turtle import Turtle, Screen

tom = Turtle()

screen = Screen()

screen.listen()

def fw():
    tom.forward(20)

def bk():
    tom.backward(20)

def cl():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

def turn_left():
    new_heading = tom.heading() + 10
    tom.setheading(new_heading)

def turn_right():
    tom.setheading(tom.heading() - 10)

screen.onkey(fw, "w")

screen.onkey(bk, "s")

screen.onkey(cl, "c")

screen.onkey(turn_right, "d")

screen.onkey(turn_left, "a")

































screen.exitonclick()


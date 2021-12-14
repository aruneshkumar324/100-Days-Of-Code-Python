from turtle import Turtle, Screen

screen = Screen()

screen.bgcolor("black")

tom = Turtle()

tom.penup()

tom.color("white")

tom.setposition(0, 280)



tom.write(arg="Hello", font=['Arial', 18])


tom.hideturtle()










screen.exitonclick()



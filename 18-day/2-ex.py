from turtle import Turtle, Screen

tom = Turtle()

tom.speed(1)

# 1 METHOD
# for _ in range(15):
#     tom.forward(10)
#     tom.color("white")
#     tom.forward(10)
#     tom.color("black")

for _ in range(15):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()



screen = Screen()
screen.exitonclick()
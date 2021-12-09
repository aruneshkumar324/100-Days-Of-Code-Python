from turtle import Turtle, Screen

tom = Turtle()

#   TRIANGLE
def triangle():
    for _ in range(3):
        tom.forward(100)
        tom.left(120)
# triangle()

# SQUARE
def square():
    for _ in range(4):
        tom.forward(100)
        tom.left(90)
# square()

# CIRCLE
def circle():
    tom.circle(100)
# circle()

#   RECTANGLE
def rectangle():
    for _ in range(2):
        tom.forward(200)
        tom.left(90)
        tom.forward(100)
        tom.left(90)
# rectangle()


# PENTAGON
def pentagon():
    for _ in range(5):
        tom.forward(100)
        tom.left(72)
pentagon()

# HEXAGON
def hexagon():
    for _ in range(6):
        tom.forward(100)
        tom.left(60)
# hexagon()












# EXIT
Screen().exitonclick()
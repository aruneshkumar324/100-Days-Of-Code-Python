import turtle as t
import random

tom = t.Turtle()
t.colormode(255)

tom.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return  rgb


#    MY SOLUTION
for _ in range(50):
    tom.color(random_color())
    tom.circle(100)
    tom.right(8)


# def draw_circle(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tom.color(random_color())
#         tom.circle(100)
#         tom.setheading(tom.heading() + size_of_gap)
#
# draw_circle(5)


#   EXIT
t.Screen().exitonclick()


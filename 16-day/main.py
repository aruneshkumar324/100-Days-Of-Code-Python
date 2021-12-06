# import testing
# print(testing.firstName)

'''
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.shapesize(2,2,2)

timmy.color("red","blue")

timmy.forward(250)

timmy.speed("slowest")

timmy.pencolor("green")

timmy.fillcolor("orange")

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvheight)

my_screen.exitonclick()
'''

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# STYLE
table.align = "l"

print(table)


























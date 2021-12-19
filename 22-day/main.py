from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

# PADDLE SETUP
paddle = Turtle("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(380, 0)

def go_up():
    new_position = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_position)

def go_down():
    new_position = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_position)

screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()

#   EXIT
screen.exitonclick()

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

# PADDLE SETUP
l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))


screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


# BALL
ball = Ball()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


#   EXIT
screen.exitonclick()

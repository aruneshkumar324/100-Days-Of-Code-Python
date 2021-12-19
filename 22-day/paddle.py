from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(paddle_pos)


    def go_up(self):
        new_position = self.ycor() + 20
        self.goto(self.xcor(), new_position)

    def go_down(self):
        new_position = self.ycor() - 20
        self.goto(self.xcor(), new_position)
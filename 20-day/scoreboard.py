from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


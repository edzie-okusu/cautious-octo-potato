from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """docstring for Scoreboard"""

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.lives = 10
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 260)
        self.write(arg=f" Lives : {self.lives} Score : {self.score}", move=False, align="left", font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def reduce_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f" Game Over", align="center", font=FONT)

from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1

        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 250)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level = {self.score}", align="left", font=FONT)

    def check_score(self):
        self.score += 1
        self.display_score()

    def game_end(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
        self.goto(0, -30)
        self.write("RIGHT CLICK TO CLOSE", align="center", font=FONT)

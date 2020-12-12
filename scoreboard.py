from turtle import Turtle

ALIGN = 'center'
FONT = "Arial", 20, "normal"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.get_score()

    def add_r_score(self):
        self.clear()
        self.r_score += 1
        self.get_score()

    def add_l_score(self):
        self.clear()
        self.l_score += 1
        self.get_score()

    def get_score(self):
        self.goto(-100, 250)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 250)
        self.write(self.r_score, align=ALIGN, font=FONT)
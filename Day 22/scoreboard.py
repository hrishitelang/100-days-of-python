from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def lpoint(self):
        self.l_score += 1
        self.updatescore()

    def rpoint(self):
        self.r_score += 1
        self.updatescore()
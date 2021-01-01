from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("gray")
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font= FONT)

    def diditeat(self):
        self.score += 1
        self.clear()
        self.update_score()

    def printgameover(self):
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
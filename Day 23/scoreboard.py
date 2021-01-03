from turtle import Turtle
FONT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.penup()
        self.goto(-280, 260)
        self.displayscore()

    def levelup(self):
        self.level += 1
        self.clear()
        self.displayscore()

    def displayscore(self):
        self.write(f"Level {self.level}", align="left", font=FONT)

    def printgameover(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=('Courier', 15, 'normal'))

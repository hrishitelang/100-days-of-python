from turtle import Turtle

START_POSITION = 0, -270
END_POSITION = 0, 260
MOVE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.lt(90)
        self.gotostart()

    def up(self):
        self.fd(MOVE)

    def gotostart(self):
        self.goto(START_POSITION)

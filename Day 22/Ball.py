from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speedlimit = 0.1
        self.xmove = 10
        self.ymove = 10
        
    def move(self):
        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)

    def collide_y(self):
        self.ymove *= -1
        self.speedlimit *= 0.9

    def collide_x(self):
        self.xmove *= -1
        self.speedlimit *= 0.9
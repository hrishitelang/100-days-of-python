from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, y)

    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)


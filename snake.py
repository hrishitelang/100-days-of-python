from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        x = 0
        for i in range(3):
            timmy = Turtle(shape="square")
            timmy.color("white")
            timmy.penup()
            timmy.setposition(x, 0)
            self.segments.append(timmy)
            x -= 20

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed(10)
turtle.colormode(255)
screen = Screen()
# color = ["red", "blue", "green", "yellow", "orange", "purple", "gray", "magenta", "tomato", "indigo"]

def random_color():
    r = int(random.randint(0, 255))
    g = int(random.randint(0, 255))
    b = int(random.randint(0, 255))
    randomcolor = (r, g, b)
    return randomcolor


def IsTurtleIn(win, timmy):
    leftbound = -win.window_width() / 2
    rightbound = win.window_width() / 2
    topbound = win.window_width() / 2
    bottombound = -win.window_width() / 2
    X = timmy.xcor()
    Y = timmy.ycor()
    if X > rightbound or X < leftbound or Y > topbound or Y < bottombound:
        return False
    else:
        return True


while IsTurtleIn(screen, timmy):
    x = random.randint(0, 3)
    timmy.pen(pensize=10)
    # timmy.pen(pensize=10, pencolor=random_color())
    timmy.color(random_color())
    if x == 1:
        timmy.right(90)
    elif x == 2:
        timmy.backward(25)
    elif x == 3:
        timmy.left(90)
    timmy.forward(25)


screen.exitonclick()

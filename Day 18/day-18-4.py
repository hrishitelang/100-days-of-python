from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed(10)
screen = Screen()
color = ["red", "blue", "green", "yellow", "orange", "purple", "gray", "magenta", "tomato", "indigo"]

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
    timmy.pen(pensize=10, pencolor=random.choice(color))
    if x == 1:
        timmy.right(90)
    elif x == 2:
        timmy.backward(25)
    else:
        timmy.left(90)
    timmy.forward(25)


screen.exitonclick()

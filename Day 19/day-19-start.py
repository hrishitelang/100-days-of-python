from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def forward():
    timmy.forward(10)


def backward():
    timmy.backward(10)


def clockwise():
    timmy.right(10)


def counterclockwise():
    timmy.left(10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counterclockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()


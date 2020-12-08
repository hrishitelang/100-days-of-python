from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('chartreuse4')

i = 0
while i < 4:
    timmy.forward(100)
    timmy.right(90)
    i += 1



screen = Screen()
screen.exitonclick()
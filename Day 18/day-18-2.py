from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('chartreuse4')

for i in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()

screen = Screen()
screen.exitonclick()


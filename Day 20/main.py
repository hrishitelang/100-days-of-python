from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

x = 0
for i in range(3):
    timmy = Turtle(shape="square")
    timmy.color("white")
    timmy.penup()
    timmy.setposition(x, 0)
    timmy.pendown()
    x -= 20


screen.exitonclick()
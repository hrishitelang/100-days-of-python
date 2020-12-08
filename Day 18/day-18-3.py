from turtle import Turtle, Screen

timmy = Turtle()

i = 3
#timmy.setposition(0,100)
for i in range(3, 10):
    for _ in range (i):
        timmy.forward(100)
        timmy.right(360/i)

screen = Screen()
screen.exitonclick()
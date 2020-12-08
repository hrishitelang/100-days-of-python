from random import choice
from turtle import Turtle, Screen, color

timmy = Turtle()

color = ['#006400', '#4682B4', '#0000FF', '#8B0000', '#FA8072', '#4B0082', '#32CD32', '#ADFF2F', '#FF0000']
#timmy.setposition(0,100)
for i in range(3, 10):
    timmy.color(choice(color))
    for _ in range (i):
        timmy.forward(100)
        timmy.right(360/i)

screen = Screen()
screen.exitonclick()
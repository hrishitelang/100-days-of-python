from turtle import Turtle, Screen
import random
import turtle

timmy = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for i in range(0, 360, 5):
    timmy.speed(0)
    timmy.color(random_color())
    timmy.setheading(i)
    timmy.circle(100)


screen = Screen()
screen.exitonclick()
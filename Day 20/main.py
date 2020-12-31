from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

# for i in range(3):
#     timmy = Turtle(shape="square")
#     timmy.color("white")
#     timmy.penup()
#     timmy.setposition(x, 0)
#     segments.append(timmy)
#     x -= 20

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
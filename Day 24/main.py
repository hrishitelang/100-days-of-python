from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.create_snake()
        score.diditeat()

    # Detect Collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        # game_is_on = False
        score.reset()
        snake.reset()

    # Detect collision with tail
    for x in snake.segments:
        if x == snake.head:
            pass
        elif snake.head.distance(x) < 10:
            # game_is_on = False
            score.reset()
            snake.reset()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()
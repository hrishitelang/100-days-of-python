from turtle import Turtle, Screen
from Ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
score = Scoreboard()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

ball = Ball()
x = 0
flag = True
while flag:
    ball.move()
    
    #When the ball hits the top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collide_y()

    #When the ball hits the paddle
    if ball.distance(r_paddle) < 30 and ball.xcor() > 320 or ball.distance(l_paddle) < 30 and ball.xcor() < -320:
        ball.collide_x()

    
    # When the ball goes out of bounds
    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.collide_x()
        score.lpoint()
        ball.speedlimit = 0.1

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.collide_x()
        score.rpoint()
        ball.speedlimit = 0.1

    screen.update()
    time.sleep(ball.speedlimit)

screen.exitonclick()

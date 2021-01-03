from turtle import Turtle, Screen

from Ball import Ball
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

ball = Ball()

flag = True
x = ball.move()
while flag:
    ball.move()
    
    #When the ball hits the top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collide_y()

    #When the ball hits the paddle
    if ball.distance(r_paddle) < 30 and ball.xcor() > 340 or ball.distance(l_paddle) < 30 and ball.xcor() < -340:
        ball.collide_x()
    
    # When the ball goes out of bounds
    if ball.xcor() > 400 or ball.xcor() < -400:
        flag = False
        if screen.onclick():
            ball.goto(0, 0)
        flag = True

        
    screen.update()
    time.sleep(0.1)

screen.exitonclick()

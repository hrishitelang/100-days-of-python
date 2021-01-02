from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
# tim = Turtle()
# tim.shape("square")
# tim.color("white")
# tim.shapesize(5, 1)
# tim.penup()
# tim.goto(350,0)
# screen.update()

#
# def up():
#     new_y = tim.ycor() + 10
#     tim.goto(tim.xcor(), new_y)
#
# def down():
#     new_y = tim.ycor() - 10
#     tim.goto(tim.xcor(), new_y)

# paddle = Paddle()
# paddle.go(350, 0)

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

flag = True
while flag:
    screen.tracer(1)

screen.exitonclick()
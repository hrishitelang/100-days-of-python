from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# print(user_input)
race = False

colors = ["red", "orange", "blue", "yellow", "green", "blue", "purple"]
all_turtle = []
y = 0
for i in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(i)
    turtle.penup()
    turtle.goto(x=-280, y=y - 130)
    all_turtle.append(turtle)
    y += 50

if user_input:
    race = True

while race:
    for turtle in all_turtle:
        if turtle.xcor() > 280:
            race = False
            winner = turtle.fillcolor()
            if winner == user_input:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")

        turtle.forward(random.randint(0, 10))



screen.exitonclick()

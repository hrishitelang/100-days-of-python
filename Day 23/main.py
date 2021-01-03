import random
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)
player = Player()
score = ScoreBoard()

screen.listen()
screen.onkeypress(player.up, "Up")
car = CarManager()
flag = True
while flag:
    choice = random.randint(1, 6)
    if choice == 6:
        car.create_car()
    car.move_left()

    # Detect Collision (Required Thinking)
    for j in car.all_cars:
        if j.distance(player) < 25:
            flag = False
            score.printgameover()

    # Detect whether the player has won or not
    if player.ycor() > 270:
        player.gotostart()
        score.levelup()
        car.level_up()

    time.sleep(0.1)
    screen.update()


screen.exitonclick()
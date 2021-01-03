from turtle import Turtle
import random

COLORS = ['yellow', 'gold', 'orange', 'red',
          'maroon', 'violet', 'magenta', 'purple', 'navy',
          'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green',
          'darkgreen', 'chocolate', 'brown', 'black', 'gray']
MOVE_LEFT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.speed = 5

    def create_car(self):
        new_car = Turtle("square")
        new_car.shape('square')
        new_car.shapesize(1, 2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(300, random.randint(-250, 250))
        self.all_cars.append(new_car)

    def move_left(self): #Required to check the solution
        for car in self.all_cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_LEFT

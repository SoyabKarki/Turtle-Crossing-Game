from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.cars = []
        self.move = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        # Randomly create a car
        if random.randint(0, 5) == 1:

            # Create a car of 40x20 px of a random color from COLORS
            t = Turtle("square")
            t.shapesize(stretch_len=2, stretch_wid=1)
            t.color(random.choice(COLORS))
            t.penup()

            # Assign a position for a car between -250 and 250 on the y-axis and 300 on the x-axis
            y_pos = random.randint(-250, 250)
            t.goto(300, y_pos)

            self.cars.append(t)

    def move_car(self):
        for cars in self.cars:
            cars.back(self.move)

    def level_up(self):
        self.move += MOVE_INCREMENT

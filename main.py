import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.up, key="Up")
screen.onkey(fun=player.down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()

    # Detect car collision
    for a_car in car.cars:
        if player.distance(a_car) <= 20:
            game_is_on = False
            score.game_end()

    # Check if user has crossed level
    if player.is_at_finish_line():
        player.reset_position()
        car.level_up()
        score.check_score()

    car.move_car()

screen.exitonclick()

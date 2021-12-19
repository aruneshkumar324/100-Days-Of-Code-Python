import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# PLAYER
player = Player()
screen.onkey(player.go_up, "Up")

# CAR
car = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    # DETECT ANY CAR TOUCH TURTLE
    for obj in car.all_cars:
        if obj.distance(player) < 20:
            game_is_on = False

    # MISSION COMPLETE
    if player.finish_task():
        player.go_to_start()


screen.exitonclick()


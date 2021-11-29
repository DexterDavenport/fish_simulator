from game.point import Point
from game.action import Action
from game.audio_service import AudioService
from game.score import Score
import random

audio_service = AudioService()

class Handle_Off_Screen_Action(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):

        food = cast["food"][0]
        fish = cast["fish"][0]
        scores = cast["score"]

        if food.get_position().get_y() >= 590:
            x = random.randint(0,790)
            s = random.randint(2,6)
            food.set_position(Point(x, 0))
            food.set_velocity(Point(0, s))

        if fish.get_position().get_x() <= 5:
            y = fish.get_position().get_y()
            fish.set_position(Point(6, y))

        if fish.get_position().get_x() >= 685:
            y = fish.get_position().get_y()
            fish.set_position(Point(684, y))

        if fish.get_position().get_y() <= 2:
            x = fish.get_position().get_x()
            fish.set_position(Point(x, 3))

        if fish.get_position().get_y() >= 551:
            fish.set_position(Point(345, 40))

            scores.pop(0)



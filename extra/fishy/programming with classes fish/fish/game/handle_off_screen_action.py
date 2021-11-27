from game.point import Point
from game import constants
from game.action import Action
from game.audio_service import AudioService
import random


audio_service = AudioService()


class Handle_Off_Screen_Action(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service


    def execute(self, cast):

        shark = cast["shark"][0]
        shark1 = cast["shark"][1]
        shark2 = cast["shark"][2]
        fish = cast["fish"][0]

        if shark.get_position().get_x() <= 50:
            y = random.randint(0,550)
            s = random.randint(-15,-2)
            shark.set_position(Point(776, y))
            shark.set_velocity(Point(s, 0))
        if shark1.get_position().get_x() <= 50:
            y = random.randint(0,550)
            s = random.randint(-15,-2)
            shark1.set_position(Point(776, y))
            shark1.set_velocity(Point(s, 0))
        if shark2.get_position().get_x() <= 50:
            y = random.randint(0,550)
            s = random.randint(-15,-2)
            shark2.set_position(Point(776, y))
            shark2.set_velocity(Point(s, 0))


        if fish.get_position().get_x() <= 5:
            y = fish.get_position().get_y()
            fish.set_position(Point(300, y))

        if fish.get_position().get_x() >= 701:
            y = fish.get_position().get_y()
            fish.set_position(Point(650, y))

        if fish.get_position().get_y() <= 5:
            x = fish.get_position().get_x()
            fish.set_position(Point(x, 17))

        if fish.get_position().get_y() >= 551:
            x = fish.get_position().get_x()
            fish.set_position(Point(x, 549))

            

        


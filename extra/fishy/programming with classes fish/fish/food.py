from game.actor import Actor
from game.point import Point
from game import constants


class Food(Actor):
    def __init__(self):
        super().__init__()
        self.set_height(constants.FOOD_H)
        self.set_width(constants.FOOD_W)
        self.set_image(constants.IMAGE_FOOD)
        self._velocity = Point(0,-2)

    def set_position(self, position):
        self._position = position
    def get_postiton(self):
        return self._position    
    def set_velocity(self, velocity):
        self._velocity = velocity
    def get_velocity(self):
        return self._velocity
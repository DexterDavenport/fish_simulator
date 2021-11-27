from game.actor import Actor
from game.point import Point
from game import constants


class Shark(Actor):
    def __init__(self):
        super().__init__()
        self.set_height(constants.SHARK_H)
        self.set_width(constants.SHARK_WIDTH)
        self.set_image(constants.IMAGE_SHARK)
        # self._velocity = Point(-2,0)

    def set_position(self, position):
        self._position = position
    def get_postiton(self):
        return self._position    
    def set_velocity(self, velocity):
        self._velocity = velocity
    def get_velocity(self):
        return self._velocity
from game.actor import Actor
from game.point import Point
from game import constants


class Ocean(Actor):
    def __init__(self):
        super().__init__()
        self.set_height(800)
        self.set_width(600)
        self.set_image(constants.IMAGE_OCEAN)
        self._velocity = Point(0,0)

    def set_position(self, position):
        self._position = position
    def get_postiton(self):
        return self._position
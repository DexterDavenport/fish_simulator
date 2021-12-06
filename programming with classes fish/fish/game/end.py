from game.actor import Actor
from game.point import Point

class End(Actor):
    def __init__(self):
        super().__init__()
        self.set_height(1)
        self.set_width(1)
        self.set_image('')
        self._velocity = Point(0,0)

    def set_position(self, position):
        self._position = position
    def get_postiton(self):
        return self._position
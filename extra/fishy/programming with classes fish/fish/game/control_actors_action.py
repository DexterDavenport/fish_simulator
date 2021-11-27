from game import constants
from game.action import Action

class ControlActorsAction(Action):
    def __init__(self, input_service):
        self._input_service = input_service

    def execute(self, cast):
        direction = self._input_service.get_direction()
        fish = cast["fish"][0]
        fish.set_velocity(direction.scale(constants.PADDLE_SPEED))

        
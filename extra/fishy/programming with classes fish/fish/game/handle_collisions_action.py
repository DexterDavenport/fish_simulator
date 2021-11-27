from game.action import Action
from game import constants
from game.point import Point
from game.audio_service import AudioService

audio_service = AudioService()

class HandleCollisionsAction(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        fish = cast["fish"][0]
        shark = cast["shark"][0]
        shark1 = cast["shark"][1]
        shark2 = cast["shark"][2]

        scores = cast["score"]


        if self._physics_service.is_collision(shark, fish):
            # audio_service.play_sound(constants.SOUND_BOUNCE)
            fish.set_position(Point(345, 530))
            scores.pop(0)
        if self._physics_service.is_collision(shark1, fish):
            # audio_service.play_sound(constants.SOUND_BOUNCE)
            fish.set_position(Point(345, 530))
            scores.pop(0)
        if self._physics_service.is_collision(shark2, fish):
            # audio_service.play_sound(constants.SOUND_BOUNCE)
            fish.set_position(Point(345, 530))
            scores.pop(0)

        


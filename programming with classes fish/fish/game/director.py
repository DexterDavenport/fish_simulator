import os
os.environ['RAYLIB_BIN_PATH'] = '.'

from game.audio_service import AudioService
import raylibpy
from game import constants
from game.point import Point

audio_service = AudioService()

class Director:

    def __init__(self, cast, script):
        self._cast = cast
        self._script = script
        self._keep_playing = True
        
    def start_game(self, cast):
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            # TODO: Add some logic like the following to handle game over conditions
            if len(self._cast["score"]) == 0:
                audio_service.play_sound(constants.SOUND_OVER)
                end = cast["end"][0]
                end_1 =cast["end_1"][0]
                food = cast["food"][0]
                
                fish = cast["fish"][0]
                fish.set_height(0)
                fish.set_width(0)
                food.set_height(0)
                food.set_width(0)
                food._velocity = Point(0,0)

                end.set_image(constants.IMAGE_END_OCEAN)
                end_1.set_image(constants.IMAGE_DEAD)

            if raylibpy.window_should_close():
                print('ending 2')
                self._keep_playing = False


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)
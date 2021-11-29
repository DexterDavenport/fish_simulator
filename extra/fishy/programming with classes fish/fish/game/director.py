import os
os.environ['RAYLIB_BIN_PATH'] = '.'

import raylibpy
from game import constants

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
                # print('ending 1')
                # Game over
                # self._keep_playing = False
                ocean = cast["ocean"][0]
                end = cast["end"][0]
                
                
                end.set_image(constants.IMAGE_END)
                ocean.set_image(constants.IMAGE_END)

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
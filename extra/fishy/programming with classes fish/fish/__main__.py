import os

os.environ['RAYLIB_BIN_PATH'] = '.'
import random
from game import constants
from game.director import Director
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.control_actors_action import ControlActorsAction
from game.move_actors_action import MoveActorsAction 
from game.handle_off_screen_action import Handle_Off_Screen_Action
from game.handle_collisions_action import HandleCollisionsAction
from game.score import Score
from game.ocean import Ocean
from game.shark import Shark
from game.fish import Fish

def main():
    x = 1
    y = 20
    cast = {}

    # cast["ocean"] = []
    # oceans = []

    # ocean = Ocean()
    # ocean.set_position(Point(0, 0))
    # oceans.append(ocean)
    # cast["ocean"] = oceans

    cast["score"] = []
    x1 = 600
    scores = []
    for round in range(0, 3):

        score = Score()
        score.set_position(Point(x1, 550))
        x1 += 65
        scores.append(score)
        cast["score"] = scores

    cast["shark"] = []
    sharks = []

    x = 800
    s = -2
    for shark in range(0,3):
        shark = Shark()
        y = random.randint(0, 580)
        x -= 20
        s = random.randint(-10,-1)
        shark.set_position(Point(x, y))
        shark._velocity = Point(s,0)
        sharks.append(shark)
        cast["shark"] = sharks

    cast["fish"] = []
    fishs = []
    fish = Fish()
    fish.set_position(Point(345, 500))
    fishs.append(fish)
    cast["fish"] = fishs

    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    move_actors_action = MoveActorsAction()
    control_actors_action = ControlActorsAction(input_service)
    draw_actors_action = DrawActorsAction(output_service)
    handle_off_screen_action = Handle_Off_Screen_Action(physics_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action,handle_collisions_action, handle_off_screen_action]
    script["output"] = [draw_actors_action]

    output_service.open_window("Fish Simulator")
    audio_service.start_audio()
    # audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()

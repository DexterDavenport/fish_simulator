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
from game.fish import Fish
from game.food import Food

def main():
    x = 1
    y = 20
    cast = {}

    cast["score"] = []
    x1 = 735
    scores = []
    for round in range(0, 3):

        score = Score()
        score.set_position(Point(x1, 550))
        x1 -= 65
        scores.append(score)
        cast["score"] = scores

    cast["food"] = []
    foods = []

    # y = 600
    s = -2
    for food in range(0,1):
        food = Food()
        # y -= 20
        # x = random.randint(0, 800)
        s = random.randint(2,6)
        food.set_position(Point(20, 20))
        food._velocity = Point(0,s)
        foods.append(food)
        cast["food"] = foods

    cast["fish"] = []
    fishs = []
    fish = Fish()
    fish.set_position(Point(325, 40))
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
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()

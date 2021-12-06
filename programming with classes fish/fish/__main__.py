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
from game.ocean import Ocean
from game.end import End
from game.end_1 import End_1

def main():

    cast = {}

    cast["ocean"] = []
    oceans = []

    ocean = Ocean()
    ocean.set_position(Point(0, 0))
    b = random.randint(0,4)
    if b == 1:
        ocean.set_image(constants.IMAGE_OCEAN_1)
    if b == 2:
        ocean.set_image(constants.IMAGE_OCEAN_2)
    if b == 3:
        ocean.set_image(constants.IMAGE_OCEAN_3)

    oceans.append(ocean)
    cast["ocean"] = oceans

    cast["score"] = []
    x1 = 715
    scores = []
    for i in range(0, 3):
        print(i)
        score = Score()
        score.set_position(Point(x1, 550))
        x1 -= 65
        scores.append(score)
        cast["score"] = scores

    cast["food"] = []
    foods = []

    s = -2
    for food in range(0,1):
        food = Food()
        s = random.randint(2,6)
        food.set_position(Point(20, 20))
        food._velocity = Point(0,s)
        foods.append(food)
        cast["food"] = foods

    cast["fish"] = []
    fishs = []
    fish = Fish()
    fish.set_position(Point(325, 40))
    burton = random.randint(0,4)
    if burton == 3:
        fish.set_image(constants.IMAGE_BURTON)
        print('this ran')
        score = Score()
        num = (len(scores))
        x = cast["score"][num - 1]
        if x != 0:
            if x.get_position().get_x() >= 60:
                new = x.get_position().get_x()
                x = new - 65
                score.set_position(Point(x, 550))
                scores.append(score)
                # print('this ran')
                cast["score"] = scores
    if burton == 2:
        fish.set_image(constants.IMAGE_BURTON_NEMO)
        print('this ran')
        score = Score()
        num = (len(scores))
        x = cast["score"][num - 1]
        if x != 0:
            if x.get_position().get_x() >= 60:
                new = x.get_position().get_x()
                x = new - 65
                score.set_position(Point(x, 550))
                scores.append(score)
                # print('this ran')
                cast["score"] = scores
    if burton == 1:
        fish.set_image(constants.IMAGE_FISH_BLOB)

    fishs.append(fish)
    cast["fish"] = fishs

    cast['end'] = []

    ends = []
    end = End()
    end.set_position(Point(0, 0))
    ends.append(end)
    cast["end"] = ends


    cast['end_1'] = []

    ends_1 = []
    end_1 = End_1()
    end_1.set_position(Point(0, 0))
    ends_1.append(end_1)
    cast["end_1"] = ends_1

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
    director.start_game(cast)

    audio_service.stop_audio()

if __name__ == "__main__":
    main()

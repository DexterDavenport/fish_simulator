import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

# IMAGE_BRICK_1 = os.path.join(os.getcwd(), "./fish/assets/brick-2.png")
# IMAGE_BRICK_2 = os.path.join(os.getcwd(), "./fish/assets/brick-3.png")
# IMAGE_BRICK_3 = os.path.join(os.getcwd(), "./fish/assets/brick-5.png")
IMAGE_SHELL = os.path.join(os.getcwd(), "./fish/assets/shell_box.png")
IMAGE_OCEAN = os.path.join(os.getcwd(), "./fish/assets/ocean.png")
IMAGE_FOOD = os.path.join(os.getcwd(), "./fish/assets/ball.png")



# IMAGE_CLOUD = os.path.join(os.getcwd(), "./fish/assets/cloud.png")
IMAGE_SHARK = os.path.join(os.getcwd(), "./fish/assets/shark_box.png")



IMAGE_FISH = os.path.join(os.getcwd(), "./fish/assets/fish_box.png")
# IMAGE_PADDLE = os.path.join(os.getcwd(), "./fish/assets/paddle.png")
IMAGE_BALL = os.path.join(os.getcwd(), "./fish/assets/ball.png")

SOUND_START = os.path.join(os.getcwd(), "./fish/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./fish/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./fish/assets/over.wav")

BALL_X = MAX_X / 2
BALL_Y = MAX_Y - 125

BALL_DX = 8
BALL_DY = BALL_DX * -1

PADDLE_X = MAX_X / 2
PADDLE_Y = MAX_Y - 25

BRICK_WIDTH = 48
BRICK_HEIGHT = 24

BRICK_SPACE = 5

PADDLE_SPEED = 15

PADDLE_WIDTH = 96
PADDLE_HEIGHT = 24

BALL_WIDTH = 24
BALL_HEIGHT = 24


CLOUD_WIDTH = 200
CLOUD_H = 145

SHARK_WIDTH = 250
SHARK_H = 100

FISH_SPEED = 7

FISH_WIDTH = 96
FISH_HEIGHT = 24

FOOD_H = 20
FOOD_W = 20
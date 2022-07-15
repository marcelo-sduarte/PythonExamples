from color import Color
# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 


# GAME
GAME_NAME = "NEPHI_THE_HUNTER"
FRAME_RATE = 60
FREQUENCY = 44100
CHANNELS = 2
SIZE = -16
BUFFER = 512

#FPS
FPS = 60

# SCREEN
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15

#ANIMALS GRID
ROWS = 5
COLUMNS = 5

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "NEPHI_THE_HUNTER/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48


# SOUND

ARROW_SOUND = "sound/arrow_sound.wav"
ANIMAL_SOUND = "sound/animal_sound.wav"
NEPHI_SOUND = "sound/nephi_sound.wav"
VOLUME = 0.25

# IMAGES

ANIMAL_IMAGE = [f"assets/images/animal{n}.png" for n in range(0, 6)]
#ANIMAL_IMAGE = "assets/images/animal1.png"
ARROW_IMAGE = "images/arrow.png"
BOW_IMAGE = "images/bow.png"
DESERT_IMAGE = "images/desert.png"
POISON_IMAGE = "images/poison.png"

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"

# COLORS
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)




#VELOCITY
SPEED = 8

#COOLDOWN MILLISECONDS
COOLDOWN = 1000 

#COUNTER
COUNTDOWN = 3

#FINAL GAME
GAME_OVER = 0


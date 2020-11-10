import pygame

#Global variables
RUN = False

SETTING_DATA = {}


'''In setting_data:
'FULL_SCREEN': bool
'''

#Screen settings
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
ANTI_ALIAS = True
FULLSCREEN = True
FRAME_PER_SECOND = 30
JOYSTICK = None

MEASURE_UNIT = 1/FRAME_PER_SECOND

#pathes
CHI_FONT_PATH = 'data/fonts/chifont.ttf'
ENG_FONT_PATH = 'data/fonts/engfont.ttf'
ALICE_FRONT = 'data/fonts/Alice-Regular.ttf'
JAP_ULT = 'data/fonts/yumin.ttf'
NUM_FONT_PATH = 'data/fonts/engfont2.ttf'
JAP_FONT_PATH = 'data/fonts/japfont2.ttf'

#sprite types
SPRITE_NONE = 0
SPRITE_PLAYER = 1
SPRITE_STATIC_IMAGE = 2
SPRITE_BULLET = 3
SPRITE_ENEMY = 4
SPRITE_BARRAGE = 5
SPRITE_BOSS = 6
SPRITE_ITEM = 7
SPRITE_EFFECT = 8
SPRITE_BOMB = 9
SPRITE_ENEMY_SPECIAL = 10

#player
ALICE = 1
DANTE = 2

# Boundary
LEFT = 0
TOP = 1
RIGHT = 2
BOTTOM = 3

BOUND_PASS = 0
BOUND_BLOCK = 1
BOUND_REFLECT = 2
BOUND_ELASTIC = 3
BOUND_KILL = 4
BOUND_CUSTOM = 5



#key option
KEY_LEFT = pygame.K_LEFT
KEY_RIGHT = pygame.K_RIGHT
KEY_UP = pygame.K_UP
KEY_DOWN = pygame.K_DOWN
KEY_SHUT = pygame.K_z
KEY_SPELL = pygame.K_x
KEY_SLOW = pygame.K_LSHIFT

#Position
TOP_LEFT = 0
TOP_MIDDLE = 1
TOP_RIGHT = 2
CENTER_LEFT = 3
CENTER_MIDDLE = 4
CENTER_RIGHT = 5
BOTTOM_LEFT = 6
BOTTOM_MIDDLE = 7
BOTTOM_RIGHT = 8

#menu types
MENU_TYPE_MAIN = 0 
MENU_TYPE_SELECT_CHARACTER = 1
MENU_TYPE_INGAME = 2
MENU_TYPE_PAUSE = 3



#color
FILL_COLOR = (0,0,0)
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255, 255, 255)
COLOR_GOLD = (255, 215, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_DARK = (40, 40, 40)

#option events
EVENT_SKIP = -1
EVENT_QIUT_GAME = 0
EVENT_NEXT = 1
EVENT_OPTION = 2
EVENT_STATISTIC = 3
EVENT_RESTART = 4
EVENT_QIUT = 5



#varibles in menu.py
'''
        Example of text/title:
        [font, size, color, [text, position]]
        Example of option_list:
        [font, size, color, [[text, position, optionevent], [text2, position2, optionevent2]]
        Example of images:
        [[image_name, position, scale, rotation]]
'''
#text(title)
TEXT_FONT = 0
TEXT_SIZE = 1
TEXT_COLOR = 2
TEXT_DETIALS = 3
#option list/test detials:
TEXT_TEXT = 0
TEXT_VECTOR = 1
OPT_TEXT = 0
OPT_VECTOR = 1
OPT_EVENT = 2
#images
IMAGE_NAME = 0
IMAGE_POSITION = 1
IMAGE_SCALE = 2
IMAGE_ROTATION = 3
IMAGE_DIM = 4





#player
SLOW_MODE = 0
FAST_MODE = 0


#Game
STAGE_LEFT_TOP = (SCREEN_HEIGHT*3*0.025/4, SCREEN_HEIGHT*0.025)
STAGE_WIDTH_HEIGHT = (SCREEN_HEIGHT*3/4,SCREEN_HEIGHT*0.95)
STAGE_RECT = (STAGE_LEFT_TOP, STAGE_WIDTH_HEIGHT)

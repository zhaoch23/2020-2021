import os
import json
import pygame

from functools import wraps
from multiprocessing import Process, Value
from utils.settings import *

#pygame.mixer.init()
#background_music = pygame.mixer.Sound('data/music/mp3/Kanata.mp3')
#background_music.play(-1)

def load_joystick():
    try:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        JOYSTICK = joystick
    except:
        print('No Joystick Attached')

def play_music(music):
    pygame.mixer.Channel(1).queue(music)

def play_sound(sound: object, channel=None):
    if channel:
        pygame.mixer.Channel(channel).play(sound)
    else:
        sound.play()

def load_sound(sound: str) -> object:
    file = f'data/music/ogg/{sound}.ogg'
    if os.path.isfile(file):
        return pygame.mixer.Sound(file)
    
def load_music(sound: str) -> object:
    file = f'data/music/ogg/{sound}.ogg'
    if os.path.isfile(file):
        return pygame.mixer.music.load(file)

#pygame.mixer.init()
#pygame.mixer.music.load('data/music/mp3/Kanata.mp3')
#pygame.mixer.music.play(-1)


def play_music(self):
    pygame.mixer.init()
    pygame.mixer.music.play(-1)

def get_path() -> str:
    """Call this function to get the home path to read/generate
     hidden config/save files
    """
    path = ''
    try:
        path = os.environ['HOME'] + '/.thyye'

    except:
        try:
            path = os.environ['APPDATA'] + '/thyye'
        
        except:
            print('Could not find vailable \'home\'')
            path = '.'
    
    if not os.path.exists(path):
        os.mkdir(path)

    return path


def load_settings():
    """Call this function to read setting file
        and append all setting detials into setting_data: dict
    """

    try:
        file = open(get_path() + '/settings.json', 'r')
        temp_data = json.loads(file.read())
        SETTING_DATA.update(temp_data)
        file.close()

    except IOError:
        print('Missing file: Initializing to default')
        temp_data = {'FULL_SCREEN': False}
        SETTING_DATA.update(temp_data)
        rewrite_settings()

def load_image(image: str, scale=1, rotation=0, dim_value=255, flip=[False, False]) -> object:
    '''load image, Return -> pygame.Surface
    '''
    file = f'data/images/{image}.png'
    if os.path.isfile(file):
        if dim_value == 255:
            image = pygame.image.load(file).convert_alpha()
            image = pygame.transform.rotozoom(image, rotation, scale)
            image = pygame.transform.flip(image, flip[0], flip[1])
            return image
        else:
            image =  pygame.image.load(file).convert_alpha()
            image = pygame.transform.rotozoom(image, rotation, scale)
            image = pygame.transform.flip(image, flip[0], flip[1])
            surface = pygame.Surface(image.get_size(), depth=24)
            key = (0,0,0)
            surface.fill(key)
            surface.set_colorkey(key)
            surface.blit(image, image.get_rect())
            surface.set_alpha(dim_value)

            return surface


def rewrite_settings():
    '''Call this function to rewrite current settings into config file
    '''
    try:
        file = open(get_path() + '/settings.json', 'w')
        data = json.dumps(SETTING_DATA)
        file.write(data)
        print('Successful to rewrite the setting')
        file.close()

    except:
        print('Unknow Reason: Fail to rewrite the setting')
        

def set_fullscreen(full=True):
    """Call this function to set full screen or not
    """
    if full:
        return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    else:
        return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def dim(value, color=(0,0,0)):
    dim = pygame.Surface(pygame.display.get_surface().get_size())
    dim.fill(color)
    dim.set_alpha(value)
    pygame.display.get_surface().blit(dim, pygame.display.get_surface().get_rect())

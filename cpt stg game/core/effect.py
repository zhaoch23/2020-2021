import copy
import random
import math 

from core import animation, image, barrage, item
from core.sprite import *
from utils import utility

def load_data():
    # load data
    an = animation.Animation()
    for i in range(1, 6):
        an.build_animation(f'{i}', [f'effect/circle{i}'])
    Effect.TYPES["circle"] = {"id": 0, "animation": an}

    an = animation.Animation()
    an.build_animation('1', [f'effect/maple'])
    Effect.TYPES['maple'] = {"id": 2, "animation": an}

    an = animation.Animation()
    an.build_animation('1', [f'effect/hp'])
    Effect.TYPES['hp'] = {"id": 3, "animation": an}

    an = animation.Animation()
    for i in range(1, 3):
        an.build_animation(f'{i}', [f'effect/bossback{i}'])
    Effect.TYPES["bossback"] = {"id": 4, "animation": an}

    an = animation.Animation()
    an.build_animation('1', [f'effect/eback'])
    Effect.TYPES['eback'] = {"id": 5, "animation": an}

class Effect(Sprite):

    TYPES = {}

    def __init__(self, parent: object, type_id=['circle', '1']): # Sprite
        super().__init__()
        self.sprite_type = SPRITE_EFFECT
        self.type_id = Effect.TYPES[type_id[0]]['id']
        self.animation = copy.copy(self.TYPES[type_id[0]]['animation'])
        self.animation.set_parent(self)
        self.animation.play_animation(type_id[1])
        self.rect = self.image.get_rect()
        self.hitrect = self.rect
        self.parent = parent

        self.can_collide = False
        self.collided_with = self
        self.bound_style = BOUND_CUSTOM
        self.bounds = -50, -50, STAGE_WIDTH_HEIGHT[0]+50, STAGE_WIDTH_HEIGHT[1]+50
        self.active = True
        
        self.position  = vector.objVector(0,0)
        self.velocity  = vector.objVector(0,0)

        self.timer = 0

        #effect attributes
        self.rotating = True
        self.rotate_angle = 10
        self.scale = 1
    
    def custom_update(self):      
        if self.rotating:
            self.rotate_angle += 5
            self.rotate(360/FRAME_PER_SECOND/3)
        
        self.timer += 1
        

    def rotate(self, angle):
        center = self.position.x, self.position.y
        rotated_image = pygame.transform.rotate(self.image, angle)
        self.rect = rotated_image.get_rect(center=center)
        self.image = rotated_image


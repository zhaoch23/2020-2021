import copy
import random
import math 

from core import animation, image, barrage, item
from core.sprite import *
from utils import utility

def load_data():
    Bomb.ANIMATION_LIST.build_animation('idle', ['effect/bomb'], scale=2.5)


class Bomb(Sprite):

    ANIMATION_LIST = animation.Animation()

    def __init__(self, parent: object): # Game
        super().__init__()
        self.sprite_type = SPRITE_BOMB
        self.animation = copy.copy(self.ANIMATION_LIST)
        self.animation.set_parent(self)
        self.animation.play_animation("idle")
        self.rect = self.image.get_rect()
        self.hitrect = self.rect
        self.parent = parent

        self.can_collide = True
        self.collided_with = self
        self.bound_style = BOUND_CUSTOM
        self.bounds = 0, 0, STAGE_WIDTH_HEIGHT[0], STAGE_WIDTH_HEIGHT[1]
        self.active = True
        
        self.position  = vector.objVector(0,0)
        self.velocity  = vector.objVector(0, -300*MEASURE_UNIT)

        self.timer = 0

        self.rotate_angle = 0
        self.scale = 1

    
    def custom_update(self): # bomb acceleration     
        self.acceleration = vector.objVector(0, 3*MEASURE_UNIT)
        self.rotate(self.rotate_angle)
        self.rotate_angle += self.velocity.norm

        if self.parent.boss_group.sprites():
            self.acceleration = vector.objVector(0, 6*MEASURE_UNIT)
            self.scale -= 0.02
        else:
            self.scale -= 0.01
        self.rescale()

        if self.velocity.y >= 0:
            self.die()
    
    def rotate(self, angle): # bomb rotation
        center = self.position.x, self.position.y
        rotated_image = pygame.transform.rotate(self.image, angle)
        self.rect = rotated_image.get_rect(center=center)
        self.image = rotated_image

    def rescale(self):
        center = self.position.x, self.position.y
        scaled_image = pygame.transform.rotozoom(self.image, 1, self.scale)
        self.rect = self.hitrect = scaled_image.get_rect(center=center)
        self.image = scaled_image
    
    def collide(self): # bomb collide with eneny
        if self.collided_with.sprite_type == SPRITE_BOSS:
            self.collided_with.health -= 1
        elif self.collided_with.sprite_type == SPRITE_ENEMY:
            self.collided_with.health -= 9999
        elif self.collided_with.sprite_type == SPRITE_BARRAGE:
            d = item.Item(self.parent, "smallpoint")
            d.position = self.collided_with.position
            d.collected = True
            self.collided_with.die()
            self.parent.item_group.add(d)

import copy
import random
import math 

from core import animation, image
from core.sprite import *
from utils import utility

def load_data():
    Bullet.BULLET_ANIMATION_LIST.build_animation('flow1', ['bullet/bullet1'], scale=1.5, dim_value=138)
    Bullet.BULLET_ANIMATION_LIST.build_animation('flow2', ['bullet/bullet2'], scale=1.5, dim_value=138)
    Bullet.BULLET_ANIMATION_LIST.build_animation('track1', ['bullet/bullet3'], scale=2)
    Bullet.BULLET_ANIMATION_LIST.build_animation('track2', ['bullet/bullet4'], scale=2)

class Bullet(Sprite):#parent

    BULLET_ANIMATION_LIST = animation.Animation()

    def __init__(self, parent, type_id='flow1'): # parent: Game
        super().__init__()
        self.sprite_type = SPRITE_BULLET
        self.type_id = type_id
        self.animation = copy.copy(self.BULLET_ANIMATION_LIST)
        self.animation.set_parent(self)
        self.animation.play_animation(type_id)
        self.rect = self.image.get_rect()
        self.hitrect = self.rect

        self.parent = parent
        self.can_collide = True
        self.bound_style = BOUND_KILL
        self.bounds = 0, 0, STAGE_WIDTH_HEIGHT[0]+50, STAGE_WIDTH_HEIGHT[1]+50
        self.active = True

        self.position = vector.objVector(0, 0)
        self.velocity = vector.objVector(0, 0)
        
        #other attributes
        self.damage = 0
        self.tracked = False

    def custom_update(self):
        
        if len(self.parent.enemy_group.sprites()) > 0:
            if (self.type_id == 'track1' or self.type_id == 'track2') and not self.tracked and self.position.y >= self.sort_list(self.parent.enemy_group.sprites())[0].position.y:
                e = self.sort_list(self.parent.enemy_group.sprites())[0]
                try:
                    bdirection = (self.position.x - self.parent.player.position.x)/abs(self.position.x - self.parent.player.position.x)
                    edirection = (e.position.x - self.parent.player.position.x)/abs(e.position.x - self.parent.player.position.x)
                    if bdirection == edirection:
                        self.tracked = True
                        speed = self.velocity.norm
                        self.velocity =  e.position - self.position
                        self.velocity.norm = speed
                        self.auto_rotate()
                except:
                    pass
        else:
            try:
                if (self.type_id == 'track1' or self.type_id == 'track2'):
                    e = self.parent.boss_group.sprites()[0]
                    if STAGE_WIDTH_HEIGHT[0] > e.position.x > 0 and STAGE_WIDTH_HEIGHT[1] > e.position.y > 0:
                        self.tracked = True
                        speed = self.velocity.norm
                        self.velocity =  e.position - self.position
                        self.velocity.norm = speed
                        self.auto_rotate()
                
            except:
                pass
    
    def auto_rotate(self):
        self.image = pygame.transform.rotate(self.image, self.velocity.angle)
                    

    def sort_list(self, sprites):
        try:
            for i in range(len(sprites) - 1):
                sorted = True
                for j in range(len(sprites) - i - 1):
                    if sprites[j].postion.y < sprites[j + 1].position.y:
                        ships[j], ships[j + 1] = sprites[j + 1], sprites[j]
                        sorted = False
                
                if sorted == True:
                    break
        except:
            pass
        
        return sprites
    
    
    def collide(self):
        if self.type_id != 'flow2':
            self.die()



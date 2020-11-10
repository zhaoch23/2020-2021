import copy
import random
import math 

from core import animation, image, barrage, item, effect
from ui import text
from core.sprite import *
from utils import utility

sin = math.sin
cos = math.cos
pi = math.pi

def load_data():
    '''
    load data
    '''
    an = animation.Animation()
    an.build_animation('idle', ['enemy/margatroid'], 0.8)
    Boss.TYPES["margatroid"] = {"id": 0, "animation": an} 

class Boss(Sprite):
    '''
    boss settings
    '''
    TYPES = {}

    def __init__(self, parent: object, type_id='margatroid'):
        super().__init__()
        self.sprite_type = SPRITE_BOSS
        self.type_id = Boss.TYPES[type_id]['id']
        self.animation = copy.copy(self.TYPES[type_id]['animation'])
        self.animation.set_parent(self)
        self.animation.play_animation('idle')
        self.rect = self.image.get_rect()
        self.hitrect = self.rect

        self.parent = parent
        self.can_collide = True
        self.collided_with = self
        self.bound_style = BOUND_CUSTOM
        self.bounds = -50, -50, STAGE_WIDTH_HEIGHT[0]+50, STAGE_WIDTH_HEIGHT[1]+50
        self.active = True

        self.position  = vector.objVector(0,0)
        self.velocity  = vector.objVector(0,0)

        self.speed = 0
        self.timer = 0


        self.health = 200
        self.health_max = 200
        self.delta_damge = 0
        self.invulnerable = False

        self.phase_list = [self.defualt_move] # contents actions of phases
        self.phase = 0
        self.phase_timer = 0

        self.fire = 0
        self.fire_pattern = [self.defualt_fire]
        self.fire_timer = 0
        self.fire_pattern_temp = {}

        self.health_bar = pygame.sprite.Group()
        self.effect_group = pygame.sprite.Group()

        self.done = False

        for i in range(556):
            h = effect.Effect(self, ["hp", "1"])
            h.position = vector.objVector(5 + 1*i, 5)
            h.rotating = False

            self.health_bar.add(h)
            self.parent.effect_group.add(h)

    def collide(self):
        '''
        When boss collide with bullets, her health will reduce.
        When boss's health below zero, it dies
        '''
        if self.collided_with.sprite_type == SPRITE_BULLET and not self.invulnerable:
            self.health -= self.collided_with.damage

           
            if self.health < 0:
               self.done = True
            else:
                self.delta_damge += self.collided_with.damage
                health_decline = self.delta_damge//(self.health_max/556)
                if health_decline > 0:
                    for i in range(int(health_decline)):
                        self.delta_damge -= self.health_max/556
                        try:
                            remove = self.health_bar.sprites().pop()
                            remove.die()
                        except:
                            pass

    
    def set_health(self, value):
        for i in self.health_bar.sprites():
            i.die()
        self.done = False

        if value > 0:
            self.health = value
            self.health_max = value
            self.delta_damge = 0

            for i in range(556):
                h = effect.Effect(self, ["hp", "1"])
                h.position = vector.objVector(5 + 1.*i, 5)
                h.rotating = False

                self.health_bar.add(h)
                self.parent.effect_group.add(h)

    def next_phase(self):
        self.phase += 1
        self.phase_timer = 0
    
    def next_fire(self):
        self.fire += 1
    
    def defualt_move(self, child):
        self.phase_timer += 1

    def defualt_fire(self, child):
        self.fire_timer += 1

    def custom_update(self):       

        self.phase_list[self.phase](self) # call the actions of this phase
        self.phase_timer += 1

        try:
            # check if there is an barrage on this point of time
            for b in self.fire_pattern_temp.pop(self.timer):
                b.set_up()
                # if has, add it to game class' barrage group
                self.parent.barrage_group.add(b)
        except:
            pass
        

        self.timer += 1
    
    def custom_death(self):
        for e in self.effect_group.sprites():
            e.die()

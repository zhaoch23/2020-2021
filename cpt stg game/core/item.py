import copy
import random
import math 

from core import animation, image, barrage
from core.sprite import *
from utils import utility

sin = math.sin
cos = math.cos
pi = math.pi

def load_data(): # load all image datas of enemy
    an = animation.Animation()
    an.build_animation('idle', ['items/item1'], 1.5)
    Item.TYPES["power"] = {"id": 1, "animation": an}
    an = animation.Animation()
    an.build_animation('idle', ['items/item2'], 1.5)
    Item.TYPES["point"] = {"id": 2, "animation": an}
    an = animation.Animation()
    an.build_animation('idle', ['items/item3'], 1.5)
    Item.TYPES["starpoint"] = {"id": 3, "animation": an}
    an = animation.Animation()
    an.build_animation('idle', ['items/item4'], 1.5)
    Item.TYPES["largepower"] = {"id": 4, "animation": an}
    an = animation.Animation()
    an.build_animation('idle', ['items/item5'], 1.5)
    Item.TYPES["largepoint"] = {"id": 5, "animation": an}
    an = animation.Animation()
    an.build_animation('idle', ['items/item6'], 1.5)
    Item.TYPES["fullpower"] = {"id": 6, "animation": an}
    an = animation.Animation()
    an.build_animation('idle', ['items/item7'], 1.5)
    Item.TYPES["life"] = {"id": 7, "animation": an}
    an = animation.Animation()
    an.build_animation('idle', ['items/item8'])
    Item.TYPES["smallpoint"] = {"id": 8, "animation": an}

class Item(Sprite):

    TYPES = {}

    def __init__(self, parent: object, type_id='power'): #parent: Game
        super().__init__()
        self.type_id = Item.TYPES[type_id]['id']
        self.animation = copy.copy(self.TYPES[type_id]['animation'])
        self.animation.set_parent(self)
        self.animation.play_animation('idle')
        self.rect = self.image.get_rect()
        self.hitrect = self.rect
        self.sprite_type = SPRITE_ITEM
        self.parent = parent

        self.can_collide = True
        self.collided_with = self
        self.bound_style = BOUND_KILL
        self.bounds = 0, -100, STAGE_WIDTH_HEIGHT[0], STAGE_WIDTH_HEIGHT[1]
        self.active = True
        
        self.position  = vector.objVector(0,0)
        self.velocity  = vector.objVector(0, -50*MEASURE_UNIT)
        self.acceleration = vector.objVector(0, 2*MEASURE_UNIT)

        self.collected = False

    def collide(self): # determine collisions
        if self.collided_with.sprite_type == SPRITE_PLAYER:
            if self.type_id == 1:
                self.parent.player.power += 0.05
                self.parent.player.score += 1
            elif self.type_id == 2:
                self.parent.player.point += 1
                self.parent.player.score += 1
            elif self.type_id == 3:
                self.parent.player.point += 1
                self.parent.player.score += 1
            elif self.type_id == 4:
                self.parent.player.power += 0.25
                self.parent.player.score += 5
            elif self.type_id == 5:
                self.parent.player.point += 5
                self.parent.player.score += 5
            elif self.type_id == 6:
                self.parent.player.power = 5.00
            elif self.type_id == 7:
                self.parent.player.life += 1
                self.parent.player.score += 10
            elif self.type_id == 8:
                self.parent.player.score += 0.1

            self.die()
    
    def custom_update(self):
        # item pick up update
        if not self.collected and self.velocity.norm >= 200*MEASURE_UNIT:
            self.velocity.norm = 150*MEASURE_UNIT

        if (self.type_id == 1 or self.type_id == 4) and self.parent.player.power >= 5.00:
            point = Item(self.parent, 'starpoint')
            point.position = self.position
            point.velocity = self.velocity
            self.parent.item_group.add(point)
            self.die()

        if self.collected:
            speed = self.velocity.norm
            self.velocity = (self.parent.player.position - self.position)
            
            if speed <= self.velocity.norm:
                self.acceleration = self.parent.player.position - self.position
                self.acceleration.norm = 100*MEASURE_UNIT
            else:
                speed = (self.parent.player.position.norm - self.position.norm)
            
            self.velocity.norm = speed

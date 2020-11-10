import copy
import random
import math 

from core import animation, image, barrage, item
from core.sprite import *
from utils import utility
from effect import death_effect

sin = math.sin
cos = math.cos
pi = math.pi

def load_data(): # load all image datas of enemy
    an = animation.Animation()
    an.build_animation('left', ['enemy/redsprite1', 'enemy/redsprite2', 'enemy/redsprite3'])
    an.build_animation('idle', ['enemy/redsprite4', 'enemy/redsprite5', 'enemy/redsprite6'])
    an.build_animation('right', ['enemy/redsprite7', 'enemy/redsprite8', 'enemy/redsprite9'])
    Enemy.TYPES["redsprite"] = {"id": 0, "animation": an}

    an = animation.Animation()
    an.build_animation('left', ['enemy/bluesprite5'], 1.5)
    an.build_animation('idle', ['enemy/bluesprite1', 'enemy/bluesprite2', 'enemy/bluesprite3', 'enemy/bluesprite4'], 1.5)
    an.build_animation('right', ['enemy/bluesprite5'], 1.5, flip=[True, False])
    Enemy.TYPES["bluesprite"] = {"id": 1, "animation": an}

    an = animation.Animation()
    an.build_animation('left', ['enemy/yellowsprite5'], 1.5)
    an.build_animation('idle', ['enemy/yellowsprite1', 'enemy/yellowsprite2', 'enemy/yellowsprite3', 'enemy/yellowsprite4'], 1.5)
    an.build_animation('right', ['enemy/yellowsprite5'], 1.5, flip=[True, False])
    Enemy.TYPES["yellowsprite"] = {"id": 2, "animation": an}

    an = animation.Animation()
    an.build_animation('left', ['enemy/greensprite5'], 1.5)
    an.build_animation('idle', ['enemy/greensprite1', 'enemy/greensprite2', 'enemy/greensprite3', 'enemy/greensprite4'], 1.5)
    an.build_animation('right', ['enemy/greensprite5'], 1.5, flip=[True, False])
    Enemy.TYPES["greensprite"] = {"id": 3, "animation": an}
    
    
    an = animation.Animation()
    an.build_animation('left', ['ruri/RuriA02'])
    an.build_animation('idle', ['ruri/RuriA02'])
    an.build_animation('right', ['ruri/RuriA-02'])
    Enemy.TYPES["kimonoruri"] = {"id": 4, "animation": an}
    
    an = animation.Animation()
    an.build_animation('left', ['ruri/RuriB02'])
    an.build_animation('idle', ['ruri/RuriB02'])
    an.build_animation('right', ['ruri/RuriB-02'])
    Enemy.TYPES["katanaruri"] = {"id": 5, "animation": an}

    for i in range(4):
        an = animation.Animation()
        an.build_animation('left', [f'enemy/mess{i+1}'], 1.5)
        an.build_animation('idle', [f'enemy/mess{i+1}'], 1.5)
        an.build_animation('right', [f'enemy/mess{i+1}'], 1.5)
        Enemy.TYPES[f"mess{i+1}"] = {"id": 6, "animation": an}

class Enemy(Sprite):

    TYPES = {}

    def __init__(self, parent: object, type_id='redsprite'):
        super().__init__()
        self.type_id = Enemy.TYPES[type_id]['id']
        self.animation = copy.copy(self.TYPES[type_id]['animation'])
        self.animation.set_parent(self)
        self.animation.play_animation('idle')
        self.rect = self.image.get_rect()
        self.hitrect = self.rect
        self.sprite_type = SPRITE_ENEMY
        self.parent = parent

        self.can_collide = True
        self.collided_with = self
        self.bound_style = BOUND_KILL
        self.bounds = -50, -50, STAGE_WIDTH_HEIGHT[0]+50, STAGE_WIDTH_HEIGHT[1]+50
        self.active = True
        
        self.position  = vector.objVector(0,0)
        self.velocity  = vector.objVector(0,0)

        self.speed = 0
        self.health = 0
        self.invulnerable = False

        self.timer = 0

        self.phase_list = [self.defualt_move] # contents actions of phases
        self.phase = 0
        self.phase_timer = 0 

        self.fire = 0
        self.fire_pattern = [self.defualt_fire]
        self.fire_pattern_temp = {} # contents the barrages of this enemy
        self.fire_group = pygame.sprite.Group()

        self.effect_group = pygame.sprite.Group()

        self.death_animation = death_effect.DeathEffect(self)

        self.item_list = []
        for i in range(2):
            i1 = item.Item(self.parent, 'power')
            i2 = item.Item(self.parent, 'point')
            self.item_list.append(i1)
            self.item_list.append(i2)
        
        self.rotating = False
        self.rotate_angle = 10
            

    def collide(self): # determine collisions
        if self.collided_with.sprite_type == SPRITE_BULLET and not self.invulnerable:
            self.health -= self.collided_with.damage
        
        if self.health <= 0:
            self.parent.player.score += 5


            self.death_animation.position = self.position
            self.parent.effect_group.add(self.death_animation)    

            self.die()

    def custom_death(self):
        for b in self.fire_group.sprites():
            b.die()

        for e in self.effect_group.sprites():
            e.die()
            
        for i in self.item_list:
                rx = random.randrange(-25, 25)
                ry = random.randrange(-25, 25)
                i.position = vector.objVector(self.position.x + rx, self.position.y + ry)
                self.parent.item_group.add(i)
            

    
    def custom_update(self):       
        #update the animations of the enemy 
        if self.velocity.x > 0:
            self.animation.play_animation('right')
        elif self.velocity.x < 0:
            self.animation.play_animation('left')
        else:
            self.animation.play_animation('idle')

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

        if self.rotating:
            self.rotate(self.rotate_angle)
            self.rotate_angle += 10

        self.timer += 1
    

    def rotate(self, angle=0):
        center = self.position.x, self.position.y
        rotated_image = pygame.transform.rotate(self.image, angle)
        self.rect = rotated_image.get_rect(center=center)
        self.image = rotated_image
    
    def next_phase(self):
        self.phase += 1
        self.phase_timer = 0
    
    def next_fire(self):
        self.fire += 1
        self.fire_timer = 0

    def defualt_move(self, child):
        pass

    def defualt_fire(self, child):
        pass


    # some defualt complex barrage pattern
    @staticmethod #通常自机狙, defualt barrage pattern - regular player aimming
    def defualt_danmaku_pattern_001(child, barrage_type=['diamond', '4'], count=5, delta_time=5, speed=250*MEASURE_UNIT):
        time = child.timer
        for i in range(count):
            dt = i*delta_time
            b = barrage.Barrage(child, barrage_type)
            b.velocity = vector.objVector(child.parent.player.position - b.parent.position)
            b.velocity.norm = speed
            try:
                child.fire_pattern_temp[time + dt].append(b)
            except:
                child.fire_pattern_temp[time + dt] = []
                child.fire_pattern_temp[time + dt].append(b)
        
    @staticmethod #瞄准自机狙, defualt barrage pattern - aimming player aimming
    def defualt_danmaku_pattern_002(child, barrage_type=['square', '1'], count=5, delta_time=5, speed=250*MEASURE_UNIT):
        time = child.timer
        for i in range(count):
            dt = i*delta_time
            b = barrage.Barrage(child, barrage_type)
            b.aim = True
            b.speed = speed
            try:
                child.fire_pattern_temp[time + dt].append(b)
            except:
                child.fire_pattern_temp[time + dt] = []
                child.fire_pattern_temp[time + dt].append(b)

    @staticmethod #变速瞄准自机狙
    def defualt_danmaku_pattern_003(child, barrage_type=['viodball', '1'], count=5, delta_time=5, speed=100*MEASURE_UNIT, ds=50*MEASURE_UNIT):
        time = child.timer
        for i in range(count):
            dt = i*delta_time
            b = barrage.Barrage(child, barrage_type)
            b.aim = True
            b.speed = speed + i*ds
            try:
                child.fire_pattern_temp[time + dt].append(b)
            except:
                child.fire_pattern_temp[time + dt] = []
                child.fire_pattern_temp[time + dt].append(b)
    
    @staticmethod #圆形散射
    def defualt_danmaku_pattern_004(child, barrage_type=['texturedball', '6'], count1=5, count2=18, delta_time=10, speed=250*MEASURE_UNIT):
        '''circular scattering
        '''
        time = child.timer
        for i in range(count1):
            dt = i*delta_time
            temp_list = []
            for j in range(count2):
                b = barrage.Barrage(child, barrage_type)
                b.speed = speed
                b.aim = True
                b.setup_angle = j*(360/count2)
                temp_list.append(b)

            try:
                child.fire_pattern_temp[time + dt].append(b)
            except:
                child.fire_pattern_temp[time + dt] = []
                child.fire_pattern_temp[time + dt] = child.fire_pattern_temp[time + dt] + temp_list
    

    # 扇形随机散射
    @staticmethod
    def defualt_danmaku_pattern_005(child, barrage_type=['diamond', '1'], count=50, angle=90, delta_time=4, speed=250*MEASURE_UNIT, ds=-2*MEASURE_UNIT):
        '''circular scattering
        '''
        time = child.timer
        for i in range(count):
            dt = i*delta_time
            b = barrage.Barrage(child, barrage_type)
            b.speed = speed + ds*i
            b.velocity = vector.objVector(0, b.speed)
            b.setup_angle = random.randrange(int(-1*angle/2), angle/2)


            try:
                child.fire_pattern_temp[time + dt].append(b)
            except:
                child.fire_pattern_temp[time + dt] = []
                child.fire_pattern_temp[time + dt].append(b)

        
    @staticmethod
    def defualt_danmaku_pattern_006(child, end_point=vector.objVector(0,0), barrage_type=['laser', '1']):
        time = child.timer
        distance = end_point - child.position
        angle = distance.angle
        center = distance/2

        b = barrage.Barrage(child, barrage_type)
        b.position = child.position + center
        b.phase_list = [barrage.Barrage.motion_laser]
        b.correct_start_position = False
        b.height = int(distance.norm)
        child.fire_group.add(b)

        try:
            child.fire_pattern_temp[time].append(b)
        except:
            child.fire_pattern_temp[time] = []
            child.fire_pattern_temp[time].append(b)

import copy
import random
import math 

from core import animation, image, item, bomb, barrage
from core.sprite import *
from utils import utility

sin = math.sin
cos = math.cos
pi = math.pi


class Player(Sprite):

    def __init__(self, parent: object):
        # init and settings
        super().__init__()

        self.sprite_type = SPRITE_PLAYER
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.collectrect = pygame.Rect(0, 0, 100, 100)
        self.hitrect = self.rect
        self.parent = parent
    

        self.can_collide = True
        self.bound_style = BOUND_BLOCK
        self.bounds = 25, 25, STAGE_WIDTH_HEIGHT[0]-25, STAGE_WIDTH_HEIGHT[1]-25
        self.active = True
        
        self.position  = vector.objVector(STAGE_WIDTH_HEIGHT[0]/2, STAGE_WIDTH_HEIGHT[1]/1.25)
        self.velocity  = vector.objVector(0,0)

        #other attributes这些可以在子级中reload
        self.name = None
        self.life = 0
        self.score = 0
        self.point = 0
        self.power = 0.00
        self.graze = 0
        self.fire_mode = 0 #火力登记
        self.fast_speed = 2*MEASURE_UNIT
        self.slow_speed = 1*MEASURE_UNIT
        self.speed = self.fast_speed
        self.slow_mode = False
        self.invulnerable = True
        self.invulnerable_time = FRAME_PER_SECOND*3
        self.dead = False
        self.collide_point = None
        self.bullet_types = []#装入该对象会发射的弹幕的种类 对象是Bullet
        self.timer = 0
        self.bomb_colddown = 0
        self.dead = False

        self.testing = False



    def check_collision(self, group):
        # check collision, if collide, apply following
        for obj in group:
            if self.hitrect.colliderect(obj.hitrect):
                if self.active and obj.active and self.can_collide and obj.can_collide:
                    self.collided_with = obj
                    obj.collided_with = self
                    self.collide()
                    obj.collide()
            
            elif self.active and obj.active and obj.sprite_type == SPRITE_BARRAGE and not obj.grazed:
                if self.rect.colliderect(obj.hitrect):
                    obj.grazed = True
                    self.graze += 1
            
            elif self.active and obj.active and obj.sprite_type == SPRITE_ITEM and not obj.collected:
                if self.collectrect.colliderect(obj.hitrect):
                    obj.collected= True


    def custom_update(self):


        keys = pygame.key.get_pressed()
        
        # slow mode key and spell(bomb) key.
        if keys[KEY_SLOW]:
            self.speed = self.slow_speed
            self.slow_mode = True
        else:
            self.speed = self.fast_speed
            self.slow_mode = False

        if self.bomb_colddown > 0:
            self.bomb_colddown -= 1
        if keys[KEY_SPELL] and self.bomb_colddown <= 0 and self.power >= 1:
            b = bomb.Bomb(self.parent)
            b.position = self.position
            self.power -= 1
            self.bomb_colddown = 5*FRAME_PER_SECOND
            self.invulnerable = True
            self.parent.bomb_group.add(b)

        if self.point >= 100:
            self.point -= 100
            self.life += 1

        # movement
        if keys[KEY_RIGHT] and keys[KEY_LEFT]:
            self.velocity.x = 0
            # self.animation.play_animation('idle')
        elif keys[KEY_LEFT]:
            self.velocity.x = -1*self.speed
            # self.animation.play_animation('left')
        elif keys[KEY_RIGHT]:
            self.velocity.x = self.speed
            # self.animation.play_animation('right')
        else:
            self.velocity.x = 0
            # self.animation.play_animation('idle')
        if keys[KEY_UP] and keys[KEY_DOWN]:
            self.velocity.y = 0
        elif keys[KEY_UP]:
            self.velocity.y = -1*self.speed
        elif keys[KEY_DOWN]:
            self.velocity.y = self.speed
        else:
            self.velocity.y = 0

        if keys[KEY_SHUT]:
            self.fire()

        
        if self.velocity.norm > self.speed:
            self.velocity.norm = self.speed


        if self.velocity.x > 0:
            self.animation.play_animation('right')
        elif self.velocity.x < 0:
            self.animation.play_animation('left')
        else:
            self.animation.play_animation('idle')

        self.collectrect.center = (self.position.x, self.position.y)
        # if power achieved 5.0, it will not excess
        if self.power > 5.00:
            self.power = 5.00

        if self.power < 0:
            self.power = 0.00
        
        if self.position.y <= STAGE_WIDTH_HEIGHT[1]*0.3 and not self.slow_mode:
            for i in self.parent.item_group.sprites():
                i.collected= True
            
        if self.invulnerable:
            # invulnerable when player spawned or revived
            self.invulnerable_time -= 1
            if not self.parent.bomb_group.sprites():
                for b in self.parent.barrage_group.sprites():
                    b.die()
            else:
                self.invulnerable_time -= 45
            if self.invulnerable_time <= 0:
                self.invulnerable_time = FRAME_PER_SECOND*3
                self.invulnerable = False
            
            elif self.invulnerable_time % 10 == 0:
                self.image.set_alpha(100)
            
            elif self.invulnerable_time % 5 == 0:
                self.image.set_alpha(255)
        else:
            self.image.set_alpha(255)

        if self.timer == 0:
            self.position = vector.objVector(STAGE_WIDTH_HEIGHT[0]/2, STAGE_WIDTH_HEIGHT[1]-26)
            self.timer += 1
        elif 0 < self.timer <= 10:
            self.timer += 1
            self.velocity = vector.objVector(0, -self.slow_speed)
        else:
            self.timer = -1


    def collide(self):
        if (self.collided_with.sprite_type == SPRITE_BARRAGE or self.collided_with.sprite_type == SPRITE_ENEMY) and not self.invulnerable:
            if not self.testing:
                self.invulnerable = True
                self.hurt()
            else:
                self.life -= 1
    
    def hurt(self):
        # shot check
        if self.life >= 0:
            self.timer = 0
            for i in range(5):
                a = random.randint(0,1)
                ran = vector.objVector(100, 0)
                ran.angle = 90 - i*36
                if a == 0:
                    d = item.Item(self.parent, 'power')
                    d.position = self.position + ran
                    self.parent.item_group.add(d)
                else:
                    d = item.Item(self.parent, 'largepower')
                    d.position = self.position + ran
                    self.parent.item_group.add(d)

            for b in self.parent.barrage_group.sprites():
                b.die()
            
            for e in self.parent.enemy_group.sprites():
                e.die()


            self.power -= 1
            self.life -= 1
            
            if self.life < 0:
                self.dead = True

        

    def fire(self): #这个方法用来制作活力系统
        pass

        
        
    
    





        

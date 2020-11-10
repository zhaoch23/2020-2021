import pygame

from core import animation
from utils import vector
from utils.settings import *


class Sprite(pygame.sprite.Sprite):

    def __init__(self):
        # init
        pygame.sprite.Sprite.__init__(self)

        self.sprite_type = SPRITE_NONE
        self.can_collide = False
        self.active = True
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.hitrect = pygame.Rect(0, 0, 0, 0)
        self.collided_with = self
        self.bound_style = BOUND_BLOCK,
        self.animation = animation.Animation()
        self.image = None
        self.position = vector.objVector(0, 0)
        self.velocity = vector.objVector(0, 0)
        self.acceleration = vector.objVector(0, 0)
        self.bounds = 0, 0, 0, 0

    def __str__(self):
        return self.sprite_type

    def show(self):
        pass

    def custom_update(self):
        pass

    def update(self):
        # animation and velocity updates
        try:
            self.animation.update()
            if self.animation.is_playing:
                self.image = self.animation.image
        except:
            pass

        self.position += self.velocity
        self.velocity += self.acceleration
        self.check_bounds()
        self.rect.center = self.hitrect.center = (self.position.x, self.position.y)

        self.custom_update()
        

    def check_collision(self, group):
        # chech collisions, if unit collide with bullets or barrages, apply following
        for obj in group:
            if self.hitrect.colliderect(obj.hitrect):
                if self.active and obj.active and self.can_collide and obj.can_collide:
                    self.collided_with = obj
                    obj.collided_with = self
                    self.collide()
                    obj.collide()

    def collide(self):
        pass
        
    def check_bounds(self):
        # check of if the unit exceed bounds of the game
        current_x = self.position.x
        current_y = self.position.y
        if current_x < self.bounds[LEFT] or current_x > self.bounds[RIGHT] or current_y < self.bounds[TOP] or current_y > self.bounds[BOTTOM]:
            self.out_of_bounds()

    def custom_death(self):
        pass

    def die(self):
        # unit die
        self.custom_death()
        self.kill()
        del self
        
    def out_of_bounds(self):
        # out of bounds effect
        if self.bound_style == BOUND_BLOCK:
            if self.position.x < self.bounds[LEFT]:
                self.position = vector.objVector(self.bounds[LEFT], self.position.y)
            elif self.position.x > self.bounds[RIGHT]:
                self.position = vector.objVector(self.bounds[RIGHT], self.position.y)
            if self.position.y < self.bounds[TOP]:
                self.position = vector.objVector(self.position.x, self.bounds[TOP])
            elif self.position.y > self.bounds[BOTTOM]:
                self.position = vector.objVector(self.position.x, self.bounds[BOTTOM])
                
        elif self.bound_style == BOUND_PASS:
            if self.position.x < self.bounds[LEFT]:
                self.position = vector.objVector(self.bounds[RIGHT], self.position.y)
            elif self.position.x > self.bounds[RIGHT]:
                self.position = vector.objVector(self.bounds[LEFT],self.position.y)
            if self.position.y < self.bounds[TOP]:
                self.position = vector.objVector(self.position.x, self.bounds[BOTTOM])
            elif self.position.y > self.bounds[BOTTOM]:
                self.position = vector.objVector(self.position.x, self.bounds[TOP])
                
        elif self.bound_style == BOUND_REFLECT:
            if self.position.x < self.bounds[LEFT]:
                self.position = vector.objVector(self.bounds[LEFT], self.position.y)
                self.velocity *= -1.0, 1.0
            elif self.position.x > self.bounds[RIGHT]:
                self.position = vector.objVector(self.bounds[RIGHT], self.position.y)
                self.velocity *= -1.0, 1.0
            if self.position.y < self.bounds[TOP]:
                self.position = vector.objVector(self.position.x, self.bounds[TOP])
                self.velocity *= 1.0, -1.0
            elif self.position.y > self.bounds[BOTTOM]:
                self.position = vector.objVector(self.position.x, self.bounds[BOTTOM])
                self.velocity *= 1.0, -1.0
        
        elif self.bound_style == BOUND_ELASTIC:
            pass
                
        elif self.bound_style == BOUND_KILL:
            self.die()
            
        elif self.bound_style == BOUND_CUSTOM:
            self.custom_bounds()


    def custom_bounds(self):
        pass

    def get_x(self):
        return self.position.x
    def set_x(self, value):
        self.position.x = value
    def del_x(self):
        self.position.x = 0      
    x = property(get_x, set_x, del_x, 'position x')
    def get_y(self):
        return self.position.y
    def set_y(self, value):
        self.position.y = value
    def del_y(self):
        self.position.y = 0
    y = property(get_y, set_y, del_y, 'position y')
    def get_vx(self):
        return self.velocity.x
    def set_vx(self, value):
        self.velocity.x = value
    def del_vx(self):
        self.velocity.x = 0
    vx = property(get_vx, set_vx, del_vx, 'velocity x')
    def get_vy(self):
        return self.velocity.y
    def set_vy(self, value):
        self.velocity.y = value
    def del_vy(self):
        self.velocity.y = 0
    vy = property(get_vy, set_vy, del_vy, 'velocity y')

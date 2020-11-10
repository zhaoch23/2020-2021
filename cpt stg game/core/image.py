import copy

from core.sprite import *

class Image(Sprite):
    
    STATIC_ANIMATION_LIST = animation.Animation()
    
    #animation 
    def __init__(self, image_name:str, scale=1, rotate=0, dim_value=0):
        super().__init__()
        self.sprite_type = SPRITE_STATIC_IMAGE
        self.animation_list = copy.copy(self.STATIC_ANIMATION_LIST)

        self.animation_list.build_animation('idle', [image_name], scale, rotate, dim_value)
        self.animation_list.play_animation('idle')
        self.animation_list.set_parent(self)
        
        self.rect = self.image.get_rect()

        self.position = vector.objVector(0,0)
        self.position = vector.objVector(0,0)

        self.bounds = 0,0,SCREEN_WIDTH,SCREEN_HEIGHT

    def show(self, screen):
        screen.blit(self.image, self.rect)

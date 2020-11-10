import pygame

from utils.utility import *
from utils import vector

class Text(pygame.sprite.Sprite):
    def __init__(self, font_type, font_size=12, color=(0, 0, 0), text='', life_timer=-1, text_index=0, alignment=CENTER_MIDDLE):
        '''Heriate this class to draw texts
            Args:
                font_type -> str: font type
                font_size -> float: font size, default = 12
                color -> (int, int, int): font color, default = (0, 0, 0)
                text -> str: text
                life_timer -> int: text duration, default = -1
                text_index -> int: text index, default = 0
        '''
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()

        self.original_text = text
        self.original_color = color
        self.original_font_size = font_size
        self.original_font_type = font_type

        self.text_index = text_index
        self.text = text
        self.color = color
        self.font_size = font_size
        self.font_type = font_type
        self.life_timer = life_timer
        self.font_object = None
        self.image = None
        self.rect = None
        self.alignment = alignment

        self.build_image()
        self.position = vector.objVector(0,0)
    
    def show(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        # aligment update
        if not(self.life_timer == -1):
            if self.life_timer == 0:
                self.kill()
            self.life_timer -= 1
        
        if self.alignment == TOP_LEFT:
            self.rect.topleft = (self.position.x, self.position.y)
        
        elif self.alignment == TOP_MIDDLE:
            self.rect.midtop = (self.position.x, self.position.y)
        
        elif self.alignment == TOP_RIGHT:
            self.rect.topright = (self.position.x, self.position.y)
        
        elif self.alignment == CENTER_LEFT:
            self.rect.midleft = (self.position.x, self.position.y)
        
        elif self.alignment == CENTER_MIDDLE:
            self.rect.center = (self.position.x, self.position.y)
        
        elif self.alignment == CENTER_RIGHT:
            self.rect.midright = (self.position.x, self.position.y)

        elif self.alignment == BOTTOM_LEFT:
            self.rect.bottomleft = (self.position.x, self.position.y)

        elif self.alignment == BOTTOM_MIDDLE:
            self.rect.midbottom = (self.position.x, self.position.y)

        elif self.alignment == BOTTOM_RIGHT:
            self.rect.bottomright = (self.position.x, self.position.y)
    
    def copy(self):#Copy the object
        new = Text(self.font_type, self.font_size, self.color, self.text, self.life_timer)
        return new

    def build_image(self):
        self.font_object = pygame.font.Font(self.font_type, self.font_size)
        image = self.font_object.render(str(self.text), ANTI_ALIAS, self.color)
        self.image = pygame.Surface(image.get_size(), depth = 24)
        key = COLOR_BLACK
        self.image.fill(key)
        self.image.set_colorkey(key)
        self.image.blit(image, image.get_rect())
        self.rect = self.image.get_rect()
                
    def set_font(self, font_size, color, font_type):
        '''Call this function to reset the font
        '''
        self.color = color
        self.font_type = font_type
        self.font_size = font_size
        self.build_image()
    
    def get_alignment(self):
        return self.alignment
    def set_alignment(self, alignment):
        self.alignment = alignment
    alignment_ = property(get_alignment, set_alignment, None, 'Tp get or set alignmet')

    def set_text(self, text):
        self.text = text
        self.build_image()
    def get_text(self):
        return self.text
    text_ = property(get_text, set_text, None, 'To get or set the text')

    def set_color(self, rgb):
        self.color = rgb[:]
        self.build_image()
    def get_color(self):
        return self.color
    color_ = property(get_color, set_color, None, 'To get or set the color')

    def get_position(self):
        return self.position.x, self.position.y
    def set_position(self, position):
        self.position[:] = position
    position_ = (get_position, set_position, None, 'To get or set the position')



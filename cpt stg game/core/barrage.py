from core.sprite import *
import copy
from typing import List
import math

def load_data():
        """Load data
        
        """
        an = animation.Animation()
        for i in range(1, 9):
            an.build_animation(f'{i}', [f'barrages/barrier{i}'], 0.6)
        Barrage.TYPES["barrier"] = {"id": 0, "animation": an}
        an = animation.Animation()
        for i in range(1, 10):
            an.build_animation(f'{i}', [f'barrages/diamond{i}'], 1.5)
        Barrage.TYPES["diamond"] = {"id": 1, "animation": an}
        an = animation.Animation()
        for i in range(1, 5):
            an.build_animation(f'{i}', [f'barrages/viodball{i}'], 1.25)
        Barrage.TYPES["viodball"] = {"id": 2, "animation": an}
        an = animation.Animation()
        for i in range(1, 6):
            an.build_animation(f'{i}', [f'barrages/ball{i}'], 0.5)
        Barrage.TYPES["ball"] = {"id": 3, "animation": an}
        an = animation.Animation()
        for i in range(1, 10):
            an.build_animation(f'{i}', [f'barrages/square{i}'])
        Barrage.TYPES["square"] = {"id": 4, "animation": an}
        an = animation.Animation()
        for i in range(1, 10):
            an.build_animation(f'{i}', [f'barrages/texturedball{i}'], 1.5)
        Barrage.TYPES["texturedball"] = {"id": 5, "animation": an}
        an = animation.Animation()
        for i in range(1, 8):
            an.build_animation(f'{i}', [f'barrages/bigstar{i}'])
        Barrage.TYPES["bigstar"] = {"id": 6, "animation": an}
        an = animation.Animation()    
        an.build_animation(f'1', [f'barrages/burningballred1', 'barrages/burningballred2', 'barrages/burningballred3', 'barrages/burningballred4'])
        Barrage.TYPES["burningballred"] = {"id": 7, "animation": an}
        an = animation.Animation()    
        an.build_animation(f'1', [f'barrages/burningballblue1', 'barrages/burningballblue2', 'barrages/burningballblue3', 'barrages/burningballblue4'])
        Barrage.TYPES["burningballblue"] = {"id": 8, "animation": an}
        an = animation.Animation()
        for i in range(1, 16):
            an.build_animation(f'{i}', [f'barrages/crystal{i}'])
        Barrage.TYPES["crystal"] = {"id": 9, "animation": an}
        an = animation.Animation()
        for i in range(1, 16):
            an.build_animation(f'{i}', [f'barrages/dart{i}'])
        Barrage.TYPES["dart"] = {"id": 10, "animation": an}
        an = animation.Animation()
        for i in range(1, 16):
            an.build_animation(f'{i}', [f'barrages/laser{i}'], 1.25)
        Barrage.TYPES["laser"] = {"id": 11, "animation": an}
        an = animation.Animation()
        for i in range(1, 16):
            an.build_animation(f'{i}', [f'barrages/star{i}'])
        Barrage.TYPES["star"] = {"id": 12, "animation": an}
        an = animation.Animation()
        for i in range(1, 8):
            an.build_animation(f'{i}', [f'barrages/knife{i}'])
        Barrage.TYPES["knife"] = {"id": 13, "animation": an}
        an = animation.Animation()
        for i in range(1, 6):
            an.build_animation(f'{i}', [f'barrages/ball{i}'])
        Barrage.TYPES["midball"] = {"id": 14, "animation": an}
        


class Barrage(Sprite):#parent
    """Barrage (the bullets)
    
    """

    TYPES = {}

    def __init__(self, parent, type_id: List[str]):
        """The __init__ method for barrage
        Arg:
            parent: the parent function/object this class
            type_id: the id(s) for this type of barrage
        
        """
        super().__init__()
        self.sprite_type = SPRITE_BARRAGE
        self.parent = parent
        self.can_collide = True
        self.bound_style = BOUND_KILL
        self.__type = type_id
        self.type_id = self.TYPES[type_id[0]]['id']
        self.animation = copy.copy(self.TYPES[type_id[0]]['animation'])
        self.animation.set_parent(self)
        self.rect = self.image.get_rect()
        self.hitrect = self.rect
        self.animation.play_animation(type_id[1])
        self.bounds = 0, 0, STAGE_WIDTH_HEIGHT[0], STAGE_WIDTH_HEIGHT[1]
        self.active = False
        self.grazed = False

        self.position = vector.objVector(0, 0)
        self.velocity = vector.objVector(0, 0)

        self.timer = 0
        self.life_time = 2*FRAME_PER_SECOND
        self.speed = 0
        self.phase = 0
        self.scale = 1
        self.phase_list = [self.defualt_motion]

        #set up settings
        self.aim = False
        self.setup_angle = 0
        self.correct_start_position = True
        
        self.custom_messages = None

    def defualt_motion(self, child):
        self.auto_rotate()

    def auto_rotate(self):
        center = self.position.x, self.position.y
        rotated_image = pygame.transform.rotate(self.image, self.velocity.angle)
        self.rect = rotated_image.get_rect(center=center)
        self.image = rotated_image

    def rotate(self, angle):
        center = self.position.x, self.position.y
        rotated_image = pygame.transform.rotate(self.image, angle)
        self.rect = rotated_image.get_rect(center=center)
        self.image = rotated_image

    def set_up(self):
        self.active = True

        if self.aim:    
            self.aimming()

        if self.correct_start_position:
            self.position = self.parent.position
        
        self.velocity.angle += self.setup_angle
           
        self.custom_setup(self)

    def custom_setup(self, child):
        pass

    def custom_update(self):
        self.phase_list[self.phase](self)
        self.timer += 1


    def collide(self):
        self.die()
    
    def aimming(self):
        self.velocity = self.parent.parent.player.position - self.parent.position
        self.velocity.norm = self.speed
        

    def copy(self) -> object:
        b = Barrage(self.parent, self.__type)
        b.position = self.position
        b.velocity = self.velocity
        b.speed = self.speed
        b.acceleration = self.acceleration
        b.bounds = self.bounds
        b.active = self.active
        
        return b


    @staticmethod
    def motion_laser(child):

        if child.timer < 0.7*FRAME_PER_SECOND:
            child.scale = 0.1
            child.width = child.image.get_width()

            new_width = child.width*0.1
            center = child.position.x, child.position.y
            rescaled = pygame.transform.scale(child.image, (int(new_width), child.height))
            child.rect = child.hitrect = rescaled.get_rect(center=center)
            child.image = rescaled
            child.can_collide = False
            child.rotate((child.position - child.parent.position).angle)

        
        elif 1.2*FRAME_PER_SECOND  > child.timer >= 0.7*FRAME_PER_SECOND:
            new_width = child.width * child.scale
            child.scale += 0.06
            center = child.position.x, child.position.y
            rescaled = pygame.transform.scale(child.image, (int(new_width), child.height))
            child.rect = child.hitrect = rescaled.get_rect(center=center)
            child.image = rescaled
            child.rotate((child.position - child.parent.position).angle)

        elif child.timer >= FRAME_PER_SECOND*1.2:
            child.can_collide = True
            center = child.position.x, child.position.y
            rescaled = pygame.transform.scale(child.image, (child.image.get_width(), child.height))
            child.rect = child.hitrect = rescaled.get_rect(center=center)
            child.image = rescaled
            child.rotate((child.position - child.parent.position).angle)

        
        if  child.timer >= child.life_time:
            new_width = child.width * child.scale
            child.scale -= 0.06
            center = child.position.x, child.position.y
            rescaled = pygame.transform.scale(child.image, (int(new_width), child.height))
            child.rect = child.hitrect = rescaled.get_rect(center=center)
            child.image = rescaled
            child.rotate((child.position - child.parent.position).angle)


        if child.timer >= child.life_time + 0.5*FRAME_PER_SECOND:
            child.die()
            
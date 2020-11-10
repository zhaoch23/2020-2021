from core.effect import *

class BossBack001(Effect):

    def __init__(self, parent, type_id=['bossback', '1']): # init
        super().__init__(parent, type_id=type_id)
        self.expand = True

    def custom_update(self):
        self.rescale()
        self.rotate(self.rotate_angle)
        self.rotate_angle -= 1
        self.position = self.parent.position
        if self.expand:
            self.scale += 0.01
        else:
            self.scale -= 0.01
        
        if self.scale < 1:
            self.expand = True
        elif self.scale > 2:
            self.expand = False
    
    def rescale(self):
        center = self.position.x, self.position.y
        scaled_image = pygame.transform.rotozoom(self.image, 1, self.scale)
        self.rect = scaled_image.get_rect(center=center)
        self.image = scaled_image

    def rotate(self, angle):
        center = self.position.x, self.position.y
        rotated_image = pygame.transform.rotate(self.image, angle)
        self.rect = rotated_image.get_rect(center=center)
        self.image = rotated_image


class BossBack002(Effect):

    def __init__(self, parent, type_id=['bossback','2']):
        super().__init__(parent, type_id=type_id)
        self.rotate_angle = 20
        self.scale = 1.3
        

    def custom_update(self):
        self.rescale()
        self.position = self.parent.position
        self.rotate(self.rotate_angle)
        self.rotate_angle += 1

    def rescale(self):
        center = self.position.x, self.position.y
        scaled_image = pygame.transform.rotozoom(self.image, 1, self.scale)
        self.rect = scaled_image.get_rect(center=center)
        self.image = scaled_image

    def rotate(self, angle):
        center = self.position.x, self.position.y
        rotated_image = pygame.transform.rotate(self.image, angle)
        self.rect = rotated_image.get_rect(center=center)
        self.image = rotated_image


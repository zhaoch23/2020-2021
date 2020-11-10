from core.effect import *

class DeathEffect(Effect):

    def __init__(self, parent, type_id=['circle','3']): # init
        super().__init__(parent, type_id=type_id)
        self.dim = 20
    
    def custom_update(self): # animation update
        super().custom_update()
        self.rescale()
        self.scale += 0.5
        self.dim += 60
        if self.timer >= 0.1*FRAME_PER_SECOND:
            self.die()
    
    def rescale(self): # animation of death
        center = self.position.x, self.position.y
        scaled_image = pygame.transform.rotozoom(self.image, 1, self.scale)
        self.rect = scaled_image.get_rect(center=center)
        self.image = scaled_image

        #dim = pygame.Surface(self.image.get_size())
        #dim.fill((0,0,0))
        #dim.set_colorkey((0,0,0))
        #dim.set_alpha(self.dim)
        #self.image.blit(dim, self.image.get_rect())

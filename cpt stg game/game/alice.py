from core.player import *
from core import bullet

def load_data():
    # load data
    Alice.ALICE_ANIMATION_LIST.build_animation('left', ['alice/alice1', 'alice/alice2', 'alice/alice3'], dim_value=254)
    Alice.ALICE_ANIMATION_LIST.build_animation('idle', ['alice/alice4', 'alice/alice5', 'alice/alice6'], dim_value=254)
    Alice.ALICE_ANIMATION_LIST.build_animation('right', ['alice/alice7', 'alice/alice8', 'alice/alice9'], dim_value=254)

class Alice(Player):

    ALICE_ANIMATION_LIST = animation.Animation()
    SOUND_EFFECT_LIST = []

    def __init__(self, parent):
        # init and settings
        super().__init__(parent)

        self.animation = copy.copy(self.ALICE_ANIMATION_LIST)
        self.animation.set_parent(self)
        self.animation.play_animation('idle')
        self.rect = self.image.get_rect()
        self.hitrect = pygame.Rect(0, 0, 1, 1)
        self.animation.play_dt = 5

        self.name = ALICE
        self.life = 2
        self.point = 0
        self.power = 0
        self.fire_cold_down = FRAME_PER_SECOND/30
        self.fast_speed = 300*MEASURE_UNIT
        self.slow_speed = 100*MEASURE_UNIT
        self.speed = self.fast_speed
        self.slow_mode = False
        self.invlnerable = False
        self.dead = False
        self.bullet_types = []

        

    def show(self, screen):
        # slow mode
        surface = pygame.Surface((5, 5))
        surface.fill((239, 124, 124))
        screen.blit(self.image, self.rect)

        
        if self.slow_mode:
            screen.blit(surface, self.hitrect)

    def custom_update(self):
        # power and fire cold down update
        super().custom_update()

        if self.power >= 1.00:
            self.fire_mode = 1
        else:
            self.fire_mode == 0

        if self.fire_cold_down > 0:
            self.fire_cold_down -= 1

    def fire(self):
        '''
        player shooting. including bullets and bomb
        as power increases, the bullets from player will enhances. 
        max enhences will applies when power = 4
        '''
        if not self.fire_cold_down:
            if 0 <= self.power:
                b = bullet.Bullet(self.parent, 'flow1')
                b.position = self.position
                b.damage = 2
                b.velocity = vector.objVector(0, -2000*MEASURE_UNIT)
                
                self.parent.bullet_group.add(b)

            if 1 <= self.power:
                b1 = bullet.Bullet(self.parent, 'track1')
                b1.position = self.position + vector.objVector(-30, 100)
                b1.damage = 0.2
                b1.velocity = vector.objVector(0, -2000*MEASURE_UNIT)
                b2 = bullet.Bullet(self.parent, 'track1')
                b2.position = self.position + vector.objVector(20, 100)
                b2.damage = 0.2
                b2.velocity = vector.objVector(0, -2000*MEASURE_UNIT)
                self.parent.bullet_group.add(b1)
                self.parent.bullet_group.add(b2)

                
            if 2 <= self.power:
                b1 = bullet.Bullet(self.parent, 'track2')
                b1.position = self.position + vector.objVector(-50, 100)
                b1.damage = 0.3
                b1.velocity = vector.objVector(0, -2000*MEASURE_UNIT)
                b2 = bullet.Bullet(self.parent, 'track2')
                b2.position = self.position + vector.objVector(40, 100)
                b2.damage = 0.3
                b2.velocity = vector.objVector(0, -2000*MEASURE_UNIT)
                self.parent.bullet_group.add(b1)
                self.parent.bullet_group.add(b2)


            if 3 <= self.power:
                b1 = bullet.Bullet(self.parent, 'flow1')
                b1.position = self.position + vector.objVector(20, 0)
                b1.damage = 1
                b1.velocity = vector.objVector(0, -2000*MEASURE_UNIT)
                b2 = bullet.Bullet(self.parent, 'flow1')
                b2.position = self.position + vector.objVector(-20, 0)
                b2.damage = 1
                b2.velocity = vector.objVector(0, -2000*MEASURE_UNIT)
                self.parent.bullet_group.add(b1)
                self.parent.bullet_group.add(b2)
            
            if 4 <= self.power:
                b = bullet.Bullet(self.parent, 'flow2')
                b.position = self.position+ vector.objVector(0, -30)
                b.damage = 0.5
                b.velocity = vector.objVector(0, -3000*MEASURE_UNIT)
                self.parent.bullet_group.add(b)

        

            self.fire_cold_down = FRAME_PER_SECOND/15


from core.enemy import *

class Example(Enemy):

    def __init__(self, parent): # Type class.Game
        super().__init__(parent)
        self.position = vector.objVector(0, 0)
        self.bounds = -50, -50, STAGE_WIDTH_HEIGHT[0]+50, STAGE_WIDTH_HEIGHT[1]+50
        self.health = 10

        self.phase_list = [self.phase_one, self.phase_two]
        self.phase = 0

        self.fire_pattern = [self.fire_1]
        self.fire = 0

    def phase_one(self, child):
        self.velocity = vector.objVector(0, 100*MEASURE_UNIT)
        if self.phase_timer == 2*FRAME_PER_SECOND:
            self.fire_pattern[self.fire](self)
            self.velocity = vector.objVector(0, 0)
        if self.phase_timer == 3*FRAME_PER_SECOND:
            self.phase += 1
    
    def phase_two(self, child):
        self.velocity = vector.objVector(0, -100*MEASURE_UNIT)

    def fire_1(self, child):
        Enemy.defualt_danmaku_pattern_005(child)
    



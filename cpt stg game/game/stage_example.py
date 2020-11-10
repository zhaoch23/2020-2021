from core.game import *
from core import barrage, enemy
from game.enemy import example
import random
import math

'''
THIS STAGE IS ONLY FOR DEMOSTRATION
IT IS NOT A PART OF THE GAME
'''

sin = math.sin
cos = math.cos
pi = math.pi

class StageExample(Game):

    def __init__(self, screen, p=None):
        super().__init__(screen, p=p)

        self.phase_list = [self.phase_zero, self.phase_one]
        self.phase = 0

    def phase_zero(self):
        if self.timer % 240 == 0:
            self.add_a_sprite()
            self.phase += 1
    
    def phase_one(self):
        #print(self.clock.get_fps())
        pass

    def add_a_sprite(self):
        new = example.Example(self)
        new.position = vector.objVector(STAGE_WIDTH_HEIGHT[0]/2, 0)
        new.fire_pattern = [self.custum_fire]

        self.enemy_group.add(new)

    def custum_fire(self, child): # 早苗🌟弹
        time = child.timer
        distance = 6
        radius = 100 # 半径

        #start
        sx = child.position[0]
        sy = child.position[1] - radius
        sangle = pi/5/2 + pi/2

        delta_time = 0
        sst = 0

        while sst <= 4:
            i = 0
            while True:
                delta_time += 0.5
                sx += cos(sangle)*distance
                sy += sin(sangle)*distance
                
                if (sx - child.position[0])**2 + (sy - child.position[1])**2 > radius*radius:
                    sst += 1
                    sangle -= (pi - pi/5)
                    break
                
                for j in range(5):
                    new = barrage.Barrage(child, ['ball', str(j+1)])
                    new.position = vector.objVector(sx, sy)
                    new.correct_start_position = False
                    new.phase_list = [self.custom_fire_update]
                    
                    new.custom_messages = {"start_angle": math.degrees(pi - 2*pi/5*j), "base_angle": math.degrees(sangle - pi + pi/20*i), "delay": int(delta_time)}
                    try:
                        child.fire_pattern_temp[time + int(delta_time)].append(new)
                    except:
                        child.fire_pattern_temp[time + int(delta_time)] = []
                        child.fire_pattern_temp[time + int(delta_time)].append(new)
                i += 1
        
    def custom_fire_update(self, child):
        if child.timer + child.custom_messages["delay"] == 4*FRAME_PER_SECOND:
            child.velocity = vector.objVector(200*MEASURE_UNIT,0)
            child.velocity.angle = child.custom_messages["start_angle"]
        elif 5*FRAME_PER_SECOND > child.timer + child.custom_messages["delay"] > 4*FRAME_PER_SECOND:
            child.velocity.norm = child.velocity.norm - 2.5*MEASURE_UNIT
        elif child.timer + child.custom_messages["delay"] >= 5*FRAME_PER_SECOND:
            child.velocity.angle = child.custom_messages["base_angle"]

from core.game import *
from core.enemy import *
from utils import utility
from data.music import *
from game import stage_two
import pygame
import random
import math

'''
This is stage_1, in order to pass this stage player needs to survive 60 seconds
There are two phases in this stage, in each stage three types of minion will spawned.
player needs to survive from enemy's barrage, and go to next stage.
'''

def load_data(): # load background music
    m = utility.load_music('Kanata')
    StageOne.MUSIC['kanata'] = m

class StageOne(Game):

    MUSIC = {}

    def __init__(self, screen, p: int = None): # init the stage
        super().__init__(screen, p)


        self.phase_list = [self.phase_0, self.phase_1, self.phase_2]
        self.player.fast_speed = 250*MEASURE_UNIT
        utility.play_music(self.MUSIC['kanata'])

    def speed_bonus(self, time):
        '''
        RECURSION
        '''
        # Recursion for speed boosting
        if time == 30*FRAME_PER_SECOND:
            return 0

        self.player.fast_speed = self.player.fast_speed + 500*MEASURE_UNIT
        self.speed_bonus(time + 1*FRAME_PER_SECOND)


    def sort_list(fire):
        '''
        BUBBLE SORT
        '''
        switch = True
        while switch:
            for i in range(len(fire) - 1):
                if fire[i] > fire[i + 1]:
                    fire[i], fire[i + 1] = fire[i + 1], fire[i]
                i = i + 1


    def search_list(fire):
        '''
        SEARCHING
        '''
        for i in range(len(fire)):
            if fire[i] == fire_pattern:
                return i
        return 0



    def minion_spawn_1(self): # This is spawntion of minion_1
        minion = Enemy(self)
        minion.phase_list = [self.motion_1]
        minion.fire_pattern = [self.fire_1]
        minion.position = vector.objVector(600, 50)
        minion.health = 20
        self.enemy_group.add(minion)

    def minion_spawn_2(self): # This is spawntion of minion_2
        minion = Enemy(self, type_id='mess1')
        minion.phase_list = [self.motion_2]
        minion.fire_pattern = [self.fire_2]
        minion.position = vector.objVector(325, 0)
        minion.health = 20
        self.enemy_group.add(minion)

    def minion_spawn_3(self): # This is spawntion of minion_3
        minion = Enemy(self, type_id='bluesprite')
        minion.phase_list = [self.motion_3]
        minion.fire_pattern = [self.fire_5]
        minion.position = vector.objVector(0, 200)
        minion.health = 20
        self.enemy_group.add(minion)

    def minion_spawn_4(self): # This is spawntion of minion_4
        minion = Enemy(self)
        minion.phase_list = [self.motion_4]
        minion.fire_pattern = [self.fire_4]
        minion.position = vector.objVector(0, 600)
        minion.health = 20
        self.enemy_group.add(minion)

    def minion_spawn_5(self): # This is spawntion of minion_5
        minion = Enemy(self, type_id='bluesprite')
        minion.phase_list = [self.motion_5]
        minion.fire_pattern = [self.fire_3]
        minion.position = vector.objVector(560, 600)
        minion.health = 20
        self.enemy_group.add(minion)


    def motion_1(self, child): # This is motion of minion_1
        if child.phase_timer == 0:
            child.velocity = vector.objVector(-100 * MEASURE_UNIT, 1)
        elif 2*FRAME_PER_SECOND > child.phase_timer > 0:
            child.acceleration = vector.objVector(-20 * MEASURE_UNIT ** 2, 5 * MEASURE_UNIT ** 2)
        elif child.phase_timer == 2.1*FRAME_PER_SECOND:
            child.fire_pattern[child.fire](child)
        else:
            child.velocity = vector.objVector(150 * MEASURE_UNIT, 5)
            child.acceleration = vector.objVector(50 * MEASURE_UNIT ** 2, -50 * MEASURE_UNIT ** 2)


    def motion_2(self, child): # This is motion of minion_2
        if child.phase_timer == 0:
            child.velocity = vector.objVector(0, 100 * MEASURE_UNIT)
        elif 1.5*FRAME_PER_SECOND > child.phase_timer > 0:
            child.acceleration = vector.objVector(0, 50 * MEASURE_UNIT ** 2)
        elif child.phase_timer == 1.6*FRAME_PER_SECOND:
            child.fire_pattern[child.fire](child)
        else:
            child.velocity = vector.objVector(-150 * MEASURE_UNIT, 5)
            child.acceleration = vector.objVector(-50 * MEASURE_UNIT ** 2, 100 * MEASURE_UNIT ** 2)


    def motion_3(self, child): # This is motion of minion_3
        if child.phase_timer == 0:
            child.velocity = vector.objVector(100 * MEASURE_UNIT, 0)
        if 2*FRAME_PER_SECOND >= child.phase_timer:
            child.velocity = vector.objVector(150 * MEASURE_UNIT, 0)
        elif child.phase_timer == 2.1*FRAME_PER_SECOND:
            child.fire_pattern[child.fire](child)
        else:
            child.velocity = vector.objVector(80 * MEASURE_UNIT, 0)

    def motion_4(self, child): # This is motion of minion_4
        if child.phase_timer == 0:
            child.velocity = vector.objVector(0, 0)
        if 2 * FRAME_PER_SECOND >= child.phase_timer:
            child.velocity = vector.objVector(150 * MEASURE_UNIT, -200 * MEASURE_UNIT)
        elif child.phase_timer == 2.1 * FRAME_PER_SECOND:
            child.fire_pattern[child.fire](child)
        else:
            child.velocity = vector.objVector(100 * MEASURE_UNIT, 0)

    def motion_5(self, child): # This is motion of minion_5
        if child.phase_timer == 0:
            child.velocity = vector.objVector(0, 0)
        if 2 * FRAME_PER_SECOND >= child.phase_timer:
            child.velocity = vector.objVector(-150 * MEASURE_UNIT, -200 * MEASURE_UNIT)
        elif child.phase_timer == 2.1 * FRAME_PER_SECOND:
            child.fire_pattern[child.fire](child)
        else:
            child.velocity = vector.objVector(-100 * MEASURE_UNIT, 0)


    def fire_1(self, child): # This is fire pattern of minion_1
        Enemy.defualt_danmaku_pattern_001(child)

    def fire_2(self, child): # This is fire pattern of minion_2
        Enemy.defualt_danmaku_pattern_002(child)

    def fire_3(self, child): # This is fire pattern of minion_3
        Enemy.defualt_danmaku_pattern_003(child)

    def fire_4(self, child): # This is fire pattern of minion_4
        Enemy.defualt_danmaku_pattern_004(child)

    def fire_5(self, child): # This is fire pattern of minion_5
        Enemy.defualt_danmaku_pattern_005(child)


    def phase_0(self):
        '''
        This is phase_o, it will preset at first 3 second when player enter the stage.
        In this stage, no enemy will be spawned.
        However, caption will show in the centre of stage that "Presented by Yuhan Xiang"
        After 3 seconds, stage will enter phase_1.
        '''
        if self.timer == 1:
            title1 = text.Text(ENG_FONT_PATH, 24, (255, 255, 255), 'Presented by Yuhan Xiang')
            title1.position = vector.objVector(STAGE_WIDTH_HEIGHT[0] / 2, STAGE_WIDTH_HEIGHT[1] / 3 + 100)
            title1.life_timer = 5 * FRAME_PER_SECOND
            self.effect_group.add(title1)

        elif self.timer == 3 * FRAME_PER_SECOND:
            self.next_phase()


    def phase_1(self):
        '''
        This is phase_1, it will present at first 30 second when player enter this phase.
        In this phase, minion_1, minion_2, minion_3 will be spawned.
        after 30 second, stage will enter phase_2.
        '''
        if self.timer <= 30*FRAME_PER_SECOND:
            if self.timer % 40 == 0 and self.timer % 5 == 0:
                self.minion_spawn_1()
            elif self.timer % 30 == 0:
                self.minion_spawn_2()
            elif self.timer % 50 == 0 and self.timer % 10 == 0:
                self.minion_spawn_3()
        else:
            self.next_phase()



    def phase_2(self):
        '''
        This is phase_2, it will present immediately after phase_1.
        In this phase, minion_2, minion_4, minion_5 will be spawned.
        after 30 second, stage will end.
        '''
        if self.timer <= 30*FRAME_PER_SECOND:
            if self.timer % 30 == 0 and self.timer % 90 == 0:
                self.minion_spawn_4()
            elif self.timer % 60 == 0 and self.timer % 40 == 0:
                self.minion_spawn_5()
            elif self.timer % 50 == 0 and self.timer % 10 == 0:
                self.minion_spawn_2()
        else:
            return stage_two.StageTwo(self.screen, self.player).run()

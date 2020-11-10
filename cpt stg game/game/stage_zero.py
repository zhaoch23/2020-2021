from core.game import *
from game.enemy import stage_zero_margatriod
from core import barrage, enemy, boss, item
from effect import death_effect, bossback
from game import stage_one
import random
import math

sin = math.sin
cos = math.cos
pi = math.pi

def load_data(): # load background music
    b = utility.load_music('bgm')
    StageZero.MUSIC['bgm'] = b

class StageZero(Game):
    """First level in the game
    self.phase_list: a list of phases
    self.player.power: player's power
    
    """

    MUSIC = {}

    def __init__(self, screen, p=None):
        super().__init__(screen, p=p)

        self.phase_list = [self.phase_000, self.phase_001, self.phase_002, self.phase_003, self.phase_004, self.phase_005, self.phase_005, self.phase_006] # a list involves all phases
        self.player.power = 0
        self.player.testing = False
        #utility.play_music(self.MUSIC['bgm'])


    def phase_000(self):
        """Information
        
        """
        if self.timer == 1:
            title1 = text.Text(JAP_FONT_PATH, 36, (255,255,255), '人形ソカイの夜')
            title1.position = vector.objVector(STAGE_WIDTH_HEIGHT[0]/2, STAGE_WIDTH_HEIGHT[1]/3)
            title1.life_timer = 5*FRAME_PER_SECOND
            title2 = text.Text(ENG_FONT_PATH, 24, (255,255,255), 'Presented by Chengzong')
            title2.position = vector.objVector(STAGE_WIDTH_HEIGHT[0]/2, STAGE_WIDTH_HEIGHT[1]/3 + 100)
            title2.life_timer = 5*FRAME_PER_SECOND
            self.effect_group.add(title1)
            self.effect_group.add(title2)
        
        elif self.timer == 3*FRAME_PER_SECOND:
            self.next_phase()

    def phase_001(self):
        """Create enemy sprites at the correct timing
        bounds: the place of invincible wall
        position: the location of the enemy
        fire_pattern: the type of bullet pattern
        
        """
        if self.timer == 3*FRAME_PER_SECOND or self.timer == 4*FRAME_PER_SECOND:
            for i in range(3):
                for j in range(2):
                    new = enemy.Enemy(self, 'bluesprite')
                    new.bounds = -50, -1000, STAGE_WIDTH_HEIGHT[0] + 50, STAGE_WIDTH_HEIGHT[1] + 50
                    new.position.x = STAGE_WIDTH_HEIGHT[0]*0.75 + 50*j
                    new.position.y = 0 - 40*i
                    new.fire_pattern = [self.fire_001_00]
                    new.phase_list = [self.motion_001_00]

                    i1 = item.Item(self, 'power')
                    new.item_list = [i1] 

                    self.enemy_group.add(new)
        
        if 12*FRAME_PER_SECOND >= self.timer > 4*FRAME_PER_SECOND and self.timer%(2*FRAME_PER_SECOND) == 0:
            for i in range(2):
                new = enemy.Enemy(self, 'greensprite')
                new.bounds = -50, -1000, STAGE_WIDTH_HEIGHT[0] + 50, STAGE_WIDTH_HEIGHT[1] + 50
                new.position.x = random.randrange(50, STAGE_WIDTH_HEIGHT[0]-50)
                new.position.y = 0
                new.fire_pattern = [self.fire_002_00]
                new.phase_list = [self.motion_002_00]
                new.health = 5

                i1 = item.Item(self, 'power')
                i2 = item.Item(self, 'point')
                i3 = item.Item(self, 'point')
                new.item_list = [i1, i2, i3] 

                self.enemy_group.add(new)
        
        if 9.5*FRAME_PER_SECOND > self.timer >= 8*FRAME_PER_SECOND and self.timer%(0.3*FRAME_PER_SECOND) == 0:
            new = enemy.Enemy(self, 'mess2')
            new.position.x = 0
            new.position.y = STAGE_WIDTH_HEIGHT[1]*0.2
            new.fire_pattern = [self.fire_003_00]
            new.phase_list = [self.motion_003_00]
            i1 = item.Item(self, 'power')
            i2 = item.Item(self, 'point')
            i3 = item.Item(self, 'point')
            new.item_list = [i1, i2, i3] 
            new.rotating = True
            self.enemy_group.add(new)
        if 10.5*FRAME_PER_SECOND > self.timer >= 9*FRAME_PER_SECOND and self.timer%(0.3*FRAME_PER_SECOND) == 0:
            new = enemy.Enemy(self, 'mess2')
            new.position.x = STAGE_WIDTH_HEIGHT[0]
            new.position.y = STAGE_WIDTH_HEIGHT[1]*0.2
            new.fire_pattern = [self.fire_003_00]
            new.phase_list = [self.motion_003_01]
            i1 = item.Item(self, 'power')
            i2 = item.Item(self, 'point')
            i3 = item.Item(self, 'point')
            new.item_list = [i1, i2, i3] 
            new.rotating = True
            self.enemy_group.add(new)   
        if 12.5*FRAME_PER_SECOND > self.timer >= 11*FRAME_PER_SECOND and self.timer%(0.3*FRAME_PER_SECOND) == 0:
            new = enemy.Enemy(self, 'mess2')
            new.position.x = STAGE_WIDTH_HEIGHT[0]
            new.position.y = STAGE_WIDTH_HEIGHT[1]*0.2
            new.fire_pattern = [self.fire_003_00]
            new.phase_list = [self.motion_003_01]
            i1 = item.Item(self, 'power')
            i2 = item.Item(self, 'point')
            i3 = item.Item(self, 'point')
            new.item_list = [i1, i2, i3] 
            new.rotating = True
            self.enemy_group.add(new)  
        if 13.5*FRAME_PER_SECOND > self.timer >= 12*FRAME_PER_SECOND and self.timer%(0.3*FRAME_PER_SECOND) == 0:
            new = enemy.Enemy(self, 'mess2')
            new.position.x = 0
            new.position.y = STAGE_WIDTH_HEIGHT[1]*0.2
            new.fire_pattern = [self.fire_003_00]
            new.phase_list = [self.motion_003_00]
            i1 = item.Item(self, 'power')
            i2 = item.Item(self, 'point')
            i3 = item.Item(self, 'point')
            new.item_list = [i1, i2, i3] 
            new.rotating = True
            self.enemy_group.add(new)
        if 14.5*FRAME_PER_SECOND > self.timer >= 13*FRAME_PER_SECOND and self.timer%(0.5*FRAME_PER_SECOND) == 0:
            for i in range(10):
                new = enemy.Enemy(self, 'bluesprite')
                new.bounds = -50, -1000, STAGE_WIDTH_HEIGHT[0] + 50, STAGE_WIDTH_HEIGHT[1] + 50
                new.position.x = random.randrange(50, STAGE_WIDTH_HEIGHT[0]-50)
                new.position.y = random.randrange(-20, 0)
                new.velocity = vector.objVector(0, 200*MEASURE_UNIT)
                new.acceleration = vector.objVector(0, -2.5*MEASURE_UNIT)
                new.fire_pattern = [self.fire_003_00]
                new.phase_list = [self.motion_001_01]
                new.health = 2

                i1 = item.Item(self, 'power')
                new.item_list = [i1] 

                self.enemy_group.add(new)

        if 20*FRAME_PER_SECOND > self.timer >= 15*FRAME_PER_SECOND and self.timer%(1.5*FRAME_PER_SECOND) == 0:

                def generate_mob(position):
                    if position <= STAGE_WIDTH_HEIGHT[0]:
                        new = enemy.Enemy(self, 'bluesprite')
                        new.bounds = -50, -1000, STAGE_WIDTH_HEIGHT[0] + 50, STAGE_WIDTH_HEIGHT[1] + 50
                        new.position.x = position
                        new.position.y = 0
                        new.velocity = vector.objVector(0, 200*MEASURE_UNIT)
                        new.acceleration = vector.objVector(0, -2.5*MEASURE_UNIT)
                        new.fire_pattern = [self.fire_003_01]
                        new.phase_list = [self.motion_001_01]
                        new.health = 2

                        i1 = item.Item(self, 'power')
                        new.item_list = [i1] 

                        self.enemy_group.add(new)
                        return generate_mob(position + 80)

                    else:
                        return ''
                
                generate_mob(5)

        if 20*FRAME_PER_SECOND == self.timer:
            self.next_phase()
        
    def phase_002(self):
        """Phase two of the stage
        timer: the timer used to count frames player spend in this phase
        stage_zero_margatriod: the boss of this stage
        
        """
        if self.timer == 1:
            for e in self.enemy_group.sprites():
                e.die()
            for b in self.barrage_group.sprites():
                d = item.Item(self, "smallpoint")
                d.position = b.position
                b.die()
                self.item_group.add(d)
            for i in self.item_group.sprites():
                i.collected = True

            b = stage_zero_margatriod.Margatriod001(self)
            self.boss_group.add(b)
        
        if self.timer > 1 and not self.boss_group.sprites():
            self.next_phase()
    
    def phase_003(self):
        """Third phase of the stage
        velocity: the variable used to control object movement
        acceleration: object acceleration
        
        """
        if 10*FRAME_PER_SECOND > self.timer and self.timer % (0.5*FRAME_PER_SECOND) == 0:
            for i in range(3):
                new = enemy.Enemy(self, 'bluesprite')
                new.bounds = -50, -50, STAGE_WIDTH_HEIGHT[0] + 50, STAGE_WIDTH_HEIGHT[1] + 50
                new.position.x = random.randrange(50, STAGE_WIDTH_HEIGHT[0]-50)
                new.position.y = random.randrange(-20, 0)
                new.velocity = vector.objVector(0, 200*MEASURE_UNIT)
                new.acceleration = vector.objVector(0, -2.5*MEASURE_UNIT)
                new.fire_pattern = [self.fire_003_02]
                new.phase_list = [self.motion_001_02]
                new.health = 3  
                if random.randint(0, 3) == 3:
                    i1 = item.Item(self, 'power')
                    new.item_list = [i1] 
                else:
                    new.item_list = [] 
                self.enemy_group.add(new)

            for i in range(2):
                new = enemy.Enemy(self, 'yellowsprite')
                new.bounds = -5, -30, STAGE_WIDTH_HEIGHT[0] + 5, STAGE_WIDTH_HEIGHT[1] + 5
                new.position.x = random.randrange(50, STAGE_WIDTH_HEIGHT[0]-50)
                new.position.y = random.randrange(-20, 0)
                new.velocity = vector.objVector(0, 200*MEASURE_UNIT)
                new.acceleration = vector.objVector(0, -2.5*MEASURE_UNIT)
                new.fire_pattern = [self.fire_003_03, self.fire_003_04]
                new.phase_list = [self.motion_001_03]
                new.health = 5
                if random.randint(0, 3) == 3:
                    i1 = item.Item(self, 'largepower')
                    new.item_list = [i1] 
                else:
                    new.item_list = [] 
                self.enemy_group.add(new)

        elif self.timer >= 10*FRAME_PER_SECOND  and self.timer%(0.5*FRAME_PER_SECOND) == 0:
            for i in range(6):
                new = enemy.Enemy(self, 'bluesprite')
                new.bounds = -50, -30, STAGE_WIDTH_HEIGHT[0] + 50, STAGE_WIDTH_HEIGHT[1] + 50
                new.position.x = random.randrange(50, STAGE_WIDTH_HEIGHT[0]-50)
                new.position.y = random.randrange(-20, 0)
                new.velocity = vector.objVector(0, 200*MEASURE_UNIT)
                new.acceleration = vector.objVector(0, -2.5*MEASURE_UNIT)
                new.fire_pattern = [self.fire_003_05]
                new.phase_list = [self.motion_001_01]
                new.health = 2

                if random.randint(0, 3) == 3:
                    i1 = item.Item(self, 'point')
                    new.item_list = [i1] 
                else:
                    new.item_list = [] 
                self.enemy_group.add(new)
        
        if self.timer == 18*FRAME_PER_SECOND:
            self.next_phase()

    def phase_004(self):
        """Phase four of the stage
        
        """
        if self.timer == 1:
            for e in self.enemy_group.sprites():
                e.die()
            for b in self.barrage_group.sprites():
                d = item.Item(self, "smallpoint")
                d.position = b.position
                b.die()
                self.item_group.add(d)
            for i in self.item_group.sprites():
                i.collected = True

            b = stage_zero_margatriod.Margatriod002(self)
            self.boss_group.add(b)
    
    def summon_a_list(self, bias=0):
        for i in range(8):
                new = enemy.Enemy(self, 'bluesprite')
                new.bounds = 0, -30, STAGE_WIDTH_HEIGHT[0], STAGE_WIDTH_HEIGHT[1]
                new.position.x = 72*i + bias
                new.position.y = random.randrange(-20, 0)
                new.velocity = vector.objVector(0, 200*MEASURE_UNIT)
                new.acceleration = vector.objVector(0, -2.5*MEASURE_UNIT)
                new.fire_pattern = [self.fire_003_05]
                new.phase_list = [self.motion_001_01]
                new.health = 2

                if random.randint(0, 3) == 3:
                    i1 = item.Item(self, 'point')
                    new.item_list = [i1] 
                else:
                    new.item_list = [] 
                self.enemy_group.add(new)
    
    """Summon
    The boss will summon some enemies during the battle
    
    """

    def summon_a_list2(self, bias=0):
        for i in range(8):
                new = enemy.Enemy(self, 'yellowsprite')
                new.bounds = 0, -30, STAGE_WIDTH_HEIGHT[0], STAGE_WIDTH_HEIGHT[1]
                new.position.x = 72*i + bias
                new.position.y = random.randrange(-20, 0)
                new.velocity = vector.objVector(0, 200*MEASURE_UNIT)
                new.acceleration = vector.objVector(0, -2.5*MEASURE_UNIT)
                new.fire_pattern = [self.fire_004]
                new.phase_list = [self.motion_001_04]
                new.health = 2
                r = random.randint(0, 4)
                if r == 3:
                    i1 = item.Item(self, 'point')
                    new.item_list = [i1] 
                elif r == 4: 
                    i1 = item.Item(self, 'power')
                    new.item_list = [i1] 
                else:
                    new.item_list = [] 
                self.enemy_group.add(new)
        
    def summon_special(self, start, end, *args):
        new = enemy.Enemy(self, 'bluesprite')
        back_effect = bossback.BossBack002(new)
        back_effect.scale = 0.5
        new.effect_group.add(back_effect)
        self.effect_group.add(back_effect)
        new.position = start
        new.start = start
        new.end = end
        new.speed = 250*MEASURE_UNIT
        new.fire_pattern = [*args]
        new.phase_list = [self.motion_004]
        new.health = 60

        i1 = item.Item(self, 'largepower')
        new.item_list.append(i1)
        self.enemy_group.add(new)

    def summon_special2(self, start, end, *args):
        new = enemy.Enemy(self, 'bluesprite')
        back_effect = bossback.BossBack002(new)
        back_effect.scale = 0.5
        new.effect_group.add(back_effect)
        self.effect_group.add(back_effect)
        new.position = start
        new.start = start
        new.end = end
        new.speed = 250*MEASURE_UNIT
        new.fire_pattern = [*args]
        new.phase_list = [self.motion_004]
        new.health = 60

        i1 = item.Item(self, 'life')
        new.item_list.append(i1)
        self.enemy_group.add(new)
        
    """
    def phase_005(self):
        if self.timer == 60:
            b = boss.Boss(self)
            b.position = vector.objVector(STAGE_WIDTH_HEIGHT[0]/2, 50)
            b.fire_pattern = [self.myon_fire, self.star_fire]
            self.boss_group.add(b)
    """
    
    def phase_005(self):
        """The fifth phase of the stage
        
        """
        if (24*FRAME_PER_SECOND > self.timer > 12*FRAME_PER_SECOND or 10*FRAME_PER_SECOND > self.timer > 0) and self.timer % (0.5*FRAME_PER_SECOND) == 0:
            if random.randint(0, 1):
                self.summon_a_list(random.randint(0, 76))
            else:
                for i in range(4):
                    new = enemy.Enemy(self, 'yellowsprite')
                    new.bounds = -5, -10, STAGE_WIDTH_HEIGHT[0] + 5, STAGE_WIDTH_HEIGHT[1] + 5
                    new.position.x = random.randrange(50, STAGE_WIDTH_HEIGHT[0]-50)
                    new.position.y = random.randrange(-20, 0)
                    new.velocity = vector.objVector(0, 200*MEASURE_UNIT)
                    new.acceleration = vector.objVector(0, -2.5*MEASURE_UNIT)
                    new.fire_pattern = [self.fire_004]
                    new.phase_list = [self.motion_001_04]
                    new.health = 5
                    if random.randint(0, 2) == 2:
                        i1 = item.Item(self, 'power')
                        new.item_list = [i1] 
                    else:
                        new.item_list = [] 
                    self.enemy_group.add(new)

        if self.timer == 10*FRAME_PER_SECOND:
            self.summon_special(
                vector.objVector(STAGE_WIDTH_HEIGHT[0], STAGE_WIDTH_HEIGHT[1]/2),
                vector.objVector(STAGE_WIDTH_HEIGHT[0]/3, STAGE_WIDTH_HEIGHT[1]/2),
                self.fire_005, self.fire_005_01
            )

        elif self.timer == 11*FRAME_PER_SECOND:
            self.summon_special(
                vector.objVector(0, STAGE_WIDTH_HEIGHT[1]/3),
                vector.objVector(STAGE_WIDTH_HEIGHT[0]*2/3, STAGE_WIDTH_HEIGHT[1]/3),
                self.fire_005_01, self.fire_005
            )

        elif self.timer == 25*FRAME_PER_SECOND:
            self.summon_special(
                vector.objVector(0, STAGE_WIDTH_HEIGHT[1]/2),
                vector.objVector(STAGE_WIDTH_HEIGHT[0]/3, STAGE_WIDTH_HEIGHT[1]/2),
                self.fire_007
            )

        elif self.timer == 26*FRAME_PER_SECOND:
            self.summon_special(
                vector.objVector(STAGE_WIDTH_HEIGHT[0], STAGE_WIDTH_HEIGHT[1]/3),
                vector.objVector(STAGE_WIDTH_HEIGHT[0]*2/3, STAGE_WIDTH_HEIGHT[1]/3),
                self.fire_007
            )

        elif 32*FRAME_PER_SECOND > self.timer > 28*FRAME_PER_SECOND and self.timer % (0.5*FRAME_PER_SECOND) == 0:
            self.summon_a_list2(random.randint(0, 76))


        elif self.timer == 34*FRAME_PER_SECOND:
            self.summon_special(
                vector.objVector(STAGE_WIDTH_HEIGHT[0]/3, 0),
                vector.objVector(STAGE_WIDTH_HEIGHT[0]/3, STAGE_WIDTH_HEIGHT[1]/3),
                self.fire_006
            )
            self.summon_special(
                vector.objVector(STAGE_WIDTH_HEIGHT[0]*2/3, 0),
                vector.objVector(STAGE_WIDTH_HEIGHT[0]*2/3, STAGE_WIDTH_HEIGHT[1]/3),
                self.fire_006
            )
        elif self.timer == 38*FRAME_PER_SECOND:
            self.summon_special2(
                vector.objVector(STAGE_WIDTH_HEIGHT[0]/3, 0),
                vector.objVector(STAGE_WIDTH_HEIGHT[0]/3, STAGE_WIDTH_HEIGHT[1]/2),
                self.fire_007
            )
            self.summon_special2(
                vector.objVector(STAGE_WIDTH_HEIGHT[0]*2/3, 0),
                vector.objVector(STAGE_WIDTH_HEIGHT[0]*2/3, STAGE_WIDTH_HEIGHT[1]/2),
                self.fire_007
            )
        elif self.timer == 36*FRAME_PER_SECOND:
            self.summon_special(
                vector.objVector(0, STAGE_WIDTH_HEIGHT[0]/3),
                vector.objVector(STAGE_WIDTH_HEIGHT[0]/3, STAGE_WIDTH_HEIGHT[0]/3),
                self.fire_005
            )
            self.summon_special(
                vector.objVector(STAGE_WIDTH_HEIGHT[0], STAGE_WIDTH_HEIGHT[0]/2),
                vector.objVector(STAGE_WIDTH_HEIGHT[0]*2/3, STAGE_WIDTH_HEIGHT[0]/3),
                self.fire_005
            )
        elif self.timer == 40*FRAME_PER_SECOND:
            self.next_phase()


    def phase_006(self):
        """The sixth phase of the stage"""
        if self.timer == 1:
            for e in self.enemy_group.sprites():
                e.die()
            for b in self.barrage_group.sprites():
                d = item.Item(self, "smallpoint")
                d.position = b.position
                b.die()
                self.item_group.add(d)
            for i in self.item_group.sprites():
                i.collected = True

            b = stage_zero_margatriod.Margatriod003(self)
            self.boss_group.add(b)

    def fire_001_00(self, child): #中球跟踪狙， 运用：开始小怪 minion #1 attack
        enemy.Enemy.defualt_danmaku_pattern_002(child, ['midball', '2'], 3, 10, 300*MEASURE_UNIT)

    def motion_001_00(self, child): # 到点向左转，角度随机：开始小怪 minion #1 movement
        if child.phase_timer < 1.5*FRAME_PER_SECOND:
            child.velocity = vector.objVector(0, 150*MEASURE_UNIT)
        elif child.phase_timer == 1.5*FRAME_PER_SECOND:
            angle = random.randrange(110, 150)
            child.velocity.angle = angle
            child.fire_pattern[child.fire](child)

    def motion_001_01(self, child): # 向下走随机转并发弹幕：小怪 minion #2 movement
        if child.timer== 60:
            r = random.randint(0,2)
            if r >= 1:
                child.fire_pattern[child.fire](child)
    
    def motion_001_02(self, child): # 到点转，角度随机：phase3小怪 phase three minion movement 1
        if child.phase_timer < 1*FRAME_PER_SECOND:
            child.velocity = vector.objVector(0, 150*MEASURE_UNIT)
        elif child.phase_timer == 1*FRAME_PER_SECOND:
            if child.position.x < STAGE_WIDTH_HEIGHT[0] / 2:
                angle = random.randrange(110, 150)
            elif child.position.x >= STAGE_WIDTH_HEIGHT[0] / 2:
                angle = -1*random.randrange(110, 150)
            child.velocity.angle = angle
            if random.randint(0,4) == 1:
                child.fire_pattern[child.fire](child)

    def motion_001_03(self, child): # 向下走发弹幕向上走：phase3小怪 phase three minion movement 2
        if child.phase_timer < FRAME_PER_SECOND:
            child.velocity = vector.objVector(0, 150*MEASURE_UNIT)
        elif child.phase_timer == FRAME_PER_SECOND:
            if random.randint(0, 2):
                child.velocity.y *= -1

            if random.randint(0,2) == 1:
                if random.randint(0,1) == 1:        
                    child.fire_pattern[0](child)
                else:
                    child.fire_pattern[1](child)
    
    def motion_001_04(self, child): # 向下走发弹幕向上走：phase5小怪 phase five minion 
        if child.phase_timer < 0.7*FRAME_PER_SECOND:
            child.velocity = vector.objVector(0, 150*MEASURE_UNIT)
        elif child.phase_timer == 0.7*FRAME_PER_SECOND:
            child.velocity.y *= -1
            child.fire_pattern[0](child)

    
    def fire_002_00(self, child): #一次原型散射：开始从上面随机下来的小怪
        enemy.Enemy.defualt_danmaku_pattern_004(child, ['midball', '4'], count1=1, count2= 8)
    
    def motion_002_00(self, child): # 向下走随机转并发弹幕： 开始从上面随机下来的小怪
        if child.phase_timer < 1.5*FRAME_PER_SECOND:
            child.velocity = vector.objVector(0, 150*MEASURE_UNIT)
        elif child.phase_timer == 1.5*FRAME_PER_SECOND:
            angle = random.randrange(0, 360)
            child.velocity.norm *= 0.5
            child.velocity.angle = angle
            child.fire_pattern[child.fire](child)
        elif child.phase_timer > 1.5*FRAME_PER_SECOND and child.phase_timer%(1.5*FRAME_PER_SECOND) == 0:
            angle = random.randrange(0, 360)
            child.velocity.angle = angle
            child.fire_pattern[child.fire](child)


    
    def fire_003_00(self, child): # 三条通常狙：滚球
        time = child.timer
        barrage_type = ['midball', '2']
        count1 = 3
        count2 = 3
        delta_time = 0
        angle = 30
        speed = 200*MEASURE_UNIT
        delta_speed = 25*MEASURE_UNIT 

        for i in range(count1):
            for j in range(count2):
                dt = j*delta_time
                b = barrage.Barrage(child, barrage_type)
                b.aim = False
                b.velocity = vector.objVector(child.parent.player.position - b.parent.position)
                b.velocity.norm = speed + j*delta_speed
                if count1%2 != 0:
                    mid = int(count1/2)
                    b.velocity.angle += angle*(i - mid)
                else:
                    mid = count1/2 + 0.5
                    b.velocity.angle += angle*(i - mid)
                try:
                    child.fire_pattern_temp[time + dt].append(b)
                except:
                    child.fire_pattern_temp[time + dt] = []
                    child.fire_pattern_temp[time + dt].append(b)

    def fire_003_01(self, child, barrage_type = ['midball', '2'], count1=3, count2=5, angle=30, delta_time=0, speed=200*MEASURE_UNIT, delta_speed=25*MEASURE_UNIT): # 多条通常狙：小怪
        time = child.timer
        for i in range(count1):
            for j in range(count2):
                dt = j*delta_time
                b = barrage.Barrage(child, barrage_type)
                b.aim = False
                b.velocity = vector.objVector(child.parent.player.position - b.parent.position)
                b.velocity.norm = speed + j*delta_speed
                if count1%2 != 0:
                    mid = int(count1/2)
                    b.velocity.angle += angle*(i - mid)
                else:
                    mid = count1/2 + 0.5
                    b.velocity.angle += angle*(i - mid)
                try:
                    child.fire_pattern_temp[time + dt].append(b)
                except:
                    child.fire_pattern_temp[time + dt] = []
                    child.fire_pattern_temp[time + dt].append(b)
    
    def fire_003_02(self, child):
        '''phase 3 minion 0'''
        self.fire_003_01(child, ['midball', '2'], count1=5, count2=2, angle=15, delta_time=15, delta_speed=0, speed=150*MEASURE_UNIT)
    
    def fire_003_03(self, child):
        '''phase 3 minion 1'''
        self.fire_003_01(child, ['midball', '1'], count1=1, count2=3, angle=30, delta_time=0, delta_speed=10*MEASURE_UNIT, speed=200*MEASURE_UNIT)
    
    def fire_003_04(self, child):
        '''phase 3 minion 2'''
        self.fire_003_01(child, ['midball', '1'], count1=2, count2=3, angle=30, delta_time=0, delta_speed=10*MEASURE_UNIT, speed=200*MEASURE_UNIT)

    def fire_003_05(self, child):
        '''phase 3 minion 3'''
        self.fire_003_01(child, ['midball', '2'], count1=6, count2=1, angle=25, delta_speed=0, speed=150*MEASURE_UNIT)
    
    def fire_004(self, child):
        time = child.timer
        barrage_type = ['midball', '1']
        count1 = 2
        count2 = 4
        delta_time = 0
        speed = 200*MEASURE_UNIT
        delta_speed = 25*MEASURE_UNIT 

        for i in range(count1):
            if i:
                angle = 170
            else:
                angle = -170
            for j in range(count2):
                b = barrage.Barrage(child, barrage_type)
                b.velocity = vector.objVector(speed + delta_speed*j, 0)
                b.velocity.angle = angle
                try:
                    child.fire_pattern_temp[time+1].append(b)
                except:
                    child.fire_pattern_temp[time+1] = []
                    child.fire_pattern_temp[time+1].append(b)
        
    def fire_005(self, child, direction=1):
        time = child.timer
        barrage_type = ['barrier', '4']
        count = 5
        delta_t = 3
        delta_a = 2
        speed = 200*MEASURE_UNIT
        for i in range(count):
            b = barrage.Barrage(child, barrage_type)
            aim = child.parent.player.position - b.parent.position
            b.velocity = vector.objVector(speed, 0)
            b.velocity.angle = delta_a*i*direction + aim.angle
            try:
                child.fire_pattern_temp[time+ delta_t*i].append(b)
            except:
                child.fire_pattern_temp[time+ delta_t*i] = []
                child.fire_pattern_temp[time+ delta_t*i].append(b)
    
    def fire_005_01(self, child):
        self.fire_005(child, -1)

    def fire_006(self, child, direction=1):
        time = child.timer
        barrage_type = ['dart', '2']
        count = 20
        delta_t = 3
        delta_a = 2
        speed = 150*MEASURE_UNIT
        for i in range(count):
            aim = child.parent.player.position - child.position
            b = barrage.Barrage(child, barrage_type)
            b.velocity = vector.objVector(speed, 0)
            b.velocity.angle = aim.angle + random.randint(0, 60) - 30
            try:
                child.fire_pattern_temp[time+ delta_t*i].append(b)
            except:
                child.fire_pattern_temp[time+ delta_t*i] = []
                child.fire_pattern_temp[time+ delta_t*i].append(b)
        
    def fire_007(self, child):
        enemy.Enemy.defualt_danmaku_pattern_004(child, ['diamond', '1'], count2=12, delta_time=8)


    def motion_004(self, child): # custom path and turn up
        start = child.start
        end = child.end
        speed = child.speed
        if child.phase_timer == 1:
            child.fired = False
            child.velocity = end - start
            child.velocity.norm = speed
        
        if (child.position - child.end).norm <= 10:
            child.velocity = vector.objVector(0,0)

            if child.phase_timer%FRAME_PER_SECOND == 0:
                child.fire_pattern[0](child)
                child.fired_time = child.timer
            elif child.phase_timer%(0.5*FRAME_PER_SECOND) == 0:
                try:       
                    child.fire_pattern[1](child)
                    child.fired_time = child.timer
                except:
                    pass
        
            if child.phase_timer > 10*FRAME_PER_SECOND:
                child.velocity = vector.objVector(0,-200)*MEASURE_UNIT
            

    def motion_003_00(self, child): # 向右走， 挑头：滚球
        if child.phase_timer < 1.5*FRAME_PER_SECOND:
            child.velocity = vector.objVector(250*MEASURE_UNIT, 0)
        elif child.phase_timer == 1.5*FRAME_PER_SECOND:
            child.velocity = vector.objVector(250*MEASURE_UNIT, 0)
            child.fire_pattern[child.fire](child)
        elif 2.5*FRAME_PER_SECOND >= child.phase_timer > 1.5*FRAME_PER_SECOND:
            child.velocity.angle += -6
            if (child.phase_timer - 1.5*FRAME_PER_SECOND)%(1/3*FRAME_PER_SECOND) == 0:
                child.fire_pattern[child.fire](child)
        elif 2.5*FRAME_PER_SECOND < child.phase_timer:
            child.velocity = vector.objVector(-300*MEASURE_UNIT, 0)


        if 2.5*FRAME_PER_SECOND >= child.phase_timer > 1.5*FRAME_PER_SECOND:
            angle = (child.phase_timer - 1.5)*(180) + 90

    def motion_003_01(self, child): # 向左走， 挑头：滚球
        if child.phase_timer < 1.5*FRAME_PER_SECOND:
            child.velocity = vector.objVector(-250*MEASURE_UNIT, 0)
        elif child.phase_timer == 1.5*FRAME_PER_SECOND:
            child.velocity = vector.objVector(-250*MEASURE_UNIT, 0)
            child.fire_pattern[child.fire](child)
        elif 2.5*FRAME_PER_SECOND >= child.phase_timer > 1.5*FRAME_PER_SECOND:
            child.velocity.angle += 6
            if (child.phase_timer - 1.5*FRAME_PER_SECOND)%(1/3*FRAME_PER_SECOND) == 0:
                child.fire_pattern[child.fire](child)
        elif 2.5*FRAME_PER_SECOND < child.phase_timer:
            child.velocity = vector.objVector(300*MEASURE_UNIT, 0)


        if 2.5*FRAME_PER_SECOND >= child.phase_timer > 1.5*FRAME_PER_SECOND:
            angle = (child.phase_timer - 1.5)*(180) + 90

    def fire_100(self, child):
        time = child.timer
        speed = 250*MEASURE_UNIT
        delta_time = 5
        for i in range(16):
            temp_list = []
            dt = i*delta_time
            for j in range(20):
                b = barrage.Barrage(child, ['texturedball', '3'])
                b.speed = speed
                b.position[0] = child.position[0] + cos(math.pi/2 + math.pi*i/15)*200
                b.position[1] = child.position[1] + sin(math.pi/2 + math.pi*i/15)*200
                b.correct_start_position = False
                b.velocity = vector.objVector(speed, 0)
                b.velocity.angle = j*(360/16)
                temp_list.append(b)

            for j in range(20):
                b = barrage.Barrage(child, ['texturedball', '4'])
                b.speed = speed
                b.velocity = vector.objVector(speed, 0)
                b.position[0] = child.position[0] + cos(math.pi/2 - math.pi*i/15)*200
                b.position[1] = child.position[1] + sin(math.pi/2 - math.pi*i/15)*200
                b.correct_start_position = False
                b.velocity.angle = j*(360/16)
                temp_list.append(b)
            try:
                child.fire_pattern_temp[time + dt].append(b)
            except:
                child.fire_pattern_temp[time + dt] = []
                child.fire_pattern_temp[time + dt] = child.fire_pattern_temp[time + dt] + temp_list

    def fire_200(self, child): # 早苗🌟弹
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
                    new.phase_list = [self.star_fire_update]
                    
                    new.custom_messages = {"start_angle": math.degrees(pi - 2*pi/5*j), "base_angle": math.degrees(sangle - pi + pi/20*i), "delay": int(delta_time)}
                    try:
                        child.fire_pattern_temp[time + int(delta_time)].append(new)
                    except:
                        child.fire_pattern_temp[time + int(delta_time)] = []
                        child.fire_pattern_temp[time + int(delta_time)].append(new)
                i += 1
        
    def star_fire_update(self, child):
        if child.timer + child.custom_messages["delay"] == 4*FRAME_PER_SECOND:
            child.velocity = vector.objVector(200*MEASURE_UNIT,0)
            child.velocity.angle = child.custom_messages["start_angle"]
        elif 5*FRAME_PER_SECOND > child.timer + child.custom_messages["delay"] > 4*FRAME_PER_SECOND:
            child.velocity.norm = child.velocity.norm - 2.5*MEASURE_UNIT
        elif child.timer + child.custom_messages["delay"] >= 5*FRAME_PER_SECOND:
            child.velocity.angle = child.custom_messages["base_angle"]

    def stage_end(self):
        return stage_one.StageOne(self.screen, self.player).run()

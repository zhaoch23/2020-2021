from core.boss import *
from effect import bossback
from core import enemy
from effect import explode

sin = math.sin
cos = math.cos
tan = math.tan

class Margatriod001(Boss):
    """Stage Zero Boss Margatriod
    bound_style: determine if there will be a invincible wall
        BOUND_BLOCK: invincible wall
        BOUND_CUSTOM: no invincible wall
    phase_list: the list of boss's phases
    fire_pattern: the list of boss's fire patterns
    position: the boss's location
    
    """

    def __init__(self, parent, type_id='margatroid'):
        super().__init__(parent, type_id=type_id)
        self.set_health(0)
        e1 = bossback.BossBack001(self)
        e2 = bossback.BossBack002(self)
        self.bound_style = BOUND_BLOCK
        self.effect_group.add(e1)
        self.effect_group.add(e2)
        self.phase_list = [self.motion_001, self.motion_002]
        self.fire_pattern = [self.spell_001_00, self.spell_001_01, self.spell_001_02, self.spell_001_03]
        self.position = vector.objVector(STAGE_WIDTH_HEIGHT[0]/2, STAGE_WIDTH_HEIGHT[1]/3) + vector.objVector(-300, -300)


    def motion_001(self, child):
        """Determines the actions of the boss"""
        if self.phase_timer < 1*FRAME_PER_SECOND:
            self.velocity = vector.objVector(300, 300)*MEASURE_UNIT
        
        elif self.phase_timer == 1*FRAME_PER_SECOND:
            for e in self.effect_group.sprites():
                self.parent.effect_group.add(e)
                e.position = self.position
            self.velocity = vector.objVector(0, 0)
            self.set_health(800)
            self.fire_pattern[self.fire](self)
            self.fire = 1
            
        elif self.phase_timer == 9*FRAME_PER_SECOND:
            self.fire_pattern[self.fire](self)
            self.fire += 1

        elif self.phase_timer == 16*FRAME_PER_SECOND:
            x = random.randrange(-100, 100)
            y = random.randrange(-100, 100)
            self.velocity = vector.objVector(x, y)*MEASURE_UNIT
        
        elif self.phase_timer == 17*FRAME_PER_SECOND:
            self.velocity = vector.objVector(0,0)
            self.fire_pattern[self.fire](self)
            self.fire += 1

        elif self.phase_timer == 25*FRAME_PER_SECOND:
            self.fire_pattern[self.fire](self)

        elif self.phase_timer == 33*FRAME_PER_SECOND:
            self.next_phase()

        if self.done:
            self.next_phase()

    """The different attacks"""
    
    def spell_001_00(self, child):
        self.spell_001(self, ['midball', '2'], 4)
    
    def spell_001_01(self, child):
        self.spell_001(self, ['midball', '1'], 4, -12)

    def spell_001_02(self, child):
        self.spell_001(self, ['midball', '4'], 5, 12)
    
    def spell_001_03(self, child):
        self.spell_001(self, ['midball', '5'], 5, -12)
    
    def spell_001(self, child, barrage_type=['midball', '2'], anchor_point_cnt=4, anchor_point_da=12):
        """spell_001
        anchor_point_dt: delta time
        anchor_point_dd: delta d
        variables controlling the attack:
        d_from_boss, b_cnt1, b_cnt2, b_speed, b_ds = 15*MEASURE_UNIT

        
        """
        time = self.timer
        anchor_point_dt = 5
        anchor_point_dd = 3
        
        d_from_boss = 120
        b_cnt1 = 2
        b_cnt2 = 3
        b_speed = 100*MEASURE_UNIT
        b_ds = 15*MEASURE_UNIT

        for anchor in range(anchor_point_cnt):
            anchor_position = vector.objVector(d_from_boss, 0)
            anchor_position.angle = anchor*(360/anchor_point_cnt)

            total_dt = 0
            for k in range(int(d_from_boss/anchor_point_dd)):
                total_dt += anchor_point_dt
                anchor_position.norm -= anchor_point_dd
                anchor_position.angle += anchor_point_da

                anchor_n_position = anchor_position.copy()
                anchor_n_position.norm -= anchor_point_dd
                anchor_n_position.angle += anchor_point_da

                dp = anchor_position -  anchor_n_position 

                anchor_r_position = anchor_position + self.position
                for i in range(b_cnt1):
                    for j in range(b_cnt2):                       
                        b = barrage.Barrage(self, barrage_type)
                        b.correct_start_position = False
                        b.position = anchor_r_position
                        b.velocity = vector.objVector(b_speed + b_ds*i*(j+1), 0)
                        b.velocity.angle = dp.angle + 20*j
                
                        try:
                            self.fire_pattern_temp[time + total_dt].append(b)
                        except:
                            self.fire_pattern_temp[time + total_dt] = []
                            self.fire_pattern_temp[time + total_dt].append(b)


    def motion_002(self, child):
        if self.phase_timer == 1:
            for b in self.parent.barrage_group.sprites():
                d = item.Item(self.parent, "smallpoint")
                d.position = b.position
                d.collected = True
                b.die()
                self.parent.item_group.add(d)

            self.fire_pattern_temp.clear()
            
            for e in self.effect_group.sprites():
                e.die()

            self.velocity = vector.objVector(300, -300)*MEASURE_UNIT
            self.set_health(0)

            temp_list = []

            for i in range(10):
                r = random.randint(0, 1)
                if r == 0:
                    i = item.Item(self.parent, 'power')
                else:
                    i = item.Item(self.parent, 'largepower')
                rx = random.randrange(-50, 50)
                ry = random.randrange(-50, 50)
                i.position = vector.objVector(self.position.x + rx, self.position.y + ry)
                self.parent.item_group.add(i)

            for i in range(10):
                r = random.randint(0, 1)
                if r == 0:
                    i = item.Item(self.parent, 'point')
                else:
                    i = item.Item(self.parent, 'largepoint')
                rx = random.randrange(-50, 50)
                ry = random.randrange(-50, 50)
                i.position = vector.objVector(self.position.x + rx, self.position.y + ry)
                self.parent.item_group.add(i)
        

        if self.position.y <= 0:
            self.die()





class Margatriod002(Boss):
    
    """Stage Zero Boss Margatriod Encounter #2
    bound_style: determine if there will be a invincible wall
        BOUND_BLOCK: invincible wall
        BOUND_CUSTOM: no invincible wall
    phase_list: the list of boss's phases
    fire_pattern: the list of boss's fire patterns
    position: the boss's location
    
    """

    def __init__(self, parent, type_id='margatroid'):
        super().__init__(parent, type_id=type_id)
        self.set_health(0)
        e1 = bossback.BossBack001(self)
        e2 = bossback.BossBack002(self)
        self.bound_style = BOUND_BLOCK
        self.effect_group.add(e1)
        self.effect_group.add(e2)
        self.done = False
        self.phase_list = [self.motion_001, self.motion_002, self.motion_003]
        self.fire_pattern = [self.spell_001_01, self.spell_001_02, self.spell_001_03, self.spell_001_04, self.spell_001_05, self.spell_001_06, self.spell_001_07]
        self.position =    self.position = vector.objVector(STAGE_WIDTH_HEIGHT[0]/2, STAGE_WIDTH_HEIGHT[1]/3) + vector.objVector(-300, -300)
    
    """Movements and attacks"""
    def motion_000(self, child):
        if self.phase_timer == 3*FRAME_PER_SECOND:
            for e in self.effect_group.sprites():
                self.parent.effect_group.add(e)
                e.position = self.position
            self.velocity = vector.objVector(0, 0)
            self.set_health(1000)
            self.fire_pattern[self.fire](self)

    def motion_001(self, child):    
        if self.phase_timer < FRAME_PER_SECOND:
            self.velocity = vector.objVector(300, 300)*MEASURE_UNIT  
        if self.phase_timer == FRAME_PER_SECOND:
            for e in self.effect_group.sprites():
                self.parent.effect_group.add(e)
                e.position = self.position
            self.velocity = vector.objVector(0, 0)
            self.set_health(800)
            self.fire_pattern[self.fire](self)
            self.fire += 1
        elif 10*FRAME_PER_SECOND >= self.phase_timer > FRAME_PER_SECOND and (self.phase_timer - FRAME_PER_SECOND)%(1.5*FRAME_PER_SECOND) == 0:
            self.fire_pattern[self.fire](self)
            self.fire += 1

        elif self.phase_timer == 11.5*FRAME_PER_SECOND:
            x = (random.randint(0, 200) - 100)*MEASURE_UNIT
            self.velocity = vector.objVector(x, 0)
            self.fire = 0
            self.fire_pattern[self.fire](self)     

        elif 20.5*FRAME_PER_SECOND >= self.phase_timer > 11.5*FRAME_PER_SECOND and (self.phase_timer - FRAME_PER_SECOND)%(1.5*FRAME_PER_SECOND) == 0:
            self.fire_pattern[self.fire](self)
            self.velocity = vector.objVector(0, 0)
            self.fire += 1

        elif self.phase_timer == 22*FRAME_PER_SECOND:
            x = (random.randint(0, 200) - 100)*MEASURE_UNIT
            self.velocity = vector.objVector(x, 0)
            self.fire = 0
            self.fire_pattern[self.fire](self)     

        elif 31*FRAME_PER_SECOND >= self.phase_timer > 22*FRAME_PER_SECOND and (self.phase_timer - FRAME_PER_SECOND)%(1.5*FRAME_PER_SECOND) == 0:
            self.fire_pattern[self.fire](self)
            self.velocity = vector.objVector(0, 0)
            self.fire += 1

        elif self.phase_timer > 33*FRAME_PER_SECOND:
            self.phase_done()
            self.next_phase()

        if self.done:
            self.phase_done()
            self.next_phase()

    def motion_002(self, child): 
        if self.phase_timer == 1:
            self.velocity = (vector.objVector(STAGE_WIDTH_HEIGHT[0]/2, STAGE_WIDTH_HEIGHT[1]/3) - self.position)/(4*FRAME_PER_SECOND)
            self.fire_pattern = [self.spell_002]
            self.fire = 0
        
        elif self.phase_timer == 4*FRAME_PER_SECOND:
            e1 = bossback.BossBack001(self)
            e2 = bossback.BossBack002(self)
            self.effect_group.add(e1)
            self.effect_group.add(e2)
            for e in self.effect_group.sprites():
                self.parent.effect_group.add(e)
                e.position = self.position

            self.velocity = vector.objVector(0, 0)
            self.set_health(1000)
            self.fire_pattern[self.fire](self)

        elif self.phase_timer > 4*FRAME_PER_SECOND and self.phase_timer%(4*FRAME_PER_SECOND) == 0:
            self.fire_pattern[self.fire](self)

        

        if self.phase_timer >= 4*FRAME_PER_SECOND and self.done:
            self.phase_done()
            self.next_phase() 
        
    
    def motion_003(self, child): # motion 3
        if self.phase_timer == 1:
            d = item.Item(self.parent, "life")
            d.position = self.position
            self.parent.item_group.add(d)
        self.velocity = vector.objVector(300, -300)*MEASURE_UNIT


        if self.phase_timer > 3*FRAME_PER_SECOND:
            self.parent.next_phase()
            self.die()


    
    def phase_done(self):
        self.set_health(0)

        for b in self.parent.barrage_group.sprites():
            d = item.Item(self.parent, "smallpoint")
            d.position = b.position
            d.collected = True
            b.die()
            self.parent.item_group.add(d)

        self.fire_pattern_temp.clear()
        
        for e in self.effect_group.sprites():
            e.die()

        for e in self.parent.enemy_group.sprites():
            e.die()

        for i in range(10):
            r = random.randint(0, 1)
            if r == 0:
                i = item.Item(self.parent, 'power')
            else:
                i = item.Item(self.parent, 'largepower')
            rx = random.randrange(-50, 50)
            ry = random.randrange(-50, 50)
            i.position = vector.objVector(self.position.x + rx, self.position.y + ry)
            self.parent.item_group.add(i)

        for i in range(10):
            r = random.randint(0, 1)
            if r == 0:
                i = item.Item(self.parent, 'point')
            else:
                i = item.Item(self.parent, 'largepoint')
            rx = random.randrange(-50, 50)
            ry = random.randrange(-50, 50)
            i.position = vector.objVector(self.position.x + rx, self.position.y + ry)
            self.parent.item_group.add(i)


    """Attacks and movements"""
    def spell_001_01(self, child):
        self.spell_001(child, ['barrier', '3'], 1)
    
    def spell_001_02(self, child):
        self.spell_001(child, ['barrier', '4'], -1)

    def spell_001_03(self, child):
        self.spell_001(child, ['barrier', '5'], 1)

    def spell_001_04(self, child):
        self.spell_001(child, ['barrier', '6'], -1)

    def spell_001_05(self, child):
        self.spell_001(child, ['barrier', '8'], 1)
    
    def spell_001_06(self, child):
        self.spell_001(child, ['barrier', '1'], -1)
    
    def spell_001_07(self, child):
        self.spell_001(child, ['barrier', '2'], 1)


    def spell_001(self, child, barrage_type=['barrier', '3'], direction=1):
        time = self.timer
        anchor_position = vector.objVector(-100, 0)
        anchor_cnt = 15

        b_cnt1 = 10
        b_cnt2 = 5
        b_speed1 = 100*MEASURE_UNIT
        b_speed2 = 150*MEASURE_UNIT
        dt = 1
        da = 180/anchor_cnt

        for i in range(anchor_cnt):
            angle = (da*i + 90)*direction
            total_dt = i*dt
            anchor_position.angle = angle

            temp_list = []

            for j in range(b_cnt1):
                b = barrage.Barrage(self, barrage_type)
                b.position = anchor_position + self.position
                b.velocity = vector.objVector(b_speed1, 0)
                b.velocity.angle = (360/b_cnt1)*j - 90 + da*i
                b.correct_start_position = False
                temp_list.append(b)
            
            for k in range(b_cnt2):
                b = barrage.Barrage(self, barrage_type)
                b.position = anchor_position + self.position
                b.velocity = vector.objVector(b_speed2, 0)
                b.velocity.angle = (180/b_cnt2)*j - 90 + da*i
                b.correct_start_position = False
                temp_list.append(b)

            try:
                self.fire_pattern_temp[time + total_dt] = child.fire_pattern_temp[time + total_dt] + temp_list
            except:
                self.fire_pattern_temp[time + total_dt] = []
                self.fire_pattern_temp[time + total_dt] = child.fire_pattern_temp[time + total_dt] + temp_list

    def spell_002(self, child):
        time = self.timer
        b = barrage.Barrage(self, ['viodball', '2'])
        b.velocity = (self.parent.player.position - self.position)
        b.velocity.norm = 75*MEASURE_UNIT
        b.phase_list = [self.spell_002_update]

        try:
            child.fire_pattern_temp[time].append(b)
        except:
            child.fire_pattern_temp[time] = []
            child.fire_pattern_temp[time].append(b)

    def spell_002_update(self, child):
        if child.timer == FRAME_PER_SECOND*2:
            self.spell_002_doll(self.parent, child.position)
            e = explode.Explode(child)
            e.position = child.position
            self.parent.effect_group.add(e)
            child.die()

    def spell_002_doll(self, child, start_position):
        for i in range(18): 
            x = random.randint(0, STAGE_WIDTH_HEIGHT[0])
            y = random.randint(0, int(STAGE_WIDTH_HEIGHT[1]/3))
            new = enemy.Enemy(self.parent, 'bluesprite')
            new.position = start_position
            new.destination = vector.objVector(x, y)
            new.velocity =  (vector.objVector(x, y) - start_position)
            new.velocity.norm = 500*MEASURE_UNIT
            new.health = 5
            new.fired = False
            new.phase_list = [self.spell_002_dollmotion]
            i1 = item.Item(self.parent, 'point')
            new.item_list = [i1] 
            self.parent.enemy_group.add(new)

        
    def spell_002_dollmotion(self, child):
        if (child.position - child.destination).norm <= 10:
            child.velocity = vector.objVector(0,0)
            if not child.fired:
                child.fired = True
                child.fired_time = child.timer
                child.aim_angle = random.randint(150, 210)
                y = STAGE_WIDTH_HEIGHT[1] - child.position.y
                x = child.position.x - tan(math.radians(180 - child.aim_angle))*y
                aim_position = vector.objVector(x, STAGE_WIDTH_HEIGHT[1])
                enemy.Enemy.defualt_danmaku_pattern_006(child, aim_position, ['laser', '2'])

            if child.fired and child.timer == child.fired_time + 0.5*FRAME_PER_SECOND:
                self.spell_002_dollfire_01(child)
                self.spell_002_dollfire_02(child)          
            if child.fired and child.timer == child.fired_time + 1.5*FRAME_PER_SECOND:
                child.die()            
            
    def spell_002_dollfire_01(self, child):
        time = child.timer
        barrage_type = ['midball', '2']
        count1 = 3
        count2 = 8
        delta_time = 0
        angle = 90
        speed = 250*MEASURE_UNIT
        delta_speed = 25*MEASURE_UNIT 
        aim_angle = child.aim_angle +  random.randint(-45, 45)
        for i in range(count1):
            for j in range(count2):
                dt = j*delta_time
                b = barrage.Barrage(child, barrage_type)
                b.aim = False
                b.velocity = vector.objVector(child.parent.player.position - b.parent.position)
                b.velocity.angle = aim_angle
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

    def spell_002_dollfire_02(self, child): # spell 2 dollfire
        time = child.timer
        barrage_type = ['midball', '1']
        cnt = 10
        aim_angle = child.aim_angle
        speed = 200*MEASURE_UNIT
        delta_speed = 10*MEASURE_UNIT 
        for i in range(cnt):
            b = barrage.Barrage(child, barrage_type)
            b.aim = False
            b.velocity = vector.objVector(child.parent.player.position - b.parent.position)
            b.velocity.angle = aim_angle
            b.velocity.norm = speed + i*delta_speed
            b.correct_start_position = False
            b.position = child.position + vector.objVector(random.randint(-30,30), random.randint(-30,30))
            try:
                child.fire_pattern_temp[time].append(b)
            except:
                child.fire_pattern_temp[time] = []
                child.fire_pattern_temp[time].append(b)

class Margatriod003(Boss):
    '''
    This is movement & attack No.3
    '''

    def __init__(self, parent, type_id='margatroid'): # init
        super().__init__(parent, type_id=type_id)
        self.set_health(0)
        e1 = bossback.BossBack001(self)
        e2 = bossback.BossBack002(self)
        self.bound_style = BOUND_BLOCK
        self.effect_group.add(e1)
        self.effect_group.add(e2)
        self.done = False
        self.phase_list = [self.motion_001, self.motion_002, self.motion_003, self.motion_004, self.motion_005]
        self.fire_pattern = [self.spell_001]
        self.position = self.position = vector.objVector(STAGE_WIDTH_HEIGHT[0]/2, STAGE_WIDTH_HEIGHT[1]/3) + vector.objVector(-300, -300)
        self.doll_group = pygame.sprite.Group()


    def motion_001(self, child):  # motion 1   
        if self.phase_timer < FRAME_PER_SECOND:
            self.velocity = vector.objVector(300, 300)*MEASURE_UNIT  
        elif self.phase_timer == FRAME_PER_SECOND:
            for e in self.effect_group.sprites():
                self.parent.effect_group.add(e)
                e.position = self.position
            self.velocity = vector.objVector(0, 0)
            self.set_health(1000)
            self.fire_pattern[self.fire](self)
            self.fire += 1

        elif self.phase_timer > FRAME_PER_SECOND:
            dolls = len(self.doll_group.sprites())
            if dolls == 0:
                self.phase_done()
                self.next_phase()
            
    
    def spell_001(self, child): # spell 1
        doll_cnt = 10
        self.invulnerable = True
        for i in range(doll_cnt):
            doll = enemy.Enemy(self.parent, 'bluesprite')
            doll.master = self
            doll.sprite_type = SPRITE_ENEMY_SPECIAL
            doll.constant_distance = 100
            doll.item_list = []
            doll.position = self.position
            doll.movement = 0
            doll.initial_angle = 360/doll_cnt*i
            doll.health = 150
            doll.rotating = True
            doll.phase_list = [self.spell_001_dollmotion]
            self.doll_group.add(doll)
            self.parent.enemy_group.add(doll)
    
    def spell_001_dollmotion(self, child): # spell 1
        distance_from_master = (child.position - self.position).norm
        distance_from_master += child.movement
        child.position = vector.objVector(distance_from_master, 0)
        child.position.angle = child.initial_angle


        if distance_from_master <= child.constant_distance/2:
            child.movement = 0.5
        elif distance_from_master > child.constant_distance:
            child.movement = -0.5

            new = barrage.Barrage(self, ['barrier', '1'])
            new.position = self.position + child.position
            new.velocity = vector.objVector(100*MEASURE_UNIT, 0)
            new.velocity.angle = child.position.angle - 90
            new.rebound_times = 0
            new.phase_list = [self.spell_001_doll_fire_update]
            new.types = [['barrier', '8'], ['barrier', '4'], ['barrier', '6']]
            new.active = True
            self.parent.barrage_group.add(new)
    
        child.position = self.position + child.position
        child.initial_angle += 3.6
    
    def spell_001_doll_fire_update(self, child): # spell 1 update
        child.auto_rotate()
        if child.rebound_times == 0 and child.timer == FRAME_PER_SECOND:
            for i in range(5):
                new = barrage.Barrage(self, child.types[child.rebound_times])
                new.position = child.position
                new.velocity = -1*child.velocity
                new.velocity.angle =  new.velocity.angle - 45 + i*22.5
                new.velocity.norm = 100*MEASURE_UNIT
                new.rebound_times = 1
                new.types = [['barrier', '8'], ['barrier', '4'], ['barrier', '6']]
                new.phase_list = [self.spell_001_doll_fire_update]
                new.active = True
                self.parent.barrage_group.add(new)

                child.die()
        elif child.rebound_times == 1 and child.timer == FRAME_PER_SECOND:
            for i in range(5):
                new = barrage.Barrage(self, child.types[child.rebound_times])
                new.position = child.position
                new.velocity = -1*child.velocity
                new.velocity.angle =  new.velocity.angle - 45 + i*22.5
                new.velocity.norm = 100*MEASURE_UNIT
                new.rebound_times = 2
                new.types = [['barrier', '8'], ['barrier', '4'], ['barrier', '6']]
                new.phase_list = [self.spell_001_doll_fire_update]
                new.active = True
                self.parent.barrage_group.add(new)

                child.die()
        elif child.rebound_times == 2 and child.timer == FRAME_PER_SECOND:
            for i in range(3):
                new = barrage.Barrage(self, child.types[child.rebound_times])
                new.position = child.position
                new.velocity = -1*child.velocity
                new.velocity.angle =  new.velocity.angle - 30 + i*30
                new.velocity.norm = 100*MEASURE_UNIT
                new.active = True
                self.parent.barrage_group.add(new)

                child.die()

    def random_move(self): # random move using random function
        rd = random.randint(0, int(STAGE_WIDTH_HEIGHT[1]))
        rd_mag = random.randint(50, 100)
        y = random.randint(0, 100) - 50
        if rd <= self.position.x:
            self.velocity = vector.objVector(-rd_mag*MEASURE_UNIT, y*MEASURE_UNIT)
            self.rd = 1
        elif rd > self.position.x:
            self.velocity = vector.objVector(rd_mag*MEASURE_UNIT, y*MEASURE_UNIT)
            self.rd = -1
        
        if self.position.x >  STAGE_WIDTH_HEIGHT[1] - 100:
            self.velocity = vector.objVector(-rd_mag*MEASURE_UNIT, y*MEASURE_UNIT)
            self.rd = 1
        elif self.position.x < 100:
            self.rd = 1
            self.velocity = vector.objVector(rd_mag*MEASURE_UNIT, y*MEASURE_UNIT)
        
        if self.position.y < 100:
            self.velocity.y = abs(y)*MEASURE_UNIT
        elif self.position.y > STAGE_WIDTH_HEIGHT[1]/2:
            self.velocity.y = -1*abs(y)*MEASURE_UNIT

    def motion_002(self, child): # motion 2


        if self.phase_timer == 1:
            self.velocity = (vector.objVector(STAGE_WIDTH_HEIGHT[0]/2, STAGE_WIDTH_HEIGHT[1]/3) - self.position)/(1*FRAME_PER_SECOND)
            self.fire_pattern = [self.spell_002_01, self.spell_002_02]
            self.fire = 0

        if self.phase_timer == FRAME_PER_SECOND:
            self.velocity = vector.objVector(0,0)

        elif self.phase_timer == 3*FRAME_PER_SECOND:
            for e in self.effect_group.sprites():
                self.parent.effect_group.add(e)
                e.position = self.position
            self.random_move()  

            self.set_health(1000)
        
        elif self.phase_timer >= FRAME_PER_SECOND*4 and self.phase_timer%(FRAME_PER_SECOND*4) == 0:
            self.velocity = vector.objVector(0,0) 
            
            if self.rd == 1:
                self.fire_pattern[0](self)
            if self.rd == -1:
                self.fire_pattern[1](self)

        elif self.phase_timer >= FRAME_PER_SECOND*4 and self.phase_timer%(FRAME_PER_SECOND*2) == 0:
            self.random_move()  
        
        if self.done:
            self.phase_done()
            self.next_phase()



    def spell_002_01(self, child):
        self.spell_002(child, 1)
    def spell_002_02(self, child):
        self.spell_002(child, -1)


    def spell_002(self, child, direction): # spell 2
        delta_d = 75*direction

        def summon_horizontal(position):

            if STAGE_WIDTH_HEIGHT[0] - position.x <= 100 and direction == 1:
                return position

            if position.x <= 100 and direction == -1:
                return position

            x = random.randint(0, 50) - 25
            y = random.randint(0, 50) - 25

            doll = enemy.Enemy(self.parent, 'bluesprite')
            doll.sprite_type = SPRITE_ENEMY_SPECIAL 
            doll.item_list = []
            doll.position = vector.objVector(position.x + x + delta_d, position.y + y)
            doll.health = 50
            doll.phase_list = [self.spell_002_dollmotion]
            doll.fire_pattern = [self.spell_002_dollfire_01]
            self.doll_group.add(doll)
            self.parent.enemy_group.add(doll)

            return summon_horizontal(doll.position.copy())

        def summon_vertical(position): # summon laser beam
            if STAGE_WIDTH_HEIGHT[1] - position.y <= 100:
                return position

            x = random.randint(0, 50) - 25
            y = random.randint(0, 50) - 25

            doll = enemy.Enemy(self.parent, 'bluesprite')
            doll.sprite_type = SPRITE_ENEMY_SPECIAL 
            doll.item_list = []
            doll.position.x = position.x + x 
            doll.position.y = position.y + y + abs(delta_d)
            doll.health = 50
            doll.phase_list = [self.spell_002_dollmotion]
            doll.fire_pattern = [self.spell_002_dollfire_02]
            self.doll_group.add(doll)
            self.parent.enemy_group.add(doll)

            return summon_vertical(doll.position.copy())

        summon_vertical(summon_horizontal(self.position))
    
    def spell_002_dollmotion(self, child): # spell 2
        if child.phase_timer == 1:
            child.fack_position = child.position.copy()
            child.fack_velocity = self.position - child.position
            child.fack_velocity.norm = 100*MEASURE_UNIT
        
        elif child.phase_timer > 1 and (child.fack_position - self.position).norm > 10:
            child.fack_position += child.fack_velocity
        elif child.phase_timer > 1 and (child.fack_position - self.position).norm < 10:
            child.fire_pattern[0](child)
            child.die()
        
        if child.timer == 2*FRAME_PER_SECOND:
            child.fire_pattern[0](child)
            child.die()       
    
    def spell_002_dollfire_01(self, child): # spell 1 & 2 dollfire
        self.spell_002_dollfire(child, barrage_type=['star', '6'])
    def spell_002_dollfire_02(self, child):
        self.spell_002_dollfire(child, barrage_type=['star', '3'])

    def spell_002_dollfire(self, child, barrage_type=['star', '6']):
        time = child.timer
        cnt1 = 6
        cnt2 = 5
        for i in range(cnt1):
            angle = 360/cnt1
            for j in range(cnt2):
                bias = random.randrange(0, 10) - 5
                b = barrage.Barrage(child, barrage_type)
                b.velocity = vector.objVector(100*MEASURE_UNIT + random.randint(0, 30)*MEASURE_UNIT, 0)
                b.velocity.angle = angle*i + bias
                try:
                    child.fire_pattern_temp[time].append(b)
                except:
                    child.fire_pattern_temp[time] = []
                    child.fire_pattern_temp[time].append(b)

    def motion_003(self, child): # motion 3
        if self.phase_timer == 1:
            self.velocity = (vector.objVector(STAGE_WIDTH_HEIGHT[0]/2, STAGE_WIDTH_HEIGHT[1]/3) - self.position)/(1*FRAME_PER_SECOND)
            self.fire_pattern = [self.spell_003]
            self.fire = 0
        if self.phase_timer == FRAME_PER_SECOND:
            self.velocity = vector.objVector(0,0)
            for e in self.effect_group.sprites():
                self.parent.effect_group.add(e)
                e.position = self.position
            self.velocity = vector.objVector(0, 0)
            self.set_health(1000)
            self.fire_pattern[self.fire](self)
            self.fire += 1

        elif self.phase_timer > FRAME_PER_SECOND:
            dolls = len(self.doll_group.sprites())
            if dolls == 0:
                self.phase_done()
                self.next_phase()
        if self.phase_timer > FRAME_PER_SECOND and self.done:
            d = item.Item(self.parent, "life")
            d.position = self.position
            self.parent.item_group.add(d)
            self.phase_done()
            self.next_phase()    

    def spell_003(self, child): # spell 3
        doll_cnt = 10
        for i in range(doll_cnt):
            doll = enemy.Enemy(self.parent, 'yellowsprite')
            doll.master = self
            doll.sprite_type = SPRITE_ENEMY_SPECIAL
            doll.constant_distance = 100
            doll.item_list = []
            doll.position = self.position
            doll.movement = 0
            doll.initial_angle = 360/doll_cnt*i
            doll.shut_angle = 0
            doll.health = 200
            doll.rotating = True
            doll.phase_list = [self.spell_003_dollmotion]
            doll.types = [['diamond', '3'], ['diamond', '7'], ['diamond', '2'], ['diamond', '9']]
            doll.type_pointer = 0
            self.doll_group.add(doll)
            self.parent.enemy_group.add(doll)


    def spell_003_dollmotion(self, child): # spell 3 dollmotion
        distance_from_master = (child.position - self.position).norm
        distance_from_master += child.movement
        child.position = vector.objVector(distance_from_master, 0)
        child.position.angle = child.initial_angle
        child.position = self.position + child.position
        child.initial_angle += 3.6
        if distance_from_master <= child.constant_distance/2:
            child.movement = 0.5
            child.fire_type = 0

        elif distance_from_master > child.constant_distance:
            child.movement = -0.5
            child.type_pointer += 1
            child.fire_type = 1
            if child.type_pointer >= len(child.types):
                child.type_pointer = 0
        
        if child.fire_type == 0 and self.phase_timer%(0.5*FRAME_PER_SECOND) == 0:
            for j in range(6):
                anglepos = 360/6*j
                b =  barrage.Barrage(self, child.types[child.type_pointer])
                position = vector.objVector(60, 0)
                position.angle = anglepos
                b.position = position + child.position
                b.correct_start_position = False
                b.active = True
                b.velocity = vector.objVector(150*MEASURE_UNIT, 0)
                b.velocity.angle = child.initial_angle
                self.parent.barrage_group.add(b)
            child.shut_angle += 12
        elif child.fire_type == 1 and self.phase_timer%(0.5*FRAME_PER_SECOND) == 0:
            for j in range(8):
                anglepos = 360/8*j
                b =  barrage.Barrage(self, child.types[child.type_pointer])
                position = vector.objVector(60, 0)
                position.angle = anglepos
                b.position = position + child.position
                b.correct_start_position = False
                b.active = True
                b.velocity = vector.objVector(150*MEASURE_UNIT, 0)
                b.velocity.angle = child.shut_angle + child.initial_angle
                self.parent.barrage_group.add(b)
    
    def motion_004(self, child): # motion 4
        if self.phase_timer == 1:
            self.velocity = (vector.objVector(STAGE_WIDTH_HEIGHT[0]/2, STAGE_WIDTH_HEIGHT[1]/3) - self.position)/(1*FRAME_PER_SECOND)
            self.fire_pattern = [self.spell_004]
            self.fire = 0
        if self.phase_timer == FRAME_PER_SECOND:
            self.velocity = vector.objVector(0,0)
            for e in self.effect_group.sprites():
                self.parent.effect_group.add(e)
                e.position = self.position
            self.velocity = vector.objVector(0, 0)
            self.set_health(2500)
            self.fire_pattern[self.fire](self)

        if self.phase_timer > FRAME_PER_SECOND and (self.phase_timer - FRAME_PER_SECOND)%(10*FRAME_PER_SECOND) == 0:
            self.random_move()
            for doll in self.doll_group.sprites():
                doll.special_mode = True 
                doll.phase_timer = 0
        
        if self.phase_timer > FRAME_PER_SECOND and self.done:
            for e in self.parent.effect_group.sprites():
                e.die()
            self.phase_done()
            self.next_phase()
    
    def spell_004(self, child): # spell 4
        for j in range(2):
            for i in range(8):
                doll = enemy.Enemy(self.parent, 'bluesprite')
                doll.master = self
                doll.sprite_type = SPRITE_ENEMY_SPECIAL
                doll.constant_distance = 150
                doll.current_distance = 0
                doll.item_list = []
                doll.position = self.position
                doll.movement = 0
                doll.initial_angle = 360/8*i
                doll.shut_angle = 0
                doll.health = 1
                doll.invulnerable = True
                doll.rotating = True
                doll.shut_angle = 360/8*i
                doll.special_mode = False
                doll.phase_list = [self.spell_004_dollmotion]
                
                if j == 0:
                    doll.direction = 1
                    doll.barrage = ['diamond', '3']
                else:
                    doll.direction = -1
                    doll.barrage = ['diamond', '4']
                self.doll_group.add(doll)
                self.parent.effect_group.add(doll)

    def spell_004_dollmotion(self, child):
        distance_from_master = (child.position - self.position).norm
        distance_from_master += child.movement
        child.current_distance += child.movement
        if child.current_distance != distance_from_master:
            distance_from_master = child.current_distance
        child.position = vector.objVector(distance_from_master, 0)
        child.position.angle = child.initial_angle
        child.position = self.position + child.position
        child.initial_angle += 0.5*child.direction
        

        if distance_from_master <= child.constant_distance/2:
            child.movement = 1

        elif distance_from_master > child.constant_distance:
            child.movement = -1


        if not child.special_mode:
            if child.phase_timer%(0.2*FRAME_PER_SECOND) == 0:
                child.shut_angle += 10*child.direction
                b =  barrage.Barrage(child, child.barrage)
                b.position = child.position.copy()
                b.active = True
                b.mode = 0
                b.phase_list = [self.spell_004_dollfire_update]
                b.bounds = 0, 0, STAGE_WIDTH_HEIGHT[0], STAGE_WIDTH_HEIGHT[1]
                b.velocity = vector.objVector(100*MEASURE_UNIT, 0)
                b.velocity.angle = child.shut_angle
                self.parent.barrage_group.add(b)
            elif child.phase_timer%(0.1*FRAME_PER_SECOND) == 0:
                child.shut_angle += 10*child.direction
                b =  barrage.Barrage(child, child.barrage)
                b.position = child.position.copy()
                b.active = True
                b.mode = 1
                b.phase_list = [self.spell_004_dollfire_update]
                b.bounds = 0, 0, STAGE_WIDTH_HEIGHT[0], STAGE_WIDTH_HEIGHT[1]
                b.velocity = vector.objVector(100*MEASURE_UNIT, 0)
                b.velocity.angle = child.shut_angle
                self.parent.barrage_group.add(b)
        else:
            if child.phase_timer%(0.1*FRAME_PER_SECOND) == 0 and child.phase_timer < 3*FRAME_PER_SECOND:
                noise = random.randint(0, 20) - 10

                if child.barrage == ['diamond', '3']:
                    b =  barrage.Barrage(child, ['barrier', '4'])
                else:
                    b =  barrage.Barrage(child, ['barrier', '2'])
                b.position = child.position.copy()
                b.active = True
                b.bounds = 0, 0, STAGE_WIDTH_HEIGHT[0], STAGE_WIDTH_HEIGHT[1]
                aim = self.parent.player.position.copy()
                aim.x += noise
                b.velocity = aim - child.position
                b.velocity.norm = 500*MEASURE_UNIT

                bl = b.copy()
                aiml = self.parent.player.position.copy()
                aiml.x += noise - 150
                bl.velocity = aiml - child.position
                bl.velocity.norm = 500*MEASURE_UNIT

                br = b.copy()
                aimr = self.parent.player.position.copy()
                aimr.x += noise + 150
                br.velocity = aimr - child.position
                br.velocity.norm = 500*MEASURE_UNIT

                self.parent.barrage_group.add(b)
                self.parent.barrage_group.add(bl)
                self.parent.barrage_group.add(br)
            elif child.phase_timer == 4*FRAME_PER_SECOND:
                child.special_mode = False
                self.velocity = vector.objVector(0,0)
            
            if child.phase_timer == 2*FRAME_PER_SECOND:
                self.velocity = (vector.objVector(STAGE_WIDTH_HEIGHT[0]/2, STAGE_WIDTH_HEIGHT[1]/3) - self.position)/(2*FRAME_PER_SECOND)


    def spell_004_dollfire_update(self, child): # spell 4 update
        if child.mode == 1 and child.timer == 2*FRAME_PER_SECOND:
            child.speed = child.velocity.norm*2
            child.angle = child.velocity.angle
            child.velocity = vector.objVector(0,0)
        elif child.mode == 1 and child.timer == 2.5*FRAME_PER_SECOND:
            child.velocity = vector.objVector(child.speed, 0)
            child.velocity.angle = child.angle
            child.velocity *= -1
            child.velocity.angle += 60*child.parent.direction
            child.mode = 0

        child.auto_rotate()

    def motion_005(self, child): # motion 5
        if self.phase_timer == 1:
            d = item.Item(self.parent, "life")
            d.position = self.position
            self.parent.item_group.add(d)
        self.velocity = vector.objVector(300, -300)*MEASURE_UNIT


        if self.phase_timer > 3*FRAME_PER_SECOND:
            self.parent.finished = True
            self.die()

    def phase_done(self): # end phase
        self.set_health(0)
        self.invulnerable = False
        self.done = False

        for b in self.parent.barrage_group.sprites():
            d = item.Item(self.parent, "smallpoint")
            d.position = b.position
            d.collected = True
            b.die()
            self.parent.item_group.add(d)

        self.fire_pattern_temp.clear()
        
        for e in self.effect_group.sprites():
            e.die()

        for e in self.parent.enemy_group.sprites():
            e.die()

        for i in range(10):
            r = random.randint(0, 1)
            if r == 0:
                i = item.Item(self.parent, 'power')
            else:
                i = item.Item(self.parent, 'largepower')
            rx = random.randrange(-50, 50)
            ry = random.randrange(-50, 50)
            i.position = vector.objVector(self.position.x + rx, self.position.y + ry)
            self.parent.item_group.add(i)

        for i in range(10):
            r = random.randint(0, 1)
            if r == 0:
                i = item.Item(self.parent, 'point')
            else:
                i = item.Item(self.parent, 'largepoint')
            rx = random.randrange(-50, 50)
            ry = random.randrange(-50, 50)
            i.position = vector.objVector(self.position.x + rx, self.position.y + ry)
            self.parent.item_group.add(i)

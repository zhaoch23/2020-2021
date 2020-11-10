from core.player import *
from core import enemy
import random
from core import barrage


class Ruri(enemy.Enemy):
    """class Ruri"""
    def __init__(self, parent, type_id):
        """The boss in stage_three
        name (str): The name of the boss, Ruri
        position (vector): the position of Ruri
        bound_style: if there will be invincible wall
        bounds: the size of the invincible wall
        hitbox: hitbox of Ruri
        get_hit (bool): determine if player hit Ruri


        """
        super().__init__(parent, type_id)
        self.name = "SHINOMIYA RURI"
        self.position = vector.objVector(STAGE_WIDTH_HEIGHT[0] / 2, -300)  # Position
        self.bound_style = BOUND_CUSTOM
        self.bounds = 50, 50, STAGE_WIDTH_HEIGHT[0] - 50, STAGE_WIDTH_HEIGHT[1] - 50
        self.parent = parent
        self.hitbox = self.rect  # Hitbox
        self.get_hit = False  # Determine if get hit by the player
        self.parent.boss_group.add(self)
        self.item_list = []
        self.fake_random = 0

    def collide(self):
        if self.collided_with.sprite_type == SPRITE_BULLET:
            self.parent.health -= self.collided_with.damage
            self.get_hit = True

    def movement_normal(self, movement: list):
        # The different movement Ruri may have
        number = random.randint(30, 60)
        if movement == ["ENTRY"]:
            self.velocity = vector.objVector(0, 75 * MEASURE_UNIT)
            number = random.randint(0, 1)
            self.fake_random += number
        if movement == ["STAND"]:
            self.velocity = vector.objVector(0, 0)
            self.fake_random += 1
        if movement == ["LEFT"]:
            self.velocity = vector.objVector(-number * MEASURE_UNIT, 0)
            self.fake_random += 1
        if movement == ["RIGHT"]:
            self.velocity = vector.objVector(number * MEASURE_UNIT, 0)
            self.fake_random += 1
        if movement == ["BACKWARD"]:
            self.velocity = vector.objVector(0, -number * MEASURE_UNIT)
            self.fake_random += 1
        if movement == ["FORWARD"]:
            self.velocity = vector.objVector(0, number * MEASURE_UNIT)
            self.fake_random += 1
        if movement == ["LEFT", "FORWARD"]:
            self.velocity = vector.objVector(-number * MEASURE_UNIT, number * MEASURE_UNIT)
            self.fake_random += 1
        if movement == ["RIGHT", "FORWARD"]:
            self.velocity = vector.objVector(number * MEASURE_UNIT, number * MEASURE_UNIT)
            self.fake_random += 1
        if movement == ["LEFT", "BACKWARD"]:
            self.velocity = vector.objVector(-number * MEASURE_UNIT, -number * MEASURE_UNIT)
            self.fake_random += 1
        if movement == ["RIGHT", "BACKWARD"]:
            self.velocity = vector.objVector(number * MEASURE_UNIT, -number * MEASURE_UNIT)
            self.fake_random += 1

    def movement_dash(self, place: str):
        # Dashes
        self.bound_style = BOUND_CUSTOM
        if place == "ORIGIN":
            self.position = vector.objVector(STAGE_WIDTH_HEIGHT[0] / 2, STAGE_WIDTH_HEIGHT[1] / 4)
            self.fake_random += 1
        if place == "OFFSCREEN":
            self.position = vector.objVector(-300, -300)
            self.fake_random += 1
        if place == "RANDOM":
            x = random.randint(75, int(STAGE_WIDTH_HEIGHT[0] - 75))
            y = random.randint(150, int(STAGE_WIDTH_HEIGHT[1] - 150))
            self.position = vector.objVector(x, y)
            self.fake_random += 1

    # Tianyu Li no nasake
    def fire_follow(self):
        if self.fake_random % 2 == 0:
            color_one = '1'
        else:
            color_one = '2'
        enemy.Enemy.defualt_danmaku_pattern_002(self, barrage_type=['dart', color_one], count=30, delta_time=5,
                                                speed=300*MEASURE_UNIT)

    def fire_circle(self):
        if self.fake_random % 2 == 0:
            color_two = '3'
        else:
            color_two = '4'
        enemy.Enemy.defualt_danmaku_pattern_004(self, barrage_type=['dart', color_two], count1=15, count2=20,
                                                delta_time=10, speed=300*MEASURE_UNIT)

    def fire_fan(self):
        if self.fake_random % 2 == 0:
            color_three = '5'
        else:
            color_three = '6'
        enemy.Enemy.defualt_danmaku_pattern_005(self, barrage_type=['dart', color_three], count=25, delta_time=10)

    # Tianyu Li no shiken
    def fire_fastfan(self):
        if self.fake_random % 2 == 0:
            color_four = '12'
        else:
            color_four = '15'
        enemy.Enemy.defualt_danmaku_pattern_005(self, barrage_type=['dart', color_four], count=20, delta_time=5,
                                                speed=300*MEASURE_UNIT)

    def fire_snipe(self):
        if self.fake_random % 2 == 0:
            color_five = '9'
        else:
            color_five = '10'
        enemy.Enemy.defualt_danmaku_pattern_003(self, barrage_type=['dart', color_five], count=10, delta_time=10,
                                                speed=350*MEASURE_UNIT)

    # Tianyu Li no akui
    def fire_ichimoji(self):
        if self.fake_random % 2 == 0:
            color_six = '11'
        else:
            color_six = '13'
        enemy.Enemy.defualt_danmaku_pattern_001(self, barrage_type=['dart', color_six], count=45, delta_time=5,
                                                speed=300*MEASURE_UNIT)

    def fire_tornado(self, barrage_type, anchor_point_cnt=3, anchor_point_da=15):
        time = self.timer
        anchor_point_dt = 5
        anchor_point_dd = 3

        d_from_boss = 120
        b_cnt1 = 2
        b_cnt2 = 2
        b_speed = 140 * MEASURE_UNIT
        b_ds = 15 * MEASURE_UNIT

        for anchor in range(anchor_point_cnt):
            anchor_position = vector.objVector(d_from_boss, 0)
            anchor_position.angle = anchor * (360 / anchor_point_cnt)

            total_dt = 0
            for k in range(int(d_from_boss / anchor_point_dd)):
                total_dt += anchor_point_dt
                anchor_position.norm -= anchor_point_dd
                anchor_position.angle += anchor_point_da

                anchor_n_position = anchor_position.copy()
                anchor_n_position.norm -= anchor_point_dd
                anchor_n_position.angle += anchor_point_da

                dp = anchor_position - anchor_n_position

                anchor_r_position = anchor_position + self.position
                for i in range(b_cnt1):
                    for j in range(b_cnt2):
                        b = barrage.Barrage(self, barrage_type)
                        b.correct_start_position = False
                        b.position = anchor_r_position
                        b.velocity = vector.objVector(b_speed + b_ds * i * (j + 1), 0)
                        b.velocity.angle = dp.angle + 20 * j

                        try:
                            self.fire_pattern_temp[time + total_dt].append(b)
                        except:
                            self.fire_pattern_temp[time + total_dt] = []
                            self.fire_pattern_temp[time + total_dt].append(b)

    def fire_akui(self, barrage_type, direction=1):
        time = self.timer
        anchor_position = vector.objVector(-100, 0)
        anchor_cnt = 15

        b_cnt1 = 10
        b_cnt2 = 5
        b_speed1 = 100 * MEASURE_UNIT
        b_speed2 = 150 * MEASURE_UNIT
        dt = 1
        da = 180 / anchor_cnt

        for i in range(anchor_cnt):
            angle = (da * i + 90) * direction
            total_dt = i * dt
            anchor_position.angle = angle

            temp_list = []

            for j in range(b_cnt1):
                b = barrage.Barrage(self, barrage_type)
                b.position = anchor_position + self.position
                b.velocity = vector.objVector(b_speed1, 0)
                b.velocity.angle = (360 / b_cnt1) * j - 90 + da * i
                b.correct_start_position = False
                temp_list.append(b)

            for k in range(b_cnt2):
                b = barrage.Barrage(self, barrage_type)
                b.position = anchor_position + self.position
                b.velocity = vector.objVector(b_speed2, 0)
                b.velocity.angle = (180 / b_cnt2) * j - 90 + da * i
                b.correct_start_position = False
                temp_list.append(b)

            try:
                self.fire_pattern_temp[time + total_dt] = self.fire_pattern_temp[time + total_dt] + temp_list
            except:
                self.fire_pattern_temp[time + total_dt] = []
                self.fire_pattern_temp[time + total_dt] = self.fire_pattern_temp[time + total_dt] + temp_list

    def na_one(self):
        # Normal Attack One
        self.fire_follow()

    def na_two(self):
        # Normal Attack Two
        self.fire_snipe()

    def na_three(self):
        # Normal Attack Three
        self.fire_fastfan()

    def random_normal(self):
        # Random Normal Attack
        decision = random.choice([0, 1, 2])
        if decision == 0:
            return self.na_one()
        if decision == 1:
            return self.na_two()
        else:
            return self.na_three()

    def co_one(self):
        # Counter Attack

        self.fire_fan()

    def co_two(self):
        self.fire_ichimoji()

    def random_counter(self):
        decision = random.choice([0, 1])
        if decision == 1:
            return self.co_one()
        else:
            return self.co_two()

    def sp_one(self):
        # Special Attack
        color_akui = random.choice(['14', '1'])
        barrage_type = ['dart', color_akui]
        self.fire_akui(barrage_type)

    def sp_two(self):
        color_tornado = random.choice(['7', '8'])
        barrage_type = ['dart', color_tornado]
        self.fire_tornado(barrage_type)

    def sp_three(self):
        self.fire_circle()

    def random_special(self):
        decision = random.randint(0, 6)
        if decision == 0 or decision == 1:
            return self.sp_one()
        elif decision == 2 or decision == 3:
            return self.sp_two()
        else:
            return self.sp_three()


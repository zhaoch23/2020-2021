from core.game import *
from core.sprite import *
from .ruri import Ruri
import random


def load_data():
    """Load the background music in the boss fight"""
    m = utility.load_music("Ruri no Sakura")
    StageThree.MUSIC["Ruri no Sakura"] = m


class StageThree(Game):
    MUSIC = {}
    """The Forth Level (Stage Three)
        self.ruri: the boss object
        self.attack_number (list): the list of attack sequence
        self.health (int): the boss's hit points
        self.hit_by_player (int): the number of times player hit the boss
        self.sequence_sorted (bool): to see if a sequence of int is sorted
        self.phase_list (list): a list of phases of this stage
        self.player.power (int): player's attack power
        self.player.life (int): player's attack power
        self.player.can_collide (bool): if the player is invincible
        self.previous_move (int): the attack number the boss previous take
        
    """
    def __init__(self, screen, p=None):
        super().__init__(screen, p=p)
        self.ruri = Ruri(self, "kimonoruri")
        self.attack_number = []
        self.health = 8400
        self.hit_by_player = 0
        self.sequence_sorted = None
        self.decision = None
        self.phase_list = [self.phase_credit, self.entry_ruri, self.phase_zero, self.phase_one,
                           self.change, self.phase_two, self.phase_three]
        self.player.power = 5
        self.player.life = 5
        self.player.can_collide = True
        self.previous_move = None

    def counter_attack(self):
        """Counter attack movement of the boss
            Determine if the boss is going to counter attack when
            the player lands a hit
        
        """
        # counter attack
        if self.ruri.get_hit:
            self.hit_by_player += 1
            self.decision = random.choice(["attack", "not attack", "not attack"])
            # Decide if is going to attack
            if self.decision == "attack":
                self.ruri.position.x = self.player.position.x
                self.ruri.position.y = self.player.position.y - 50
                self.ruri.random_counter()
            self.ruri.get_hit = False

        self.ruri.position = vector.objVector(STAGE_WIDTH_HEIGHT[0] / 2, STAGE_WIDTH_HEIGHT[1] / 4)

    def damage_bonus(self, hits: int):
        """Bonus score calculation"""
        # Recursion for score calculating
        if hits == 0:
            self.player.score += 0
            return self.player.score
        self.player.score += 1500
        return self.player.score + self.damage_bonus(hits - 1)

    def sort_sequence(self, attack_number: list):
        # Bubble sort for rankings and attack sequence
        # in the descending order
        for times_through in range(len(attack_number) - 1):
            i = 0
            self.sequence_sorted = True
            while i < len(attack_number) - 1 - times_through:
                first = attack_number[i]
                second = attack_number[i + 1]
                if first < second:
                    temp = first
                    attack_number[i] = attack_number[i + 1]
                    attack_number[i + 1] = temp
                    self.sequence_sorted = False
                i += 1
            if self.sequence_sorted:
                return attack_number

    def rank(self, bonus: int):
        # calculate score
        ranked_score = [95000, 64000, 32000, bonus]
        self.sort_sequence(ranked_score)
        index = 0
        while index < len(ranked_score):
            if ranked_score[index] != bonus:
                index += 1
            elif ranked_score[index] == bonus:
                return index
        if index >= len(ranked_score):
            return -1

    def phase_credit(self):
        """The phase with stage name, credit, etc..."""
        if self.timer == 1:
            self.health = 8400
            title1 = text.Text(JAP_ULT, 28, (255, 255, 255), "瑠璃の夢　カタナの情け　春の花")
            title1.position = vector.objVector(STAGE_WIDTH_HEIGHT[0] / 2, STAGE_WIDTH_HEIGHT[1] / 3)
            title1.life_timer = 5 * FRAME_PER_SECOND
            title2 = text.Text(ALICE_FRONT, 24, (255, 255, 255), "Finale: The Fantasy of Shinomiya Ruri")
            title2.position = vector.objVector(STAGE_WIDTH_HEIGHT[0] / 2, STAGE_WIDTH_HEIGHT[1] / 3 + 50)
            title2.life_timer = 5 * FRAME_PER_SECOND
            title3 = text.Text(ALICE_FRONT, 20, (255, 255, 255), "Presented by Tianyu")
            title3.position = vector.objVector(STAGE_WIDTH_HEIGHT[0] / 2, STAGE_WIDTH_HEIGHT[1] / 3 + 100)
            title3.life_timer = 5 * FRAME_PER_SECOND
            self.effect_group.add(title1)
            self.effect_group.add(title2)
            self.effect_group.add(title3)

        elif self.timer == 3 * FRAME_PER_SECOND:
            self.next_phase()

    def entry_ruri(self):
        """The phase where the bgm plays, followed by
        the entrance of Ruri, the boss from the top
        of the screen"""
        if self.timer == 90:
            self.health = 8400
            self.ruri.movement_normal(["ENTRY"])
            self.ruri.bound_style = BOUND_BLOCK
        elif self.timer == 120:
            self.ruri.movement_normal(["STAND"])
            #utility.play_music(self.MUSIC["Ruri no Sakura"])
            self.next_phase()

    def phase_zero(self):
        """Phase zero: Enter when stage started
        Movements:
            attacks:
                100% normal attacks; attack_number[1]
        Exit when health is 7000
        
        """
        if self.timer == 1:
            self.attack_number = [1]
            self.ruri.movement_normal(["STAND"])
        elif self.timer == 35:
            self.ruri.movement_normal(["LEFT"])
            self.ruri.random_normal()
        elif self.timer == 70:
            self.ruri.movement_normal(["RIGHT"])
            self.ruri.random_normal()
        elif self.timer == 105:
            self.ruri.movement_normal(["STAND"])
            self.ruri.random_normal()

        if self.timer % 60 == 0:
            movement = random.choice([["LEFT"], ["RIGHT"]])
            if self.previous_move != movement:
                self.ruri.movement_normal(movement)
                self.previous_move = movement
            else:
                self.ruri.movement_normal(["STAND"])

        if self.health > 7000:
            if self.timer % 120 == 0:
                self.ruri.random_normal()

        if self.health <= 7000:
            self.ruri.sp_three()
            self.next_phase()

    def phase_one(self):
        """Phase one: Enter when health is 5600
        Movements:
            attacks:
                75% normal attacks; attack_number[1]
                25% special attacks; attack_number[2]
        Exit when health is 5600
        
        """
        if self.timer == 1:
            self.attack_number.extend((1, 1, 2))

        if self.timer % 45 == 0:
            movement_one = random.choice([["LEFT"], ["RIGHT"], ["FORWARD"], ["BACKWARD"], ["LEFT"], ["RIGHT"],
                                          ["LEFT"], ["RIGHT"], ["FORWARD"], ["BACKWARD"], ["LEFT"], ["RIGHT"],
                                          ["LEFT"], ["RIGHT"]])
            movement_two = random.choice([["RIGHT", "FORWARD"], ["LEFT", "BACKWARD"], ["RIGHT", "BACKWARD"],
                                          ["LEFT", "FORWARD"]])
            movement = random.choice([movement_one, movement_two])
            if self.previous_move != movement:
                self.ruri.movement_normal(movement)
                self.previous_move = movement
            else:
                self.ruri.movement_normal(["STAND"])

        if self.health > 5600:
            self.sort_sequence(self.attack_number)
            random.shuffle(self.attack_number)
            if self.timer % 90 == 0 and self.attack_number[0] == 1:
                self.ruri.random_normal()
            if self.timer % 210 == 0 and self.timer % 90 != 0:
                self.ruri.random_special()
            self.sort_sequence(self.attack_number)
            # The first number is the attack that is going to use

        if self.health <= 5600:
            self.ruri.random_special()
            self.next_phase()

    def change(self):
        """The phase where Ruri vanishes and change appearance"""
        self.ruri.movement_dash("OFFSCREEN")
        self.ruri.die()
        if self.timer == 120:
            self.ruri = Ruri(self, "katanaruri")
            self.ruri.movement_dash("ORIGIN")
            self.ruri.sp_three()
            self.ruri.movement_dash("RANDOM")
            self.ruri.sp_two()
            self.ruri.movement_dash("ORIGIN")
            self.ruri.sp_one()
            self.next_phase()

    def phase_two(self):
        """Phase two: Enter when health is 4800
        Movements:
            attacks:
                65% normal attacks; attack_number[1]
                35% special attacks; attack_number[2]
        Exit when health is 4200
        
        """
        if self.timer == 1:
            if self.player.power < 5:
                self.player.power = 5
            self.attack_number.extend((1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
            self.attack_number.extend((2, 2, 2, 2, 2, 2))
        # attack number = 1 * 13 and 2 * 7
        if self.timer % 120 == 0:
            movement = random.choice(["RANDOM", "RANDOM", "RANDOM", "ORIGIN"])
            self.ruri.movement_dash(movement)

        if self.health > 4200:
            random.shuffle(self.attack_number)
            if self.timer % 90 == 0 and self.attack_number[0] == 1:
                self.ruri.random_normal()
            if self.timer % 150 == 0 and self.timer % 90 != 0:
                self.ruri.random_special()
            self.sort_sequence(self.attack_number)
            # The first number is the attack that is going to use

        if self.health <= 4200:
            self.next_phase()

    def phase_three(self):
        """Phase three: Enter when health is 3000
        Movements:
            attacks:
                55% normal attacks; attack_number[1]
                45% special attacks; attack_number[2]
        Exit when health is 0
        
        """
        if self.timer == 1:
            self.attack_number.remove(1)
            self.attack_number.remove(1)
            self.attack_number.extend((2, 2))

        if self.timer % 90 == 0:
            movement = random.choice(["RANDOM", "RANDOM", "RANDOM", "ORIGIN"])
            self.ruri.movement_dash(movement)
            self.ruri.random_normal()

        if self.health > 0:
            # attack number = 1 * 11 and 2 * 9
            random.shuffle(self.attack_number)
            if self.timer % 60 == 0 and self.attack_number[0] == 1:
                self.ruri.random_normal()
            if self.timer % 120 == 0 and self.timer % 90 != 0:
                self.ruri.random_special()
                # The first number is the attack that is going to use
            self.sort_sequence(self.attack_number)

        if self.health <= 0:
            self.ruri.movement_dash("OFFSCREEN")

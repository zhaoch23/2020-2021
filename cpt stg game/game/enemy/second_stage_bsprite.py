from core.enemy import *
import random

class SSBlueSprite(Enemy):
    """
    This class represents a specific type of BlueSprite 
    that initially move randomly.
    It inherits from class Enemy.

    Attributes:
        name(str): the name of this mob.
    """
    name = 'blue'

    def __init__(self, parent):
        """
        This method initializes BlueSprite initial object.

        Args:
            parent (stage): A stage(any class that represents a stage in the game) object 
            that inherits from the game.
        
        Attributes:
            position (objvector): The initial position of the enemy.
            bound (tuple): Bound which this sprite can stay in.
            health (int): Health of this sprite.
            phase_list (list): List of this BlueSprites motions.
        """
        super().__init__(parent, type_id='bluesprite')
        self.position = vector.objVector(0, 0)
        self.bounds = -50, -50, STAGE_WIDTH_HEIGHT[0]+50, STAGE_WIDTH_HEIGHT[1]+50
        self.health = 100
        self.phase_list = [self.motion_one, self.motion_two, self.motion_three]

    def motion_one(self, child):
        """
        This method assigns a specific motion to the child.
        This specific motion moves child randomly and orders the child to fire 
        every 10 seconds of the phase timer. 
        After the phase timer reaches 30 seconds, it move to the next motion.
        
        Args:
            child(Enemy): Enemy invoved with this action.
        """
        self.velocity = vector.objVector(0, 50*MEASURE_UNIT)
        self.velocity.set_angle(random.randint(0, 360))
        if self.phase_timer % 10 == 0:
            self.fire_pattern[self.fire](self)
        self.phase_timer += 1
        if self.phase_timer >= 5*FRAME_PER_SECOND:
            self.next_phase()
            self.next_fire()
    
    def motion_two(self, child):
        """
        This method assigns a sepcific motion to the child.
        This specific motion moves the child randomly in a random direction.
        The child fires every 15 seconds.
        Then it would move on to the next phase if the phase timer is over 35 seconds.
        
        Args:
            child(Enemy): Enemy invoved with this action.
        """

        self.velocity.set_angle(random.randint(0, 360))
        self.velocity.norm = 100*MEASURE_UNIT
        if self.phase_timer % 15 == 0:
            self.fire_pattern[self.fire](self)
        self.phase_timer += 1
        if self.phase_timer >= 10*FRAME_PER_SECOND:
            self.next_phase()
            self.next_fire()

    def motion_three(self, child):
        """
        This method assigns a specific motion to the child.
        This specific motion simply speeds up the child in one direction.
        it fires every 10 seconds.
        
        Args:
            child(Enemy): Enemy invoved with this action.
        """
        self.velocity.norm = 120*MEASURE_UNIT
        if self.phase_timer % 10 == 0:
            self.fire_pattern[self.fire](self)

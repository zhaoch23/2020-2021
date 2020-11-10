from core.enemy import *
import random 

class HorizontalRedSprite(Enemy):
    """
    This class represents a specific type of RedSprite 
    that initially move horizontally.
    It inherits from class Enemy.

    Attributes:
        name(str): the name of this mob.
    """
    name = 'red'

    def __init__(self, parent):
        """
        This method initializes HorizontalRedSprite initial object.

        Args:
            parent(stage): A stage(any class that represents a stage in the game) object 
            that inherits from the game.
        
        Attributes:
            position(objvector): position of this mob.
            bounds(tuple): boundary for this mob
            health(int): hp of this mob.
            phase_list(list): List of this RedSprites motions.
            

        """
        super().__init__(parent, type_id='redsprite')
        self.position = vector.objVector(0, 0)
        self.bounds = -50, -50, STAGE_WIDTH_HEIGHT[0]+50, STAGE_WIDTH_HEIGHT[1]+50
        self.health = 100
        self.phase_list = [self.motion_zero, self.motion_one, self.get_random_angle, self.motion_two, self.get_random_angle, self.motion_three]
    
    def motion_zero(self, child):
        """
        This function sets initial direction of the redsprite.

        Args:
            child(Enemy): Enemy invoved with this action.
        """
        move_list = [60*MEASURE_UNIT, -60*MEASURE_UNIT]
        self.velocity = vector.objVector(move_list[random.randint(0, 1)], 0)
        self.next_phase()
    
    def motion_one(self, child):
        """
        This method assigns a specific motion to the child.
        This specific motion moves child horizontally and orders the child to fire 
        every 30 seconds of the phase timer. 
        After the phase timer reaches 120 seconds, it move to the next motion.
        
        Args:
            child(Enemy): Enemy invoved with this action.
        """
        if self.phase_timer > 0 and self.phase_timer % FRAME_PER_SECOND == 0:
            self.fire_pattern[self.fire](self)
            self.phase_timer += 1
        # This mob intends to move left and right
        # if self.position.x >= STAGE_WIDTH_HEIGHT[0]:
        #     self.position[0] -= 2
        #     self.velocity *= -1, 1
        # elif self.position.x <= 0:
        #     self.position[0] += 2
        #     self.velocity *= -1, 1

        if self.phase_timer > 5*FRAME_PER_SECOND:
            self.next_phase()
            self.next_fire()
        
    def motion_two(self, child):
        """
        This method assigns a sepcific motion to the child.
        This specific motion moves the child randomly in a random direction.
        The child fires every 20 seconds and if the child went over half of the screen vertically
        Then it would move on to the next phase if the phase timer is over 200 seconds.
        
        Args:
            child(Enemy): Enemy invoved with this action.
        """
        # Moves randomly and fire faster
        if self.phase_timer > 0 and self.phase_timer % (FRAME_PER_SECOND//2) == 0:
            self.fire_pattern[self.fire](self)
            self.phase_timer += 1
        if self.phase_timer > 10*FRAME_PER_SECOND and self.position.y >= STAGE_WIDTH_HEIGHT[1]/2:
            self.next_phase()
            self.next_fire()
    
    def get_random_angle(self, child):
        """
        This function sets a random angle to the horizontalredsprite.

        Args:
            child(enemy): enemy involved with this change of angle.
        """
        self.velocity.set_angle(random.randint(0, 360))
        self.next_phase()

    def motion_three(self, child):
        """
        This method assigns a specific motion to the child.
        This specific motion simply speeds up the child in one direction.
        
        Args:
            child(Enemy): Enemy invoved with this action.
        """
        self.velocity.norm = 250*MEASURE_UNIT


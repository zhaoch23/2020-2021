from typing import List
import math

class Ship(object):

    def __init__(self, x, y, z, firepower):
        self.x = x
        self.y = y
        self.z = z
        self.firepower = firepower
    
    def get_distance(self) -> float:
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def get_threat(self) -> float:
        return self.firepower*3/self.get_distance()

    
def sort(ships: List[Ship]) -> List[Ship]:
    for i in range(len(ships) - 1):
        sorted = True
        for j in range(len(ships) - i - 1):
            if ships[j].get_threat() < ships[j + 1].get_threat():
                ships[j], ships[j + 1] = ships[j + 1], ships[j]
                sorted = False
        
        if sorted == True:
            break
    
    i = ships(list) - 1
    while i >= 0:
        if ships[i].get_distance() > 50:
            del ships[i]
        i -= 1

    return ships

from typing import List
import math
import os

class Ship(object):

    def __init__(self, x, y, z, firepower):
        self.x = x
        self.y = y
        self.z = z
        self.firepower = firepower
    
    def __repr__(self):
        return f"{self.get_threat()}"

    def get_distance(self) -> float:
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def get_threat(self) -> float:
        return self.firepower*3/self.get_distance()

def sort_a(ships: List[Ship]) -> List[Ship]:#sort based on distance
    for i in range(len(ships) - 1):
        sorted = True
        for j in range(len(ships) - i - 1):
            if ships[j].get_distance() < ships[j + 1].get_distance():
                ships[j], ships[j + 1] = ships[j + 1], ships[j]
                sorted = False
        
        if sorted == True:
            break
    
    return ships


def sort_b(ships: List[Ship]) -> List[Ship]:#sort based on threat
    for i in range(len(ships) - 1):
        sorted = True
        for j in range(len(ships) - i - 1):
            if ships[j].get_threat() < ships[j + 1].get_threat():
                ships[j], ships[j + 1] = ships[j + 1], ships[j]
                sorted = False
        
        if sorted == True:
            break
    
    return ships


def search(ships: List[Ship]) -> List[Ship]:#search based on distance
    i = len(ships) - 1
    while i >= 0:
        if ships[i].get_distance() > 50:
            del ships[i]
        i -= 1

    return ships



def final(ships: List[Ship]) -> List[Ship]:
    return search(sort_b(ships))


if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    os.chdir(path)

    os.system('pytest test_main.py')
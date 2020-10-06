import os
from typing import List

class Animal:
    def __init__(self, genus:str, specific_name:str, name:str):
        self.genus = genus
        self.specific_name = specific_name
        self.name = name

    def get_species(self) -> str:
        return f'{self.genus[0]}. {self.specific_name}'
    
    def get_binomial(self) -> str:
        return f'{self.genus} {self.specific_name}'
    
    def __repr__(self) -> str:
        return f'{self.name} ({self.get_species()})'

class Sprite:
    def __init__(self, postion:List[int], speed:List[int], image_path:str, width:int, height:int):
        self.position = postion
        self.speed = speed
        self.image_path = image_path
        self.width =width
        self.height = height
    
    def get_x(self) -> int:
        return self.position[0]
    def set_x(self, value:int) -> None:
        self.x = value
    x = property(get_x, set_x)
    
    def get_y(self) -> int:
        return self.position[1]
    def set_y(self, value:int) -> None:
        self.y = value
    y = property(get_y, set_y)

    def get_size(self) -> List[int]:
        return [self.width, self.height]
    
    def update(self) -> None:
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]


if __name__ == "__main__":
    os.system("pytest test_animal.py")
    os.system("pytest test_sprite.py")

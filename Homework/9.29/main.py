class Animal:

    def __init__(self, genus:str, species:str):
        super().__init__()
        self.genus = genus
        self.species = species
    
    def __str__(self):
        return self.genus, self.species

class Student:

    def __init__(self, name:str, email:str, grades:int):
        super().__init__()
        self.name = name
        self.email = email
        self.grades = grades

    def __str__(self):
        return self.name, self.email, self.grades

def main_():
    animal = Animal('1', '2')
    student = Student('1', '2', 3)
    print(animal, student)


class CarDealership:

    def __init__(self, name:str, manager: Person, cars_for_sale: list[Car]):
        self.name = name
        self.manager = manager
        self.cars_for_sale = cars_for_sale

    def __str__(self):
        return self.name, self.manager, self.cars_for_sale


class Person:

    def __init__(self, name:str, email:str):
        self.name = name
        self.email = email
    
    def __str__(self):
        return self.name, self.email


class Car:

    def __init__(self, make:str, model:str, engine: Engine):
        self.make = make
        self.model = model
        self.engine =  engine

    def __str__(self):
        return self.make, self.model, self.engine

class Engine:

    def __init__(self, manufactor:str, model:str, horse_power:int):
        self.manufactor = manufactor
        self.model = model
        self.horse_power = horse_power
    
    def __str__(self):
        return self.manufactor, self.model, self.horse_power

def main():
    pass


if __name__ == "__main__":
    main()
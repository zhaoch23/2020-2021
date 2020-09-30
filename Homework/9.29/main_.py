class CarDealership:

    def __init__(self, name:str, manager: Person, cars_for_sale: list[Car], income:float):
        self.name = name
        self.manager = manager
        self.cars_for_sale = cars_for_sale
        self.income = income

    def __str__(self):
        return self.name, self.manager, self.cars_for_sale
    
    def sell_cars(self, car: Car, price: float):
        if car in self.cars_for_sale:
            self.cars_for_sale.remove(car)
            self.income += price

class Person:

    def __init__(self, name:str, email:str, health:int):
        self.name = name
        self.email = email
        self.health = health
    
    def __str__(self):
        return self.name, self.email

    def eat(self):
        self.health += 10

class Car:

    def __init__(self, make:str, model:str, engine: Engine):
        self.make = make
        self.model = model
        self.engine =  engine

    def __str__(self):
        return self.make, self.model, self.engine

    def change_engine(self, new_engine:Engine):
        self.engine = new_engine

class Engine:

    def __init__(self, manufactor:str, model:str, horse_power:int):
        self.manufactor = manufactor
        self.model = model
        self.horse_power = horse_power
    
    def __str__(self):
        return self.manufactor, self.model, self.horse_power

    def update_horsepower(self, new_horse_power):
        self.horse_power = new_horse_power

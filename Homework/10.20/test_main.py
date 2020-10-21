from main import *

def test():
    a = Ship(10,20,30,5)
    b = Ship(20,10,50,7)
    c = Ship(90,50,10,100)

    ships = [a,b,c]
    assert final(ships) == [b, a]

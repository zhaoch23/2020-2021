from main import Animal


def test_animal_init():
    a = Animal("Canis", "Lupis", "Fluffy")
    assert a.genus == "Canis"
    assert a.specific_name == "Lupis"
    assert a.name == "Fluffy"
    
    a = Animal("Homo", "Sapiens", "Jeff")
    assert a.genus == "Homo"
    assert a.specific_name == "Sapiens"
    assert a.name == "Jeff"


def test_animal_get_species():
    a = Animal("Canis", "Lupis", "Fluffy")
    assert a.get_species() == "C. Lupis"
    
    a = Animal("Homo", "Sapiens", "Jeff")
    assert a.get_species() == "H. Sapiens"


def test_animal_get_binomial():
    a = Animal("Canis", "Lupis", "Fluffy")
    assert a.get_binomial() == "Canis Lupis"
    
    a = Animal("Homo", "Sapiens", "Jeff")
    assert a.get_binomial() == "Homo Sapiens"


def test_animal_str():
    a = Animal("Canis", "Lupis", "Fluffy")
    assert str(a) == "Fluffy (C. Lupis)"
    
    a = Animal("Homo", "Sapiens", "Jeff")
    assert str(a) == "Jeff (H. Sapiens)"

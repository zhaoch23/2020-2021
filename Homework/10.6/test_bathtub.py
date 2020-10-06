from main import Bathtub

def test_bathtub_init():
    b = Bathtub(100)
    assert b.max_capacity == 100
    assert b.drain_plugged == False

    b = Bathtub(200)
    assert b.max_capacity == 200
    assert b.drain_plugged == False

def test_bathtub_drain_plug():
    b = Bathtub(200)

    b.plug_drain()
    assert b.drain_plugged is True

    b.unplug_drain()
    assert b.drain_plugged is False

    b.plug_drain()
    assert b.drain_plugged is True

def test_bathtub_set_faucet():
    b = Bathtub(200)

    b.set_faucet(1)
    assert b.faucet_flow == 1

    b.set_faucet(0.2)
    assert b.faucet_flow == 0.2
    
def test_bathtub_is_full():
    b = Bathtub(100)

    b.volume = 100
    assert b.is_full() is True

    b.volume -= 50
    assert b.is_full() is False

def test_bathtub_is_being_filled():
    b = Bathtub(100)

    b.volume = 50
    assert b.is_being_filled() is False

    b.plug_drain()
    assert b.is_being_filled() is True

    b.volume += 100
    assert b.is_being_filled() is False
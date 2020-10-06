from main import Sprite


def test_spirit_init():
    s = Sprite([0,0], [1,1], 'image.png', 100, 100)
    assert s.speed == [1,1]
    assert s.position == [0,0]
    assert s.image_path == 'image.png'

def test_get_x():
    s = Sprite([0,0], [1,1], 'image.png', 100, 100)
    assert s.x == 0
    assert s.y == 0    

def test_get_size():
    s = Sprite([0,0], [1,1], 'image.png', 100, 100)
    assert s.get_size() == [100, 100]

def test_update():
    s = Sprite([0,0], [1,1], 'image.png', 100, 100)
    s.update()
    assert s.x == 1
    assert s.y == 1
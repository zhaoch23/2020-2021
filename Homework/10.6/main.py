import os

work_path = os.path.abspath(os.path.dirname(__file__))
os.chdir(work_path)

class Bathtub(object):

    def __init__(self, max_capacity: int, volume: int=0,
                       faucet_flow: float=0.0, drain_plugged: bool=False):
        self.max_capacity = max_capacity
        self.volume = volume
        self.faucet_flow = faucet_flow
        self.drain_plugged = drain_plugged
    
    def plug_drain(self) -> None:
        self.drain_plugged = True
    
    def unplug_drain(self) -> None:
        self.drain_plugged = False
    
    def set_faucet(self, persent_flow:float) -> None:
        assert 1.0 >= persent_flow >= 0.0, 'persent flow must from 0.0 to 1.0'
        self.faucet_flow = persent_flow

    def is_full(self) -> bool:
        if self.volume >= self.max_capacity:
            return True
        else:
            return False
    
    def is_being_filled(self) -> bool:
        if not self.is_full() and self.drain_plugged:
            return True
        else:
            return False


class Pen(object):

    def __init__(self, color: str, is_activated: bool=False):
        self.color = color
        self.is_activated = is_activated
    
    def click_top_button(self) -> None:
        if self.is_activated:
            self.is_activated = False
        else:
            self.is_activated = True
    
    def draw_line(self, length:int) -> str:
        if self.is_activated:
            line = '-'*length
            return  f'{line} ({self.color})'
        else:
            return ''



if __name__ == "__main__":
    os.system("pytest test_pen.py")
    os.system("pytest test_bathtub.py")

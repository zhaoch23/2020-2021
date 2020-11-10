from ui import text
from utils import vector
from utils.settings import *


class Option(text.Text):


    def __init__(self, font_type, font_size=12, color=(0, 0, 0), text='', event=None, life_timer=-1, text_index=0, alignment=CENTER_MIDDLE):
        super().__init__(font_type, font_size = font_size, color = color, text = text, life_timer = life_timer, text_index = text_index, alignment = alignment)
        self.event = event

        self.image.set_alpha(138)
        self.selection = False # if this is selected
        self.updated = False # if the option is updated
    
    def __str__(self):
        return self.text

    def update(self):
        #update selection, can be reload
        if self.selection and not self.updated:
            self.image.set_alpha(255)
            self.position += vector.objVector(-50, 0)
            self.updated = True

        elif not self.selection and self.updated:
            self.reduction()
            self.updated = False

        super().update()

    def reduction(self):#reduct to original form
        self.position += vector.objVector(50, 0)
        self.image.set_alpha(138)


    def trigger(self, parent):
        if self.event == EVENT_QIUT_GAME:
            pygame.quit()
            exit()
        
        return self.event

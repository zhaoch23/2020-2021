from utils.settings import *
from . import text
from utils import vector
from core import image

class ScoreBoard(object):

    CONTENT = []
    BACKGROUND_IMAGE = []

    @classmethod
    def load_data(cls): # load data
        item1 = [ENG_FONT_PATH, 30, COLOR_WHITE, ["SCORE", [650, 50]]]
        item2 = [ENG_FONT_PATH, 30, COLOR_WHITE, ["HISCORE", [650, 100]]]
        item3 = [ENG_FONT_PATH, 30, COLOR_WHITE, ["LIFE REMAINS", [650, 200]]]
        item4 = [ENG_FONT_PATH, 30, COLOR_WHITE, ["POWER", [650, 250]]]
        item5 = [ENG_FONT_PATH, 30, COLOR_WHITE, ["POINT", [650, 300]]]
        item6 = [ENG_FONT_PATH, 30, COLOR_WHITE, ["GRAZE", [650, 350]]]
        item7 = [ENG_FONT_PATH, 30, COLOR_WHITE, ["FPS", [650, 400]]]
        cls.CONTENT = [item1, item2, item3, item4, item5, item6, item7]
        image1 = ["background0", [SCREEN_WIDTH/2,SCREEN_HEIGHT/2], 0.33, 0, 255]
        cls.BACKGROUND_IMAGE.append(image1)


    def __init__(self, parent): # init
        self.parent = parent

        self.content_list = pygame.sprite.Group()
        self.numbers = pygame.sprite.Group()
        self.image = pygame.sprite.Group()

        '''
        setting of scoreboard. like colour, textfont, and adding variables
        including life remains, power, point, graze, fps
        '''
        
        if self.BACKGROUND_IMAGE:
            for b in self.BACKGROUND_IMAGE:
                i = image.Image(b[IMAGE_NAME], b[IMAGE_SCALE],b[IMAGE_ROTATION], b[IMAGE_DIM])
                i.position = vector.objVector(b[IMAGE_POSITION])

                self.image.add(i)

        idx = 0
        for t in self.CONTENT:
            temp_text = text.Text(t[TEXT_FONT], t[TEXT_SIZE], t[TEXT_COLOR], t[TEXT_DETIALS][TEXT_TEXT])
            temp_text.position = vector.objVector(t[TEXT_DETIALS][TEXT_VECTOR])
            temp_text.text_index = idx
            temp_text.alignment = CENTER_LEFT
            if idx <= 1:
                number = text.Text(NUM_FONT_PATH, t[TEXT_SIZE], t[TEXT_COLOR], "000000")

                number.position = vector.objVector(t[TEXT_DETIALS][TEXT_VECTOR])
                number.position.x += 300
                number.position.y -= 10
                number.alignment = CENTER_RIGHT
                
                self.numbers.add(number)

            if idx == 2:
                number = text.Text(NUM_FONT_PATH, t[TEXT_SIZE], t[TEXT_COLOR], "00")

                number.position = vector.objVector(t[TEXT_DETIALS][TEXT_VECTOR])
                number.position.x += 300
                number.position.y -= 10
                number.alignment = CENTER_RIGHT

                self.numbers.add(number)


            if idx == 3:
                number = text.Text(NUM_FONT_PATH, t[TEXT_SIZE], t[TEXT_COLOR], "0.00/5.00")

                number.position = vector.objVector(t[TEXT_DETIALS][TEXT_VECTOR])
                number.position.x += 300
                number.position.y -= 10
                number.alignment = CENTER_RIGHT

                self.numbers.add(number)

            if idx == 4:
                number = text.Text(NUM_FONT_PATH, t[TEXT_SIZE], t[TEXT_COLOR], "000000")

                number.position = vector.objVector(t[TEXT_DETIALS][TEXT_VECTOR])
                number.position.x += 300
                number.position.y -= 10
                number.alignment = CENTER_RIGHT

                self.numbers.add(number)

            if idx == 5:
                number = text.Text(NUM_FONT_PATH, t[TEXT_SIZE], t[TEXT_COLOR], "000000")

                number.position = vector.objVector(t[TEXT_DETIALS][TEXT_VECTOR])
                number.position.x += 300
                number.position.y -= 10
                number.alignment = CENTER_RIGHT
                
                self.numbers.add(number)
            
            if idx == 6:
                number = text.Text(NUM_FONT_PATH, t[TEXT_SIZE], t[TEXT_COLOR], "0.00")

                number.position = vector.objVector(t[TEXT_DETIALS][TEXT_VECTOR])
                number.position.x += 300
                number.position.y -= 10
                number.alignment = CENTER_RIGHT
                
                self.numbers.add(number)

            self.content_list.add(temp_text)
            idx += 1

    def update(self):
        # scoreboard update
        self.image.update()
        self.content_list.update()
        
        if self.parent.player.score <= 999999:
            self.numbers.sprites()[0].set_text("{:0>6}".format(round(self.parent.player.score)))
        if self.parent.player.life:
            self.numbers.sprites()[2].set_text("{:0>2}".format(self.parent.player.life))
        if self.parent.player.power <= 999:
            self.numbers.sprites()[3].set_text("{:.2f}/5.00".format(self.parent.player.power))
        if self.parent.player.point <= 999999:
            self.numbers.sprites()[4].set_text("{:0>4}/100".format(self.parent.player.point))
        if self.parent.player.graze <= 999999:
            self.numbers.sprites()[5].set_text("{:0>6}".format(self.parent.player.graze))

        self.numbers.sprites()[6].set_text("{:.2f}".format(self.parent.clock.get_fps()))

        self.numbers.update()

    def show(self, screen):
        # show scoreboard
        screen.fill(FILL_COLOR)

        self.content_list.update()
        self.image.update()

        self.image.draw(screen)
        self.content_list.draw(screen)
        self.numbers.draw(screen)

        

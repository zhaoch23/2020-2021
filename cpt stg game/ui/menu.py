import copy
import pygame

from core import sprite, animation, image
from ui import text, option
from utils import utility, vector
from utils.settings import *


class Menu(object):

    def __init__(self, 
                 screen,
                 title, 
                 option_list,
                 image_list=None,
                 music=None,
                 background=None,
                 start_selection=0,
                 alignment=CENTER_MIDDLE):
        '''Parent class of menu object, to create and show
        Args:
        screen,
        title(list)
        option_list
        image_list=None,
        music=None
        start_selection=0
        alignment= CENTER_MIDDLE

        Example of title:
        [font, size, color, [text, [x, y]]]

        Example of option_list:
        [
            font: str(defualted in setting),
            size: float,
            color: triple of RGB,
            [
                [
                    text1: str,
                    [x: float, y: float],
                    event: int(defualted in setting)
                ],
                [
                    text2: str,
                    [x: float, y: float],
                    event2: int(defualted in setting)                    
                ]
            ]
        ]
        
        Example of image_list:
        [
            [
                name: str,
                [x, y],
                scale,
                rotation,
                dim
            ]
        ]

        '''
        #local varibles
        self.screen = screen
        self.title = title
        self.option_list = option_list
        self.image_list = image_list
        self.music = music
        self.menu_selection = start_selection
        self.alignment = alignment

        self.option_group = pygame.sprite.Group()
        self.image_group = pygame.sprite.Group()
        self.clock = pygame.time.Clock()#clock
        self.menu_active = True

        self.background = background


        #set up menu
        pygame.mouse.set_visible(False)

        self.set_up()
        self.custom_set_up()
    
    def __bool__(self):
        return self.menu_active

    def set_up(self):
        #set title
        title = self.title
        self.menu_title = text.Text(title[TEXT_FONT], title[TEXT_SIZE], title[TEXT_COLOR],
                                        title[TEXT_DETIALS][TEXT_TEXT])
        self.menu_title.position = vector.objVector(title[TEXT_DETIALS][TEXT_VECTOR])
        self.menu_title.alignment = CENTER_MIDDLE

        #set options
        if self.option_list:
            for opt in self.option_list[TEXT_DETIALS]:
                o = option.Option(self.option_list[TEXT_FONT], self.option_list[TEXT_SIZE],
                                        self.option_list[TEXT_COLOR], opt[OPT_TEXT], opt[OPT_EVENT])
                o.alignment = self.alignment
                o.position = vector.objVector(opt[OPT_VECTOR])
                self.option_group.add(o)
        

        
        #pictures:
        if self.image_list:
            for i in self.image_list:
                im = image.Image(i[IMAGE_NAME], i[IMAGE_SCALE], i[IMAGE_ROTATION], i[IMAGE_DIM])
                im.position = vector.objVector(i[IMAGE_POSITION])
                self.image_group.add(im)


    def show(self):
        #draw and update
        self.fade_in_animation()
        
        while True:
            if self.menu_active:
                if self.background:
                    self.screen.blit(self.background, self.background.get_rect())
             
                #update texts
                self.menu_title.update()
                self.option_group.update()
                self.image_group.update()

                result = self.custom_update()#return if special statement traggered
                if result:
                    return result


                # Draw stuff
                self.image_group.draw(self.screen)
                self.custom_draw(self.screen)
                self.option_group.draw(self.screen)
                self.menu_title.show(self.screen)


                # Determine the option selected
                selection = self.option_group.sprites()[self.menu_selection]
                for option in self.option_group.sprites():
                    option.selection = False
                selection.selection = True
                
                pygame.display.update()                    
                pygame.display.flip()

                # Command events:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and (event.key == KEY_DOWN or event.key == KEY_RIGHT):
                        self.menu_selection += 1
                        if self.menu_selection > len(self.option_group.sprites()) - 1:
                            self.menu_selection = 0
                    
                    elif event.type == pygame.KEYDOWN and (event.key == KEY_UP or event.key == KEY_LEFT):
                        self.menu_selection -= 1

                        if self.menu_selection < 0:
                            self.menu_selection = len(self.option_group.sprites()) - 1
                        
                    
                    elif event.type == pygame.KEYDOWN and (event.key == KEY_SHUT or event.key == pygame.K_RETURN):
                        return selection.trigger(self)
                        
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    self.custom_event(event)
                self.clock.tick(FRAME_PER_SECOND)
    
    def fade_in_animation(self):
        pass
    
    def custom_set_up(self):
        self.play_animation = True
        self.opacity = True

    def custom_draw(self, *kargs):
        pass

    def custom_update(self):
        if self.play_animation and len(self.image_group.sprites()) >= 1:

            for opt in self.option_group.sprites():
                opt.image.set_alpha(self.opacity)
            self.menu_title.image.set_alpha(self.opacity+70)

            if self.opacity >= 180:
                self.menu_active = True
                self.play_animation = False
                self.option_group.sprites()[self.menu_selection].image.set_alpha(255)
            else:
                self.opacity += 10
                self.clock.tick(FRAME_PER_SECOND)


    def custom_event(self, *args):
        # custom event
        pass


title_example = [
    ENG_FONT_PATH,
    60,
    COLOR_WHITE,
    [
        'MIDNIGHT SEPTET',
        [750, 275]
    ]

]

option_example = [
    ENG_FONT_PATH,
    45,
    COLOR_WHITE,
    [
        [
            'START',
            [900, 400],
            EVENT_NEXT
            ],
            ['OPTION',
            [900, 500],
            EVENT_SKIP
            ],
            ['GALLERY',
            [900, 600],
            EVENT_SKIP
            ],
            ['QUIT',
            [900, 700],
            EVENT_QIUT_GAME
            ]
        ]
    ]

image_example = [    
    [
        'background0',
        [SCREEN_WIDTH/2,SCREEN_HEIGHT/2],
        0.33,
        0,
        255
    ]
]

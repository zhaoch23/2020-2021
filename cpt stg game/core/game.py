from ui import menu, text, score_board
from utils import utility, vector
from utils.utility import *
from game import alice
from . import player
from ui import menu
import time


class Game(object):

    def __init__(self, screen, p: int=None):#p是玩家角色, p is player character
        self.screen = screen

        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.barrage_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.boss_group = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()
        self.effect_group = pygame.sprite.Group()
        self.bomb_group = pygame.sprite.Group()

        if  p == ALICE:
            alice.load_data()
            self.player = alice.Alice(self)
            self.player_group.add(self.player)
        else:
            self.player = p
            self.player.parent = self
            self.player_group.add(self.player)


        self.score_board = score_board.ScoreBoard(self)
        self.phase_list = [self.phase_zero, self.stage_end] # a list contents all phases, object type function
        self.timer = 0
        self.stage_timer = 0
        self.phase = 0
        self.clock = pygame.time.Clock()

        self.finished = False
    
    def phase_zero(self):
        pass   

    def stage_end(self):
        pass

    def next_phase(self):
        self.phase += 1
        self.timer = 0 

    def update(self):
        self.enemy_group.update()
        self.boss_group.update()
        self.player_group.update()
        self.bullet_group.update()
        self.item_group.update()
        self.score_board.update()
        self.effect_group.update()
        self.barrage_group.update()
        self.bomb_group.update()
    
    def draw(self):
        surface = pygame.Surface(STAGE_WIDTH_HEIGHT)
        surface.fill(COLOR_BLACK)
        self.effect_group.draw(surface)
        self.bullet_group.draw(surface)
        self.score_board.show(self.screen)
        self.effect_group.draw(surface)
        self.item_group.draw(surface)
        self.player.show(surface)
        self.boss_group.draw(surface)
        self.barrage_group.draw(surface)
        self.enemy_group.draw(surface)
        self.bomb_group.draw(surface)
        
        self.screen.blit(surface, STAGE_RECT)

    def check_collision(self):
        if self.player.active:
            self.player.check_collision(self.enemy_group)
            self.player.check_collision(self.boss_group)
            self.player.check_collision(self.barrage_group)
            self.player.check_collision(self.item_group)
        
        for bomb in self.bomb_group:
            bomb.check_collision(self.barrage_group)

        for boss in self.boss_group:
            boss.check_collision(self.bullet_group)
            boss.check_collision(self.bomb_group)
        
        for enemy in self.enemy_group:
            enemy.check_collision(self.bullet_group)
            enemy.check_collision(self.bomb_group)


    def run(self):
        while True:
            
            self.update()
            self.draw()
            self.check_collision()

            if self.finished:
                return self.stage_end()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    utility.dim(128)
                    
                    screen = self.screen.copy()
                    result = menu.Menu(self.screen, PAUSE_TITLE, PAUSE_OPTIONS, background=screen, alignment=CENTER_RIGHT).show()
                    if result == EVENT_SKIP:
                        pass

                    elif result == EVENT_RESTART:
                        return EVENT_RESTART

                    elif result == EVENT_QIUT:
                        return EVENT_QIUT
            
            if self.player.dead:
                utility.dim(128)
                
                screen = self.screen.copy()
                result = menu.Menu(self.screen, DEATH_TITLE, DEATH_OPTIONS, background=screen, alignment=CENTER_RIGHT).show()
                if result == EVENT_SKIP:
                    pass

                elif result == EVENT_RESTART:
                    return EVENT_RESTART

                elif result == EVENT_QIUT:
                    return EVENT_QIUT

            self.phase_list[self.phase]()
            if self.stage_timer % FRAME_PER_SECOND == 0:
                self.player.score += 1
        

            self.stage_timer += 1
            self.timer += 1

            self.clock.tick(FRAME_PER_SECOND)
            pygame.display.update()
            pygame.display.flip()

    def stage_end(self):
        pass

def phase_one(parent):
    parent.phase_end = True
    pass

def stage_end(self):
    # status_remain is a keyword

    class Remains:
        def __init__(self, char: str, life_remain: int, magic_remain: int):
            self._char = char
            self._life = life_remain
            self._magic = magic_remain

    status_remain = Remains(self.name, self.life, self.magic)


    # maximum bonus is 100,000
    def health_bonus():

        if status_remain._char == DANTE:
            if status_remain.life == 0:
                return 0
            status_remain._life -= 1
            return 20000+health_bonus()
        
        if status_remain._char == ALICE:
            if status_remain.life == 0:
                return 0
            status_remain._life -= 1
            return 50000+health_bonus()

    health_score = health_bonus()


    def magic_bonus():

        if status_remain._char == DANTE:
            if status_remain._magic == 0:
                return 0
            status_remain._magic -= 5
            return 10000+magic_bonus()
        
        if status_remain._char == ALICE:
            if status_remain._magic == 0:
                return 0
            status_remain._magic -= 5
            return 4000+magic_bonus()

    magic_score = magic_bonus()
    

    def total_bonus():
        return int(magic_score*0.4 + health_score*0.6)



PAUSE_TITLE = [
    ENG_FONT_PATH,
    40,
    COLOR_WHITE,
    [
        'PAUSE  MENU',
        [300, 275]
    ]
]

PAUSE_OPTIONS = [
    ENG_FONT_PATH,
    30,
    COLOR_WHITE,
    [
        [
            'BACK  TO  GAME',
            [500, 400],
            EVENT_SKIP
            ],
            ['RESTART  FROM  BEGINNING',
            [500, 500],
            EVENT_RESTART
            ],
            ['EXIT  TO  MAIN  MENU',
            [500, 600],
            EVENT_QIUT
            ]
    ]
]



DEATH_TITLE = [
    ENG_FONT_PATH,
    40,
    COLOR_WHITE,
    [
        'YOU DEAD',
        [300, 275]
    ]
]

DEATH_OPTIONS = [
    ENG_FONT_PATH,
    30,
    COLOR_WHITE,
    [
            ['RESTART  FROM  BEGINNING',
            [500, 500],
            EVENT_RESTART
            ],
            ['EXIT  TO  MAIN  MENU',
            [500, 600],
            EVENT_QIUT
            ]
    ]
]
#!/user/bin/python3
#REQUIRED MODULES: pygame, numpy
import pygame
import os
import json

from ui import text, menu, score_board
from core import sprite, image, game, player, enemy, barrage, item, bullet, effect, bomb, boss
from game import stage_zero, stage_example, stage_two, stage_three, stage_one
from utils import utility, vector
from utils.settings import *


def main():
    pygame.init()
    pygame.mixer.init()

    # Read settings
    utility.load_settings()

    # full screen and create screen
    if SETTING_DATA['FULL_SCREEN']:
        screen = utility.set_fullscreen()
    else:
        screen = utility.set_fullscreen(False)

    # icon and caption
    # pygame.display.set_icon(utility.load_image('icon'))
    pygame.display.set_caption('')

    pygame.display.flip()

    pygame.mouse.set_visible(True)

    # load everything here
    #stage_one.load_data()
    #stage_three.load_data()
    #stage_zero.load_data()
    effect.load_data()
    enemy.load_data()
    barrage.load_data()
    item.load_data()
    bullet.load_data()
    bomb.load_data()
    boss.load_data()
    score_board.ScoreBoard.load_data()
    utility.load_joystick()

    RUN = True



    while RUN:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        result = menu.Menu(screen, menu.title_example, menu.option_example, menu.image_example).show()
        if result == EVENT_NEXT:
            while True:       
                g = stage_zero.StageZero(screen, ALICE)
                result = g.run()

                if result == EVENT_QIUT:
                    break
                elif result == EVENT_RESTART:
                    continue
            
        elif result == EVENT_SKIP:
            continue
        
        elif result == EVENT_QIUT_GAME:
            pygame.quit()
            exit()

        pygame.display.update()
        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(FRAME_PER_SECOND)


if __name__ == "__main__":
    # Redirect working path
    work_path = os.path.abspath(os.path.dirname(__file__))
    os.chdir(work_path)

    main()

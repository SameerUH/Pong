import pygame
from objects import display, PONG_TITLE, PLAY_GAME, SETTINGS

#START SCREEN
def start_screen():
        display.SCREEN.fill(display.BLACK)
        PONG_TITLE.functions()
        PLAY_GAME.functions()
        SETTINGS.functions()
        pygame.display.update()
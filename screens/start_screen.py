import pygame
from objects import display, PONG_TITLE, PLAY_GAME, SETTINGS, QUIT

#START SCREEN
def start_screen(mouse_pos, mouse_clicked):
        display.SCREEN.fill(display.BLACK)
        PONG_TITLE.functions(mouse_pos, mouse_clicked)
        PLAY_GAME.functions(mouse_pos, mouse_clicked)
        SETTINGS.x, SETTINGS.y = 200, 400
        SETTINGS.functions(mouse_pos, mouse_clicked)
        QUIT.functions(mouse_pos, mouse_clicked)
        pygame.display.update()

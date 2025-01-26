import pygame
from objects import display, PONG_TITLE, PLAY_GAME, SETTINGS

#START SCREEN
def start_screen(mouse_pos, mouse_clicked, user_input):
        display.SCREEN.fill(display.BLACK)
        PONG_TITLE.functions(mouse_pos, mouse_clicked, user_input)
        PLAY_GAME.functions(mouse_pos, mouse_clicked, user_input)
        SETTINGS.functions(mouse_pos, mouse_clicked, user_input)
        #pygame.display.update()
import pygame
from objects import display, CONGRATULATIONS, WINNER, QUIT

def winner_screen(mouse_pos, mouse_clicked):
    display.SCREEN.fill(display.BLACK)
    CONGRATULATIONS.functions(mouse_pos, mouse_clicked)
    WINNER.functions(mouse_pos, mouse_clicked)
    QUIT.x, QUIT.y = 425, 400
    QUIT.functions(mouse_pos, mouse_clicked)

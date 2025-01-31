import pygame
from objects import display, CONGRATULATIONS, WINNER, QUIT

def winner_screen(mouse_pos, mouse_clicked):
    if display.vision == "normal_mode":
        CONGRATULATIONS.colour = display.GREEN
        WINNER.colour = display.BLUE
        QUIT.colour = display.PURPLE
    elif display.vision == "colourblind_mode":
        CONGRATULATIONS.colour = display.YELLOW
        WINNER.colour = display.GRAY
        QUIT.colour = display.LIGHT_BLUE
    
    display.SCREEN.fill(display.BLACK)
    CONGRATULATIONS.functions(mouse_pos, mouse_clicked)
    WINNER.functions(mouse_pos, mouse_clicked)
    QUIT.x, QUIT.y = 425, 400
    QUIT.functions(mouse_pos, mouse_clicked)

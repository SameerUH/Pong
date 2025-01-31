import pygame
from objects import display, SETTINGS, GO_BACK, COLOURBLIND, SPEED, SCORE

"""
SETTINGS TO-DO/NOTES:

Which settings do I want?:
- Colour blind mode.
- Speed settings (slow, normal, fast).
- Normal vision mode (due to double inputs).
- First to 'x' mode????

First make the settings buttons and then do the code for them.
"""

def settings_screen(mouse_pos, mouse_clicked):
    if display.vision == "normal_mode":
        display.SCREEN.fill(display.LIGHT_BLUE)
        SETTINGS.colour = display.RED
        SCORE.colour = display.MAROON
        
    elif display.vision == "colourblind_mode":
        display.SCREEN.fill(display.BLACK)
        SETTINGS.colour = display.BLUE
        SCORE.colour = display.LIGHT_BLUE
        
    
    SETTINGS.x, SETTINGS.y = 425, 50
    SETTINGS.functions(mouse_pos, mouse_clicked)
    GO_BACK.functions(mouse_pos, mouse_clicked)
    COLOURBLIND.functions(mouse_pos, mouse_clicked)
    SPEED.functions(mouse_pos, mouse_clicked)
    SCORE.functions(mouse_pos, mouse_clicked)
    
#Imports/file management for usage of other objects.
import pygame
from objects import display, SETTINGS, GO_BACK, COLOURBLIND, SPEED, SCORE

#Settings screen
def settings_screen(mouse_pos, mouse_clicked):
    """
    Function to allow the player to modify the programs behaviour such as ball and player speed, vision mode and score maximum.

    Similar to the pause screen where it checks which vision mode it is in before deciding which colours to use and then updates the variables/objects used in the function.

    Args:
        mouse_pos (list[ints]): List of integers acting as coordinates for the mouse, used to check if the mouse is over a button.
        mouse_clicked (boolean): Boolean value to check if the mouse button has been clicked or not.
    
    """

    #Selection for which mode the program is in.
    if display.vision == "normal_mode":
        display.SCREEN.fill(display.LIGHT_BLUE)
        SETTINGS.colour = display.RED
        SCORE.colour = display.MAROON
        
    elif display.vision == "colourblind_mode":
        display.SCREEN.fill(display.BLACK)
        SETTINGS.colour = display.BLUE
        SCORE.colour = display.LIGHT_BLUE
        
    
    #Updates for the objects using the functions method.
    SETTINGS.x, SETTINGS.y = 425, 50
    SETTINGS.functions(mouse_pos, mouse_clicked)
    GO_BACK.x, GO_BACK.y = 100, 200
    GO_BACK.functions(mouse_pos, mouse_clicked)
    COLOURBLIND.functions(mouse_pos, mouse_clicked)
    SPEED.functions(mouse_pos, mouse_clicked)
    SCORE.functions(mouse_pos, mouse_clicked)
    
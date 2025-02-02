#Imports/file management to allow usage of other objects.
import pygame
from objects import display, CONGRATULATIONS, WINNER, QUIT

#Winner screen.
def winner_screen(mouse_pos, mouse_clicked):
    """
    Function used to display the winner screen if the player or enemy goes past the score maximum.

    Similar process as other screens.

    Args:
        mouse_pos (list[ints]): List of integers acting as coordinates for the mouse, used to check if the mouse is over a button.
        mouse_clicked (boolean): Boolean value to check if the mouse button has been clicked or not.
    """

    #Selection to decide which vision mode the program is in.
    if display.vision == "normal_mode":
        CONGRATULATIONS.colour = display.GREEN
        WINNER.colour = display.BLUE
        QUIT.colour = display.PURPLE
    elif display.vision == "colourblind_mode":
        CONGRATULATIONS.colour = display.YELLOW
        WINNER.colour = display.GRAY
        QUIT.colour = display.LIGHT_BLUE
    
    #Updates the objects used in the function and displays them.
    display.SCREEN.fill(display.BLACK)
    CONGRATULATIONS.functions(mouse_pos, mouse_clicked)
    WINNER.functions(mouse_pos, mouse_clicked)
    QUIT.x, QUIT.y = 425, 400
    QUIT.functions(mouse_pos, mouse_clicked)

#Imports/file management.
import pygame
from objects import display, TWO_PLAYER, COMPUTER, GAMEMODE, GO_BACK

def computer_decider_screen(mouse_pos, mouse_clicked):
    """
    Function to let the user decide between playing with their friends or playing against the computer.

    Simply displays the buttons and allows the button.py file to act as a backend and control behaviour of the buttons.

    There is also a 'GO BACK' button allowing the user to return to the start screen.
    """
    
    display.SCREEN.fill(display.BLACK)
    GAMEMODE.functions(mouse_pos, mouse_clicked)
    TWO_PLAYER.functions(mouse_pos, mouse_clicked)
    COMPUTER.functions(mouse_pos, mouse_clicked)
    GO_BACK.x, GO_BACK.y = 425, 500
    GO_BACK.functions(mouse_pos, mouse_clicked)
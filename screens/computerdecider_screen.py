"""
To make the computer run on its own I'm going to first make a screen which allows the user to decide between the computer or 2 player game.

3 buttons: (2-player, computer, GO BACK).
    if 2-player button is pressed:
        game_setting.computer = False
        display.state = 'game_screen'
    elif computer is pressed:
        game_setting.computer = True
        display.state = 'game_screen'

Make the computer after.
"""

import pygame
from objects import display, TWO_PLAYER, COMPUTER, GAMEMODE

def computer_decider_screen(mouse_pos, mouse_clicked):
    display.SCREEN.fill(display.BLACK)
    GAMEMODE.functions(mouse_pos, mouse_clicked)
    TWO_PLAYER.functions(mouse_pos, mouse_clicked)
    COMPUTER.functions(mouse_pos, mouse_clicked)
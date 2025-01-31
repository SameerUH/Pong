"""
To-Do:
1. Score. ####
2. Start screen. ####
    - Black screen with buttons. ####
3. Settings screen. ###
4. Computer A.I.
5. Changes to the ball movement. ###
6. Possibly an intro scene.
7. Do I think I can add animations??
"""
#Imports:
import pygame
import os
import sys
import time


#File organization:
from screens import *
from objects import display, ball, player, enemy, QUIT

os.environ["SDL_VIDEO_CENTERED"] = "1"

clock = pygame.time.Clock()

mouse_clicked = False


pygame.init()

#Main loop
while True:
    user_input = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    FULLSCREEN = False
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if events.type == pygame.MOUSEBUTTONDOWN:
        mouse_clicked = True
    else:
        mouse_clicked = False

    if (user_input[pygame.K_F11]):
        pygame.display.toggle_fullscreen()


    clock.tick()
    pygame.display.set_caption("FPS: " + str(int(clock.get_fps())))
    if display.state == "start_screen":
        #START SCREEN
        start_screen(mouse_pos, mouse_clicked)
    elif display.state == "game_screen":
        #GAME DISPLAY
        game_screen(mouse_pos, mouse_clicked, user_input)
    elif display.state == "settings_screen":
        settings_screen(mouse_pos, mouse_clicked)
    elif display.state == "pause_screen":
        pause_screen(mouse_pos, mouse_clicked, user_input)
    elif display.state == "winner_screen":
        winner_screen(mouse_pos, mouse_clicked)

    pygame.display.update()
    
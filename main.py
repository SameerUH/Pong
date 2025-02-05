"""
To-Do:
1. Score. ####
2. Start screen. ####
    - Black screen with buttons. ####
3. Settings screen. ###
4. Computer A.I. ###
5. Changes to the ball movement. ###
6. Possibly an intro scene.
7. Do I think I can add animations??
"""
#Imports:
import pygame
import os
import sys


#File organization:
from screens import *
from objects import display, ball, player, enemy, QUIT

#Centers the window when the game is run
os.environ["SDL_VIDEO_CENTERED"] = "1"


#Used to keep track of FPS (debugging/troubleshooting)
clock = pygame.time.Clock()

#Initializes the mouse_clicked variable to help keep track of user inputs.
mouse_clicked = False

fullscreen = False

#Initializes pygame modules.
pygame.init()

#Main loop
while True:
    #Used to allow user inputs.
    user_input = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    FULLSCREEN = False
    
    #Keeps track of events in the program.
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Used to keep track of mouse inputs.
    if events.type == pygame.MOUSEBUTTONDOWN:
        mouse_clicked = True
    else:
        mouse_clicked = False

    #Used to allow fullscreen.
    if (user_input[pygame.K_F11]) and fullscreen == False:
        pygame.display.toggle_fullscreen()
        fullscreen = True
    elif (user_input[pygame.K_F11]) and fullscreen == True:
        fullscreen = False

    #Used to keep track of FPS and displays it as the window title when run.
    clock.tick()
    pygame.display.set_caption("PONG")

    #Selection to decide which functions should run when the user navigates through the game.
    if display.state == "intro_screen":
        #INTRO SCREEN
        intro_screen()
    if display.state == "start_screen":
        #START SCREEN
        start_screen(mouse_pos, mouse_clicked)
    elif display.state == "game_screen":
        #GAME DISPLAY
        game_screen(mouse_pos, mouse_clicked, user_input)
    elif display.state == "settings_screen":
        #SETTINGS DISPLAY
        settings_screen(mouse_pos, mouse_clicked)
    elif display.state == "pause_screen":
        #PAUSE DISPLAY
        pause_screen(mouse_pos, mouse_clicked, user_input)
    elif display.state == "winner_screen":
        #WINNER DISPLAY
        winner_screen(mouse_pos, mouse_clicked)
    elif display.state == "computer_decider_screen":
        #GAMEMODE DISPLAY
        computer_decider_screen(mouse_pos, mouse_clicked)

    #Constantly updates pygame to apply changes.
    pygame.display.update()
    
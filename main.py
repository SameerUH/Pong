"""
To-Do:
1. Score. ####
2. Start screen.
    - Black screen with buttons.
3. Settings screen.
4. Computer A.I.
5. Changes to the ball movement.
6. Possibly an intro scene.
7. Do I think I can add animations??
"""
#Imports:
import pygame
import os
import sys


#File organization:
from objects import player
from objects import enemy
from objects import ball
from objects import PONG_TITLE, PLAY_GAME, SETTINGS
from objects import display

#Game States:
Start_state = False
Game_state = True

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.display.set_caption("PONG")
pygame.init()

#Score Text:
font = pygame.font.Font('freesansbold.ttf', 32)
player_score = font.render(f'Player Score: {player.score}', True, display.BLACK)
player_score_rect = player_score.get_rect()
player_score_rect.center = (150, 650)

enemy_score = font.render(f"Enemy Score: {enemy.score}", True, display.BLACK)
enemy_score_rect = enemy_score.get_rect()
enemy_score_rect.center = (1000, 650)

while True:
    user_input = pygame.key.get_pressed()
    FULLSCREEN = False
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            mouseclicked = True
        if (user_input[pygame.K_F11]):
            pygame.display.toggle_fullscreen()
        else:
            mouseclicked = False
    
    if Start_state == True:
        #START SCREEN
        display.SCREEN.fill(display.BLACK)
        PONG_TITLE.functions()
        PLAY_GAME.functions()
        SETTINGS.functions()
        pygame.display.update()

    elif Game_state == True:
        #GAME DISPLAY
        display.SCREEN.fill(display.GRAY)
        SCREEN_OUTLINE = pygame.draw.rect(display.SCREEN, display.BLUE, (0, 0, display.SCREENWIDTH, display.GAMEHEIGHT), 2)

        #Score display code:
        player_score = font.render(f'Player Score: {player.score}', True, display.BLACK)
        enemy_score = font.render(f"Enemy Score: {enemy.score}", True, display.BLACK) 
        display.SCREEN.blit(player_score, player_score_rect)
        display.SCREEN.blit(enemy_score, enemy_score_rect)
        

        #Object/Screen updates:
        player.functions(user_input)
        enemy.functions(user_input)
        ball.functions()

        pygame.display.update()
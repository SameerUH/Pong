import pygame
from objects import display, player, ball, enemy, CONTINUE, PAUSED, END_GAME
from .start_screen import start_screen

font = pygame.font.Font('freesansbold.ttf', 32)
player_score = font.render(f'Player Score: {player.score}', True, display.BLACK)
player_score_rect = player_score.get_rect()
player_score_rect.center = (150, 650)

enemy_score = font.render(f"Enemy Score: {enemy.score}", True, display.BLACK)
enemy_score_rect = enemy_score.get_rect()
enemy_score_rect.center = (1000, 650)

"""
TO-DO:
Finish layout
    - End game button in red which will go back to the start screen.
    - Big "PAUSED" text note at the top.
    - Maybe have the Continue button on the left and the End game button on the right.
"""
def pause_screen(mouse_pos, mouse_clicked, user_input):
    #print(ball.temp_x_velocity, ball.temp_y_velocity)
    display.SCREEN.fill(display.GRAY)
    SCREEN_OUTLINE = pygame.draw.rect(display.SCREEN, display.BLUE, (0, 0, display.SCREENWIDTH, display.GAMEHEIGHT), 2)
    player.functions(user_input)
    enemy.functions(user_input)
    ball.draw_updatescreen()
    PAUSED.functions(mouse_pos, mouse_clicked)
    CONTINUE.functions(mouse_pos, mouse_clicked)
    END_GAME.functions(mouse_pos, mouse_clicked)
    player_score = font.render(f'Player Score: {player.score}', True, display.BLACK)
    enemy_score = font.render(f"Enemy Score: {enemy.score}", True, display.BLACK)
    display.SCREEN.blit(player_score, player_score_rect)
    display.SCREEN.blit(enemy_score, enemy_score_rect)
    temp_x, temp_y = ball.temp_x_velocity, ball.temp_y_velocity
    ball.x_velocity = 0
    ball.y_velocity = 0

    #pygame.display.update()
    if display.state == "game_screen":
        ball.x_velocity, ball.y_velocity = temp_x, temp_y


    




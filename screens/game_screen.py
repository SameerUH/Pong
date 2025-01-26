import pygame
from objects import display, player, enemy, ball, PAUSE
from .pause_screen import pause_screen

#pygame.init()


font = pygame.font.Font('freesansbold.ttf', 32)
player_score = font.render(f'Player Score: {player.score}', True, display.BLACK)
player_score_rect = player_score.get_rect()
player_score_rect.center = (150, 650)

enemy_score = font.render(f"Enemy Score: {enemy.score}", True, display.BLACK)
enemy_score_rect = enemy_score.get_rect()
enemy_score_rect.center = (1000, 650)

#GAME DISPLAY
def game_screen(user_input, mouse_pos, mouse_clicked):
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
    PAUSE.functions(mouse_pos, mouse_clicked, user_input)
    #pygame.display.update()
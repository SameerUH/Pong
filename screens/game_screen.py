import pygame
from objects import display, player, enemy, ball, PAUSE, WINNER
from .pause_screen import pause_screen
from game_settings import game_setting

font = pygame.font.Font('freesansbold.ttf', 32)
player_score = font.render(f'Player Score: {player.score}', True, display.BLACK)
player_score_rect = player_score.get_rect()
player_score_rect.center = (150, 650)

enemy_score = font.render(f"Enemy Score: {enemy.score}", True, display.BLACK)
enemy_score_rect = enemy_score.get_rect()
enemy_score_rect.center = (1000, 650)

#GAME DISPLAY
def game_screen(mouse_pos, mouse_clicked, user_input):
    if display.vision == "normal_mode":
        display.SCREEN.fill(display.GRAY)
        SCREEN_OUTLINE = pygame.draw.rect(display.SCREEN, display.BLUE, (0, 0, display.SCREENWIDTH, display.GAMEHEIGHT), 2)
        PAUSE.colour = display.GREEN
        ball.colour = display.RED
        player.colour = display.BLACK
        enemy.colour = display.BLACK
        player_score = font.render(f'Player Score: {player.score}', True, display.BLACK)
        enemy_score = font.render(f"Enemy Score: {enemy.score}", True, display.BLACK) 


    elif display.vision == "colourblind_mode":
        display.SCREEN.fill(display.BLUE)
        SCREEN_OUTLINE = pygame.draw.rect(display.SCREEN, display.PURPLE, (0, 0, display.SCREENWIDTH, display.GAMEHEIGHT), 2)
        PAUSE.colour = display.YELLOW
        ball.colour = display.WHITE
        player.colour = display.MAROON
        enemy.colour = display.MAROON
        player_score = font.render(f'Player Score: {player.score}', True, display.YELLOW)
        enemy_score = font.render(f"Enemy Score: {enemy.score}", True, display.YELLOW) 

    #Score display code:
    display.SCREEN.blit(player_score, player_score_rect)
    display.SCREEN.blit(enemy_score, enemy_score_rect)


    if player.score == game_setting.score:
        display.state = "winner_screen"
        WINNER.text = "PLAYER WINS!"
    elif enemy.score == game_setting.score:
        display.state = "winner_screen"
        WINNER.text = "ENEMY WINS!"


    #Object/Screen updates:
    player.functions(user_input)
    enemy.functions(user_input)
    ball.functions()
    PAUSE.functions(mouse_pos, mouse_clicked)
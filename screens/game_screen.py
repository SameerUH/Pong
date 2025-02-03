#Imports/file management to allow the use of other modules/objects.
import pygame
from objects import display, player, enemy, ball, PAUSE, WINNER
from .pause_screen import pause_screen
from game_settings import game_setting

#Creation of the "Score: x" to be displayed in the corners of the screen
font = pygame.font.Font('freesansbold.ttf', 32)
player_score = font.render(f'Player Score: {player.score}', True, display.BLACK)
player_score_rect = player_score.get_rect()
player_score_rect.center = (150, 650)

enemy_score = font.render(f"Enemy Score: {enemy.score}", True, display.BLACK)
enemy_score_rect = enemy_score.get_rect()
enemy_score_rect.center = (1000, 650)

tempx_0 = ball.x
tempy_0 = ball.y
tempx_600 = ball.x
tempy_600 = ball.y
#GAME DISPLAY
def game_screen(mouse_pos, mouse_clicked, user_input):
    global tempx_0, tempy_0, tempx_600, tempy_600
    """
    Function which constantly displays the game screen.

    First checks whether or not the game is in colourblind mode or not and decides which colours to use.
    Then displays the scores in the corners and checks which user has won.
    Finally uses the 'functions' used to constantly update the display and values of objects used.

    Args:
        mouse_pos (list[ints]): List of integers which is used as the coordinates of the mouse.
        mouse_clicked(boolean): Boolean value to check if the mouse has been clicked or not.
    """
    #Selection of whether or not the game is in colourblind mode or not.
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

    
    if tempy_0 > 0:
        if tempy_0 < 10:
            tempy_0 -= 0.1
            tempx_0 -= 0.1
        else:
            tempy_0 -= (ball.y_velocity * 5)
            tempx_0 -= (ball.x_velocity * 5)
        pygame.draw.line(display.SCREEN, display.BLUE, (ball.x, ball.y), (tempx_0, tempy_0), 10)
        pygame.draw.circle(display.SCREEN, display.GREEN, (tempx_0, tempy_0), 50, 10)
        print(tempx_0, tempy_0)

    if tempy_0 < 0:
        tempx_0 = ball.x
        tempy_0 = ball.y


    
    #Selection to check if a player has won.
    if player.score == game_setting.score:
        display.state = "winner_screen"
        WINNER.text = "PLAYER WINS!"
    elif enemy.score == game_setting.score:
        display.state = "winner_screen"
        WINNER.text = "ENEMY WINS!"

    #Object/Screen updates:
    player.functions(user_input, ball)
    enemy.functions(user_input, ball)
    ball.functions()
    PAUSE.functions(mouse_pos, mouse_clicked)
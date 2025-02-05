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

#wall_predict_x = ball.x
#wall_predict_y = ball.y

#enemy_predict_x = wall_predict_x
#enemy_predict_y = wall_predict_y

#GAME DISPLAY
def game_screen(mouse_pos, mouse_clicked, user_input):
    #global wall_predict_x, wall_predict_y
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

    
    if ball.wall_predict_y > 0:
        if ball.wall_predict_y < 10:
            ball.wall_predict_y -= 0.1
            ball.wall_predict_x -= 0.1
        else:
            ball.wall_predict_y -= (ball.y_velocity * 1.5)
            ball.wall_predict_x -= (ball.x_velocity * 1.5)
        #print(tempx_0, tempy_0)
    
    elif ball.wall_predict_y < 600:
        if ball.wall_predict_y > 590:
            ball.wall_predict_y += 0.1
            ball.wall_predict_x += 0.1
        else:
            ball.wall_predict_y += (ball.y_velocity * 1.5)
            ball.wall_predict_x += (ball.x_velocity * 1.5)
 
    if ball.wall_predict_y < 0:
        ball.wall_predict_y = ball.y
        ball.wall_predict_x = ball.x
    elif ball.wall_predict_y > 600:
        ball.wall_predict_y = ball.y
        ball.wall_predict_x = ball.x
    
    if ball.wall_predict_x < 100:
        ball.wall_predict_y = ball.y
        ball.wall_predict_x = ball.x
    elif ball.wall_predict_x > 1050:
        ball.wall_predict_y = ball.y
        ball.wall_predict_x = 1050
    
    line_x_700 = pygame.draw.line(display.SCREEN, display.MAROON, (700, 0), (700, 600), 5)
    line_x_1000 = pygame.draw.line(display.SCREEN, display.MAROON, (1000, 0), (1000, 600), 5)


    line_predict = pygame.draw.line(display.SCREEN, display.BLUE, (ball.x, ball.y), (ball.wall_predict_x, ball.wall_predict_y), 10)
    #line_predict2 = pygame.draw.line(display.SCREEN, display.PURPLE, (ball.wall_predict_x, ball.wall_predict_y), (enemy.x, enemy.y), 10)
    circle_predict = pygame.draw.circle(display.SCREEN, display.GREEN, (ball.wall_predict_x, ball.wall_predict_y), 30, 10)
    
    #Selection to check if a player has won.
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
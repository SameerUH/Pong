#Imports/file management to allow use of other objects/modules.
import pygame
from objects import display, player, ball, enemy, CONTINUE, PAUSED, END_GAME
from .start_screen import start_screen

#Creation of the "Score: x" to be displayed in the corners of the screen
font = pygame.font.Font('freesansbold.ttf', 32)
player_score = font.render(f'Player Score: {player.score}', True, display.BLACK)
player_score_rect = player_score.get_rect()
player_score_rect.center = (150, 650)

enemy_score = font.render(f"Enemy Score: {enemy.score}", True, display.BLACK)
enemy_score_rect = enemy_score.get_rect()
enemy_score_rect.center = (1000, 650)


def pause_screen(mouse_pos, mouse_clicked, user_input):
    """
    Function used to display the pause screen when the pause button is pressed.

    Similar process to other screens where it checks which vision mode the game is in and decided which colours to use, then it updates all the objects used in the screen.

    In this screen it should show the ball, players and scores but shouldn't allow the players to move them, effectively making it a freezeframe.

    Args:
        mouse_pos (list[ints]): List of integers acting as coordinates for the mouse, used to check if the mouse is over a button.
        mouse_clicked (boolean): Boolean value to check if the mouse button has been clicked or not.
        user_input (inbuilt): Passed into the player and enemy objects so that they don't move when keys are pressed in the pause screen.
    """
    
    #Selection to decide which vision mode the program is in.
    if display.vision == "normal_mode":
        display.SCREEN.fill(display.GRAY)
        SCREEN_OUTLINE = pygame.draw.rect(display.SCREEN, display.BLUE, (0, 0, display.SCREENWIDTH, display.GAMEHEIGHT), 2)
        ball.colour = display.RED
        player.colour = display.BLACK
        enemy.colour = display.BLACK
        player_score = font.render(f'Player Score: {player.score}', True, display.BLACK)
        enemy_score = font.render(f"Enemy Score: {enemy.score}", True, display.BLACK)
        PAUSED.colour = display.BLACK
        CONTINUE.colour = display.GREEN
        END_GAME.colour = display.RED
    
    elif display.vision == "colourblind_mode":
        display.SCREEN.fill(display.BLUE)
        SCREEN_OUTLINE = pygame.draw.rect(display.SCREEN, display.PURPLE, (0, 0, display.SCREENWIDTH, display.GAMEHEIGHT), 2)
        ball.colour = display.WHITE
        player.colour = display.MAROON
        enemy.colour = display.MAROON
        player_score = font.render(f'Player Score: {player.score}', True, display.YELLOW)
        enemy_score = font.render(f"Enemy Score: {enemy.score}", True, display.YELLOW)
        PAUSED.colour = display.LIGHT_BLUE
        CONTINUE.colour = display.ORANGE
        END_GAME.colour = display.PURPLE

    #Updates for variables and objects.
    SCREEN_OUTLINE = pygame.draw.rect(display.SCREEN, display.BLUE, (0, 0, display.SCREENWIDTH, display.GAMEHEIGHT), 2)
    player.functions(user_input)
    enemy.functions(user_input)
    ball.draw_updatescreen()
    PAUSED.functions(mouse_pos, mouse_clicked)
    CONTINUE.functions(mouse_pos, mouse_clicked)
    END_GAME.functions(mouse_pos, mouse_clicked)
    display.SCREEN.blit(player_score, player_score_rect)
    display.SCREEN.blit(enemy_score, enemy_score_rect)
    temp_x, temp_y = ball.temp_x_velocity, ball.temp_y_velocity
    ball.x_velocity = 0
    ball.y_velocity = 0

    #Makes the ball go back to the same direction if the player decides to continue the game.
    if display.state == "game_screen":
        ball.x_velocity, ball.y_velocity = temp_x, temp_y


    




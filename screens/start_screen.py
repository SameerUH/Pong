#Imports/file management for usage of other objects.
import pygame
from objects import display, PONG_TITLE, PLAY_GAME, SETTINGS, QUIT, ball, player, enemy

#START SCREEN
def start_screen(mouse_pos, mouse_clicked):
        """
        Function used to display the start screen and to reset objects/variables such as positioning and scores.

        First checks which vision state the game is in, then repositions objects and updates them to be displayed.

        Args:
                mouse_pos (list[ints]): List of integers acting as coordinates for the mouse, used to check if the mouse is over a button.
                mouse_clicked (boolean): Boolean value to check if the mouse button has been clicked or not.
        """

        #Selection to decide which state the game is in.
        if display.vision == "normal_mode":
                PONG_TITLE.colour = display.DARK_GRAY
                PLAY_GAME.colour = display.BLUE
                SETTINGS.colour = display.RED
                QUIT.colour = display.PURPLE
                display.SCREEN.fill(display.BLACK)
        if display.vision == "colourblind_mode":
                display.SCREEN.fill(display.GREEN)
                PONG_TITLE.colour = display.ORANGE
                PLAY_GAME.colour = display.BLUE
                SETTINGS.colour = display.BLACK
                QUIT.colour = display.PURPLE
        
        #Updates/repositions objects/buttons.
        ball.x, ball.y, ball.x_velocity, ball.y_velocity = (display.SCREENWIDTH / 2), (display.SCREENHEIGHT / 2), 1, 0
        player.y, player.score = (display.SCREENHEIGHT / 2), 0
        enemy.y, enemy.score = (display.SCREENHEIGHT / 2), 0
        QUIT.x, QUIT.y = 600, 400
        SETTINGS.x, SETTINGS.y = 200, 400

        #Updates and uses the functions method to display them in the correct place.
        ball.update(ball.x, ball.y, ball.x_velocity, ball.y_velocity, ball.colour, ball.wall_hit)
        player.update(player.y, player.score, player.colour)
        enemy.update(enemy.y, enemy.score, enemy.colour)
        QUIT.functions(mouse_pos, mouse_clicked)
        PONG_TITLE.functions(mouse_pos, mouse_clicked)
        PLAY_GAME.functions(mouse_pos, mouse_clicked)
        SETTINGS.functions(mouse_pos, mouse_clicked)
        QUIT.functions(mouse_pos, mouse_clicked)

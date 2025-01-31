import pygame
from objects import display, PONG_TITLE, PLAY_GAME, SETTINGS, QUIT, ball, player, enemy

#START SCREEN
def start_screen(mouse_pos, mouse_clicked):
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
                
        ball.x, ball.y, ball.x_velocity, ball.y_velocity = (display.SCREENWIDTH / 2), (display.SCREENHEIGHT / 2), 1, 0
        player.y, player.score = (display.SCREENHEIGHT / 2), 0
        enemy.y, enemy.score = (display.SCREENHEIGHT / 2), 0
        QUIT.x, QUIT.y = 600, 400
        ball.update(ball.x, ball.y, ball.x_velocity, ball.y_velocity, ball.colour)
        player.update(player.y, player.score, player.colour)
        enemy.update(enemy.y, enemy.score, enemy.colour)
        QUIT.functions(mouse_pos, mouse_clicked)
        PONG_TITLE.functions(mouse_pos, mouse_clicked)
        PLAY_GAME.functions(mouse_pos, mouse_clicked)
        SETTINGS.x, SETTINGS.y = 200, 400
        SETTINGS.functions(mouse_pos, mouse_clicked)
        QUIT.functions(mouse_pos, mouse_clicked)
        pygame.display.update()

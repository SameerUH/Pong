import pygame, sys, math
from .display import display
from .ball import ball
from game_settings import game_setting
pygame.init()


class Button(pygame.sprite.Sprite):
    def __init__(self, colour, x, y, width, height, text, font_size):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = text
        self.font_size = font_size
        pygame.draw.rect(display.SCREEN, self.colour, self.shape)
        self.font = pygame.font.Font('freesansbold.ttf', self.font_size)
        display_text = self.font.render(self.text, True, display.WHITE)
        display_text_rect = display_text.get_rect()
        display_text_rect.center = (self.x + (self.width/2), self.y - (self.height / 2) )
        display.SCREEN.blit(display_text, display_text_rect)

    def draw_updatescreen(self):
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(display.SCREEN, self.colour, self.shape)
        font = pygame.font.Font('freesansbold.ttf', self.font_size)
        display_text = font.render(self.text, True, display.WHITE)
        display_text_rect = display_text.get_rect()
        display_text_rect.center = (self.x + (self.width/2), self.y + (self.height / 2) )
        display.SCREEN.blit(display_text, display_text_rect)
    
    def interaction(self, mouse_pos, mouse_clicked):
        if mouse_pos[1] < self.shape[1] + self.shape[3] and mouse_pos[1] > self.shape[1]:
            if mouse_pos[0] > self.shape[0] and mouse_pos[0] < self.shape[0] + self.shape[2]:
                if mouse_clicked:
                    if display.state == "start_screen":
                        if self.text == "PLAY GAME":
                            display.state = "game_screen"
                        elif self.text == "SETTINGS":
                            display.state = "settings_screen"
                        elif self.text == "QUIT":
                            pygame.quit()
                            sys.exit()
                    elif display.state == "game_screen":
                        if self.text == "PAUSE":
                            display.state = "pause_screen"
                    elif display.state == "pause_screen":
                        if self.text == "CONTINUE":
                            display.state = "game_screen"
                        elif self.text == "END GAME":
                            display.state = "start_screen"
                    elif display.state == "settings_screen":
                        if self.text == "GO BACK":
                            display.state = "start_screen"

                        elif self.text == "SPEED: NORMAL":
                            self.text = "SPEED: FAST"
                            self.colour = display.GREEN
                            game_setting.x_velocity_min, game_setting.x_velocity_max = 1.5, 2
                            game_setting.y_velocity_min, game_setting.y_velocity_max = 1.3, 1.6
                            game_setting.speed = 2
                        
                        elif self.text == "SPEED: FAST":
                            self.text = "SPEED: SLOW"
                            self.colour = display.RED
                            game_setting.x_velocity_min, game_setting.x_velocity_max = 0.5, 1
                            game_setting.y_velocity_min, game_setting.y_velocity_max = 0.4, 0.7
                            game_setting.speed = 0.5
                            
                        elif self.text == "SPEED: SLOW":
                            self.text = "SPEED: NORMAL"
                            self.colour = display.YELLOW
                            game_setting.x_velocity_min, game_setting.x_velocity_max = 1, 1.5
                            game_setting.y_velocity_min, game_setting.y_velocity_max = 0.7, 1
                            game_setting.speed = 1
                            
                        elif self.text == "COLOURBLIND":
                            self.text = "NORMAL"
                            self.colour = display.DARK_GRAY
                            display.vision = "colourblind_mode"
                            
                        elif self.text == "NORMAL":
                            self.text = "COLOURBLIND"
                            self.colour = display.BLUE
                            display.vision = "normal_mode"
                        

                        if self.text == "SCORE:MAX":
                            game_setting.score = 1
                            self.text = "SCORE: 1"
                        elif self.text == f"SCORE: {game_setting.score}":
                            game_setting.score += 1
                            self.text = f"SCORE: {game_setting.score}"
                            if game_setting.score > 10:
                                game_setting.score = math.inf
                                self.text = "SCORE:MAX"
                
                    elif display.state == "winner_screen":
                        if self.text == "QUIT":
                            display.state = "start_screen"
                        
                    pygame.time.delay(100)
                            



    def update(self, x, y): 
        self.x = x
        self.y = y
    
    def functions(self, mouse_pos, mouse_clicked):
        self.draw_updatescreen()
        self.interaction(mouse_pos, mouse_clicked)
        self.update(self.x, self.y)


PONG_TITLE = Button(display.DARK_GRAY, 425, 50, 300, 100, "PONG", 50)
PLAY_GAME = Button(display.BLUE, 425, 200, 300, 100, "PLAY GAME", 50)
SETTINGS = Button(display.RED, 200, 400, 300, 100, "SETTINGS", 50)
PAUSE = Button(display.GREEN, 425, 600, 300, 100, "PAUSE", 50)
CONTINUE = Button(display.GREEN, 200, 400, 300, 100, "CONTINUE", 50)
PAUSED = Button(display.BLACK, 400, 200, 300, 100, "PAUSED", 50)
END_GAME = Button(display.RED, 600, 400, 300, 100, "END GAME", 50)
QUIT = Button(display.PURPLE, 600, 400, 300, 100, "QUIT", 50)
GO_BACK = Button(display.ORANGE, 100, 200, 300, 100, "GO BACK", 50)
COLOURBLIND = Button(display.BLUE, 700, 200, 300, 100, "COLOURBLIND", 35)
SPEED = Button(display.YELLOW, 700, 400, 300, 100, "SPEED: NORMAL", 35)
SCORE = Button(display.MAROON, 100, 400, 325, 100, "SCORE:MAX", 50)
CONGRATULATIONS = Button(display.GREEN, 300, 50, 600, 100, "CONGRATULATIONS!!!", 50)
WINNER = Button(display.BLUE, 375, 225, 400, 100, "NONE", 50)
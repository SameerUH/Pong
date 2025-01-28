import pygame, sys
from .display import display
from .ball import ball
pygame.init()


class Button(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height, text, font_size):
        #pygame.Surface.convert_alpha(display.SCREEN)
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = text
        self.font_size = font_size
        pygame.draw.rect(display.SCREEN, self.color, self.shape)
        self.font = pygame.font.Font('freesansbold.ttf', self.font_size)
        display_text = self.font.render(self.text, True, display.WHITE)
        display_text_rect = display_text.get_rect()
        display_text_rect.center = (self.x + (self.width/2), self.y - (self.height / 2) )
        display.SCREEN.blit(display_text, display_text_rect)

    def draw_updatescreen(self):
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(display.SCREEN, self.color, self.shape)
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
                        if self.text == "END GAME":
                            display.state = "start_screen"
                    elif display.state == "settings_screen":
                        if self.text == "GO BACK":
                            display.state = "start_screen"

    def update(self, x, y): 
        self.x = x
        self.y = y
    
    def functions(self, mouse_pos, mouse_clicked):
        self.draw_updatescreen()
        self.interaction(mouse_pos, mouse_clicked)
        self.update(self.x, self.y)


PONG_TITLE = Button(display.DARK_GRAY, 425, 50, 300, 100, "PONG", 50)
PLAY_GAME = Button(display.BLUE, 425, 200, 300, 100, "PLAY GAME", 50)
SETTINGS = Button(display.RED, 200, 500, 300, 100, "SETTINGS", 50)
PAUSE = Button(display.GREEN, 425, 600, 300, 100, "PAUSE", 50)
CONTINUE = Button(display.GREEN, 200, 400, 300, 100, "CONTINUE", 50)
PAUSED = Button(display.BLACK, 400, 200, 300, 100, "PAUSED", 50)
END_GAME = Button(display.RED, 600, 400, 300, 100, "END GAME", 50)
QUIT = Button(display.PURPLE, 600, 500, 300, 100, "QUIT", 50)
GO_BACK = Button(display.ORANGE, 100, 200, 300, 100, "GO BACK", 50)
COLOURBLIND = Button(display.BLUE, 700, 200, 300, 100, "COLOURBLIND", 35)
NORMAL_MODE = Button(display.DARK_GRAY, 700, 350, 300, 100, "NORMAL VISION", 35)
SPEED = Button(display.YELLOW, 700, 500, 300, 100, "SPEED: NORMAL", 35)
SCORE = Button(display.MAROON, 100, 350, 300, 100, "SCORE:  ", 50) 
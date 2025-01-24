import pygame
from .display import display
pygame.init()


class Button(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height, text, font_size):
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

    def update(self, x, y): 
        self.x = x
        self.y = y
    
    def functions(self):
        self.draw_updatescreen()
        self.update(self.x, self.y)


PONG_TITLE = Button(display.DARK_GRAY, 425, 50, 300, 100, "PONG", 50)
PLAY_GAME = Button(display.BLUE, 200, 200, 300, 100, "PLAY GAME", 50)
SETTINGS = Button(display.RED, 600, 200, 300, 100, "SETTINGS", 50)
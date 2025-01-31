import pygame
from .display import display
from game_settings import game_setting

#Enemy class:
class Enemy(pygame.sprite.Sprite):
    def __init__(self, colour, y):
        self.colour = colour
        self.x = 1050
        self.y = y
        self.width = 20
        self.height = 60
        self.shape = pygame.draw.rect(display.SCREEN, self.colour, (self.x, self.y, self.width, self.height), 0)
        self.hitbox = pygame.draw.rect(display.SCREEN, self.colour, (self.x, self.y, self.width, self.height), 1)
        self.score = 0
        self.direction = "normal"

    def draw_updatescreen(self):
        self.shape = pygame.draw.rect(display.SCREEN, self.colour, (self.x, self.y, self.width, self.height), 0)
        self.hitbox = pygame.draw.rect(display.SCREEN, self.colour, (self.x, self.y, self.width, self.height), 1)
    
    def update(self, y, score, colour):
        self.x = 1050
        self.y = y
        self.score = score
        self.colour = colour

    def movement(self, user_input):
        if display.state == "game_screen":
            if (user_input[pygame.K_UP]):
                self.y -= game_setting.speed
                self.direction = "up"
            elif (user_input[pygame.K_DOWN]):
                self.y += game_setting.speed
                self.direction = "down"
            
            if (self.y + 60) >= display.GAMEHEIGHT:
                self.y -= game_setting.speed
            elif self.y <= 0:
                self.y += game_setting.speed

        elif display.state == "pause_screen":
            if (user_input[pygame.K_UP]):
                self.y -= 0
            elif (user_input[pygame.K_DOWN]):
                self.y += 0


    def functions(self, user_input):
        self.draw_updatescreen()
        self.update(self.y, self.score, self.colour)
        self.movement(user_input)


enemy = Enemy(display.BLACK, display.SCREENHEIGHT / 2)
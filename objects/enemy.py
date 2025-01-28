import pygame
from .display import display
#pygame.init()

#Enemy class:
class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, y):
        self.color = color
        self.x = 1050
        self.y = y
        self.width = 20
        self.height = 60
        self.shape = pygame.draw.rect(display.SCREEN, self.color, (self.x, self.y, self.width, self.height), 0)
        self.upperhitbox = pygame.draw.rect(display.SCREEN, self.color, (self.x, self.y, self.width, self.height / 2), 1)
        self.lowerhitbox = pygame.draw.rect(display.SCREEN, self.color, (self.x, self.y+30, self.width, self.height / 2), 1)
        self.score = 0

    def draw_updatescreen(self):
        self.shape = pygame.draw.rect(display.SCREEN, self.color, (self.x, self.y, self.width, self.height), 0)
        self.upperhitbox = pygame.draw.rect(display.SCREEN, self.color, (self.x, self.y, self.width, self.height / 2), 1)
        self.lowerhitbox = pygame.draw.rect(display.SCREEN, self.color, (self.x, self.y+30, self.width, self.height / 2), 1)
    
    def update(self, y, score):
        self.x = 1050
        self.y = y
        self.score = score

    def movement(self, user_input):
        if display.state == "game_screen":
            if (user_input[pygame.K_UP]):
                self.y -= 1
            elif (user_input[pygame.K_DOWN]):
                self.y += 1
            
            if (self.y + 60) >= display.GAMEHEIGHT:
                self.y -= 1
            elif self.y <= 0:
                self.y += 1
        elif display.state == "pause_screen":
            if (user_input[pygame.K_UP]):
                self.y -= 0
            elif (user_input[pygame.K_DOWN]):
                self.y += 0


    def functions(self, user_input):
        self.draw_updatescreen()
        self.update(self.y, self.score)
        self.movement(user_input)


enemy = Enemy(display.BLACK, display.SCREENHEIGHT / 2)
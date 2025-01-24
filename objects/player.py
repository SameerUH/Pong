import pygame
from .display import display

#Player class:
class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
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
        #self.hitbox = pygame.draw.rect(SCREEN, BLUE, (self.x, self.y, self.width, self.height), 1)
    def update(self, x, y, score):
        self.x = x
        self.y = y
        self.score = score

    def movement(self, user_input):
        if (user_input[pygame.K_w]):
            self.y -= 0.5
        elif (user_input[pygame.K_s]):
            self.y += 0.5

        if (self.y + 60) >= display.GAMEHEIGHT:
            self.y -= 0.5
        elif self.y <= 0:
            self.y += 0.5
    
    
    def functions(self, user_input):
        self.draw_updatescreen()
        self.update(self.x, self.y, self.score)
        self.movement(user_input)


player = Player(display.BLACK, 100, display.SCREENHEIGHT / 2)
        



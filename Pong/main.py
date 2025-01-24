"""
To-Do:
- Start screen.
- Score.
- Computer A.I.
- Settings screen.
- Possibly an intro scene.
"""


#Imports:
import pygame
import os
import sys
import random as rand


#Colours:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (211, 211, 211)
BLUE = (0, 0, 255)

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.display.set_caption("PONG")


#Screen code:
SCREENWIDTH = 1150
SCREENHEIGHT = 600
SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
SCREEN = pygame.display.set_mode(SCREENSIZE)

#Player class:
class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.width = 20
        self.height = 60
        self.shape = pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height), 0)
        self.upperhitbox = pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height / 2), 1)
        self.lowerhitbox = pygame.draw.rect(SCREEN, self.color, (self.x, self.y+30, self.width, self.height / 2), 1)
        self.score = 0

    def draw_updatescreen(self):
        self.shape = pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height), 0)
        self.upperhitbox = pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height / 2), 1)
        self.lowerhitbox = pygame.draw.rect(SCREEN, self.color, (self.x, self.y+30, self.width, self.height / 2), 1)
    
    def update(self, x, y):
        self.x = x
        self.y = y


#Ball class:
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.radius = 15
        self.shape = pygame.draw.circle(SCREEN, self.color, (self.x, self.y), self.radius)
        #self.hitbox = pygame.draw.rect(SCREEN, WHITE, (self.x, self.y, self.radius, self.radius), 1)
        self.x_velocity = 0.5
        self.y_velocity = 0
    
    def draw_updatescreen(self):
        self.shape = pygame.draw.circle(SCREEN, self.color, (self.x, self.y), self.radius)
        #self.hitbox = pygame.draw.rect(SCREEN, WHITE, (self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2), 1)
    
    def update(self, x, y, x_velocity, y_velocity):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        


#Enemy class:
class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.width = 20
        self.height = 60
        self.shape = pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height), 0)
        self.upperhitbox = pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height / 2), 1)
        self.lowerhitbox = pygame.draw.rect(SCREEN, self.color, (self.x, self.y+30, self.width, self.height / 2), 1)
        self.score = 0


    def draw_updatescreen(self):
        self.shape = pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height), 0)
        self.upperhitbox = pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height / 2), 1)
        self.lowerhitbox = pygame.draw.rect(SCREEN, self.color, (self.x, self.y+30, self.width, self.height / 2), 1)
    
    def update(self, x, y):
        self.x = x
        self.y = y


#Objects
player = Player(BLACK, 100, SCREENHEIGHT / 2)
ball = Ball(RED, (SCREENWIDTH / 2), (SCREENHEIGHT / 2))
enemy = Enemy(BLACK, 1050, SCREENHEIGHT / 2)

while True:
    user_input = pygame.key.get_pressed()
    FULLSCREEN = False
    SCREEN.fill(GRAY)
    SCREEN_OUTLINE = pygame.draw.rect(SCREEN, BLUE, (0, 0, SCREENWIDTH, SCREENHEIGHT), 2)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            mouseclicked = True
        if (user_input[pygame.K_F11]):
            pygame.display.toggle_fullscreen()
        else:
            mouseclicked = False
    
    #Movement:
    if (user_input[pygame.K_w]):
        player.y -= 0.5
    elif (user_input[pygame.K_s]):
        player.y += 0.5
    
    if (user_input[pygame.K_UP]):
        enemy.y -= 0.5
    elif (user_input[pygame.K_DOWN]):
        enemy.y += 0.5
    
    if (player.y + 60) >= SCREENHEIGHT:
        player.y -= 0.5
    elif player.y <= 0:
        player.y += 0.5
    
    if (enemy.y + 60) >= SCREENHEIGHT:
        enemy.y -= 0.5
    elif enemy.y <= 0:
        enemy.y += 0.5

    #Ball movement:
    ball.x -= ball.x_velocity
    ball.y -= ball.y_velocity

    #Ball colliding with player:
    if ball.shape.colliderect(player.upperhitbox):
        ball.x_velocity = rand.uniform(-0.5, -0.4)
        ball.y_velocity = rand.uniform(0.3, 0.5)
        #print (ball.x, ball.y)
    elif ball.shape.colliderect(player.lowerhitbox):
        ball.x_velocity = rand.uniform(-0.5, -0.4)
        ball.y_velocity = rand.uniform(-0.3, -0.5)
        #print (ball.x, ball.y)


    #Ball colliding with enemy:
    if ball.shape.colliderect(enemy.upperhitbox):
        ball.x_velocity = rand.uniform(0.4, 0.5)
        ball.y_velocity = rand.uniform(0.3, 0.5)
        print (ball.x, ball.y)
    elif ball.shape.colliderect(enemy.lowerhitbox):
        ball.x_velocity = rand.uniform(0.4, 0.5)
        ball.y_velocity = rand.uniform(-0.3, -0.5)
        print (ball.x, ball.y)
    
    #Ball colliding with top and bottom wall:
    if ball.y < 0:
        ball.y_velocity = -abs(ball.y_velocity)
    elif ball.y > 600:
        ball.y_velocity = abs(ball.y_velocity)

    
    if ball.x < 0:
        ball.x, ball.y = SCREENWIDTH / 2, SCREENHEIGHT / 2
        ball.x_velocity = rand.choice([-0.5, 0.5])
        ball.y_velocity = 0
        enemy.score += 1
        print (f"PLAYER SCORE: {player.score}, ENEMY SCORE: {enemy.score}")
    elif ball.x > SCREENWIDTH:
        ball.x, ball.y = SCREENWIDTH / 2, SCREENHEIGHT / 2
        ball.x_velocity = rand.choice([-0.5, 0.5])
        ball.y_velocity = 0
        player.score += 1
        print (f"PLAYER SCORE: {player.score}, ENEMY SCORE: {enemy.score}")

    #Object/Screen updates:
    player.draw_updatescreen()
    player.update(player.x, player.y)
    ball.draw_updatescreen()
    ball.update(ball.x, ball.y, ball.x_velocity, ball.y_velocity)
    enemy.draw_updatescreen()
    enemy.update(enemy.x, enemy.y)
    pygame.display.update()
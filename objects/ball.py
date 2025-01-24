import pygame, random as rand
from .player import player
from .enemy import enemy
from .display import display


#Ball class:
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.radius = 15
        self.shape = pygame.draw.circle(display.SCREEN, self.color, (self.x, self.y), self.radius)
        #self.hitbox = pygame.draw.rect(SCREEN, WHITE, (self.x, self.y, self.radius, self.radius), 1)
        self.x_velocity = 0.5
        self.y_velocity = 0
    
    def draw_updatescreen(self):
        self.shape = pygame.draw.circle(display.SCREEN, self.color, (self.x, self.y), self.radius)
        #self.hitbox = pygame.draw.rect(SCREEN, BLUE, (self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2), 1)
    
    def update(self, x, y, x_velocity, y_velocity):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
    
    def movement(self):
        self.x -= self.x_velocity
        self.y -= self.y_velocity
    
    def collision(self, player, enemy):
        #Ball colliding with player:
        if self.shape.colliderect(player.upperhitbox,):
            self.x_velocity = rand.uniform(-0.5, -0.4)
            self.y_velocity = rand.uniform(0.3, 0.5)

        elif ball.shape.colliderect(player.lowerhitbox):
            self.x_velocity = rand.uniform(-0.5, -0.4)
            self.y_velocity = rand.uniform(-0.3, -0.5)

        #Ball colliding with enemy:
        if self.shape.colliderect(enemy.upperhitbox):
            self.x_velocity = rand.uniform(0.4, 0.5)
            self.y_velocity = rand.uniform(0.3, 0.5)

        elif ball.shape.colliderect(enemy.lowerhitbox):
            self.x_velocity = rand.uniform(0.4, 0.5)
            self.y_velocity = rand.uniform(-0.3, -0.5)
        
        #Ball colliding with top and bottom wall:
        if ball.y < 0:
            ball.y_velocity = -abs(ball.y_velocity)
        elif ball.y > display.GAMEHEIGHT - 10: #-10 to make it look realistic, before part of the ball would cross over the blue outline.
            ball.y_velocity = abs(ball.y_velocity)

    def player_score(self, player):
        if ball.x > display.SCREENWIDTH:
            ball.x, ball.y = display.SCREENWIDTH / 2, display.SCREENHEIGHT / 2
            ball.x_velocity = rand.choice([-0.5, 0.5])
            ball.y_velocity = 0
            player.score += 1
    
    def enemy_score(self, enemy):
        if ball.x < 0:
            ball.x, ball.y = display.SCREENWIDTH / 2, display.SCREENHEIGHT / 2
            ball.x_velocity = rand.choice([-0.5, 0.5])
            ball.y_velocity = 0
            enemy.score += 1
    
    def functions(self):
        self.draw_updatescreen()
        self.update(self.x, self.y, self.x_velocity, self.y_velocity)
        self.collision(player, enemy)
        self.movement()
        self.player_score(player)
        self.enemy_score(enemy)


ball = Ball(display.RED, (display.SCREENWIDTH / 2), (display.SCREENHEIGHT / 2))
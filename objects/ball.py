import pygame, random as rand
from .player import player
from .enemy import enemy
from .display import display
from game_settings import game_setting


#Ball class:
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.radius = 15
        self.shape = pygame.draw.circle(display.SCREEN, self.color, (self.x, self.y), self.radius)
        #self.hitbox = pygame.draw.rect(SCREEN, WHITE, (self.x, self.y, self.radius, self.radius), 1)
        self.x_velocity = game_setting.x_velocity_min
        self.y_velocity = 0
        self.temp_x_velocity = self.x_velocity
        self.temp_y_velocity = self.y_velocity
    
    def draw_updatescreen(self):
        self.shape = pygame.draw.circle(display.SCREEN, self.color, (self.x, self.y), self.radius)
        #self.hitbox = pygame.draw.rect(SCREEN, BLUE, (self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2), 1)
    
    def update(self, x, y, x_velocity, y_velocity):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.temp_x_velocity = self.x_velocity
        self.temp_y_velocity = self.y_velocity

    def movement(self):
        self.x -= self.x_velocity
        self.y -= self.y_velocity
    
    def collision(self, player, enemy, game_setting):
        #Ball colliding with player:
        if self.shape.colliderect(player.upperhitbox) or self.shape.colliderect(player.lowerhitbox):
            self.x_velocity = rand.uniform(-abs(game_setting.x_velocity_min), -abs(game_setting.x_velocity_max))
            self.y_velocity = rand.choice([rand.uniform(game_setting.y_velocity_max, game_setting.y_velocity_min), rand.uniform(-abs(game_setting.y_velocity_max), -abs(game_setting.y_velocity_min))])

        #Ball colliding with enemy:
        if self.shape.colliderect(enemy.upperhitbox) or self.shape.colliderect(enemy.lowerhitbox):
            self.x_velocity = rand.uniform(game_setting.x_velocity_min, game_setting.x_velocity_max)
            self.y_velocity = rand.choice([rand.uniform(game_setting.y_velocity_max, game_setting.y_velocity_min), rand.uniform(-abs(game_setting.y_velocity_max), -abs(game_setting.y_velocity_min))])
        
        #Ball colliding with top and bottom wall:
        if self.y < 0:
            self.y_velocity = -abs(self.y_velocity)
        elif ball.y > display.GAMEHEIGHT - 10: #-10 to make it look realistic, before part of the ball would cross over the blue outline.
            self.y_velocity = abs(self.y_velocity)

    def player_score(self, player):
        if self.x > display.SCREENWIDTH:
            self.x, self.y = display.SCREENWIDTH / 2, display.SCREENHEIGHT / 2
            self.x_velocity = rand.choice([1, 1])
            self.y_velocity = 0
            player.score += 1
    
    def enemy_score(self, enemy):
        if self.x < 0:
            self.x, self.y = display.SCREENWIDTH / 2, display.SCREENHEIGHT / 2
            self.x_velocity = rand.choice([1, 1])
            self.y_velocity = 0
            enemy.score += 1
    
    def functions(self):
        self.draw_updatescreen()
        self.update(self.x, self.y, self.x_velocity, self.y_velocity)
        self.collision(player, enemy, game_setting)
        self.movement()
        self.player_score(player)
        self.enemy_score(enemy)


ball = Ball(display.RED, (display.SCREENWIDTH / 2), (display.SCREENHEIGHT / 2))
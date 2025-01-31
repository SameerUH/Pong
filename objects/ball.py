import pygame, random as rand
from .player import player
from .enemy import enemy
from .display import display
from game_settings import game_setting


#Ball class:
class Ball(pygame.sprite.Sprite):
    def __init__(self, colour, x, y):
        self.colour = colour
        self.x = x
        self.y = y
        self.radius = 15
        self.shape = pygame.draw.circle(display.SCREEN, self.colour, (self.x, self.y), self.radius)
        #self.hitbox = pygame.draw.rect(SCREEN, WHITE, (self.x, self.y, self.radius, self.radius), 1)
        self.x_velocity = game_setting.x_velocity_min
        self.y_velocity = 0
        self.temp_x_velocity = self.x_velocity
        self.temp_y_velocity = self.y_velocity
    
    def draw_updatescreen(self):
        self.shape = pygame.draw.circle(display.SCREEN, self.colour, (self.x, self.y), self.radius)
        #self.hitbox = pygame.draw.rect(SCREEN, BLUE, (self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2), 1)
    
    def update(self, x, y, x_velocity, y_velocity, colour):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.temp_x_velocity = self.x_velocity
        self.temp_y_velocity = self.y_velocity
        self.colour = colour

    def movement(self):
        self.x -= self.x_velocity
        self.y -= self.y_velocity
    
    def collision(self, player, enemy, game_setting):
        #Ball colliding with player:
        if self.shape.colliderect(player.hitbox):
            self.x_velocity = rand.uniform(-abs(game_setting.x_velocity_min), -abs(game_setting.x_velocity_max))
            if player.direction == "up":
                self.y_velocity = rand.uniform(game_setting.y_velocity_min, game_setting.y_velocity_max)
            elif player.direction == "down":
                self.y_velocity = rand.uniform(-abs(game_setting.y_velocity_min), -abs(game_setting.y_velocity_max))


        #Ball colliding with enemy:
        elif self.shape.colliderect(enemy.hitbox):
            self.x_velocity = rand.uniform(game_setting.x_velocity_min, game_setting.x_velocity_max)
            if enemy.direction == "up":
                self.y_velocity = rand.uniform(game_setting.y_velocity_min, game_setting.y_velocity_max)
            elif enemy.direction == "down":
                self.y_velocity = rand.uniform(-abs(game_setting.y_velocity_min), -abs(game_setting.y_velocity_max))
        
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
        self.update(self.x, self.y, self.x_velocity, self.y_velocity, self.colour)
        self.collision(player, enemy, game_setting)
        self.movement()
        self.player_score(player)
        self.enemy_score(enemy)


ball = Ball(display.RED, (display.SCREENWIDTH / 2), (display.SCREENHEIGHT / 2))
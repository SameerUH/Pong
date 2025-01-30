import pygame, math
#List of attributes in the setting class will be applied to the game.

class Game_setting(pygame.sprite.Sprite):
    def __init__(self):
        self.colour = "normal"
        self.speed = 1
        self.x_velocity_min, self.x_velocity_max = 1, 1.5
        self.y_velocity_min, self.y_velocity_max = 0.7, 1
        self.score = math.inf
    
    def update(self, colour = "normal", speed = 1, score = math.inf, x_velocity_min = 1, x_velocity_max = 1.5, y_velocity_min = 0.7, y_velocity_max = 1):
        self.colour = colour
        self.speed = speed
        self.score = score
        self.x_velocity_min, self.x_velocity_max = x_velocity_min, x_velocity_max
        self.y_velocity_min, self.y_velocity_max = y_velocity_min, y_velocity_max

game_setting = Game_setting()
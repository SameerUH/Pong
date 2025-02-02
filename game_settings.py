#Imports.
import pygame, math
#List of attributes in the setting class will be applied to the game.

class Game_setting(pygame.sprite.Sprite):
    """
    Class used as a constant object that holds settings to be updated

    Attributes:
        speed (int): Integer used as the speed for the players.
        x_velocity_min, x_velocity_max (float): Used as the speed for the ball when colliding with other objects.
        y_velocity_min, y_velocity_max (float): Used as the angle for the ball when colliding with other objects.
        score (int): Used to decide what the maximum score is for the players to win.
        computer: Used to decide whether or not the enemy is a player or a computer.
    """
    def __init__(self):
        """
        Constructor to set initial values for the object

        Basically the base settings when the program runs.
        """

        self.speed = 1
        self.x_velocity_min, self.x_velocity_max = 1, 1.5
        self.y_velocity_min, self.y_velocity_max = 0.7, 1
        self.score = math.inf
        self.computer = False

    def update(self, speed = 1, score = math.inf, x_velocity_min = 1, x_velocity_max = 1.5, y_velocity_min = 0.7, y_velocity_max = 1, computer = False):
        """
        Function used to update variables and modify settings of the programs, uses default values set to the values used in the constructor method.

        Args:
            speed (int): Integer used as the speed for the players (Set to infinity at first).
            x_velocity_min, x_velocity_max (float): Used as the speed for the ball when colliding with other objects.
            y_velocity_min, y_velocity_max (float): Used as the angle for the ball when colliding with other objects.
            score (int): Used to decide what the maximum score is for the players to win.
            computer: Used to decide whether or not the enemy is a player or a computer.
        """

        self.speed = speed
        self.score = score
        self.computer = computer
        self.x_velocity_min, self.x_velocity_max = x_velocity_min, x_velocity_max
        self.y_velocity_min, self.y_velocity_max = y_velocity_min, y_velocity_max

#Object creation.
game_setting = Game_setting()
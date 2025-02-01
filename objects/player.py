#Imports/file management to allow use of other modules and objects.
import pygame
from .display import display
from game_settings import game_setting

#Player class:
class Player(pygame.sprite.Sprite):
    """
    Class for the Player player (object on the left of the screen).

    Attributes:
        colour (list[ints]): List of integers to represent the colour of the player.
        x (int): x-coordinate of the player, set as a constant as they shouldn't be able to move in the x-axis.
        y (int): y-coordinate of the player, set as a variable to be passed through as a parameter.
        width, height (int): Size of the player.
        score (int): Score of the player.
        direction (string): Stores the direction the player is going to be used in the balls movement function.
        shape (inbuilt): Uses other attributes to display the player.
        hitbox (inbuilt): Uses other attributes to display the hitbox of the player (for testing purposes)
    """

    def __init__(self, colour, y):
        """
        Constructor of the player class.

        Args:
            colour (list[ints]): Initial colour of the player.
            y (int): Initial y-coordinate of the player.
        """
        self.colour = colour
        self.x = 100
        self.y = y
        self.width = 20
        self.height = 60
        self.direction = "normal"
        self.score = 0

    def draw_updatescreen(self):
        #Function to display the player object and create the hitbox to be used in the ball's movement function.
        self.shape = pygame.draw.rect(display.SCREEN, self.colour, (self.x, self.y, self.width, self.height), 0)
        self.hitbox = pygame.draw.rect(display.SCREEN, self.colour, (self.x, self.y, self.width, self.height), 1)

    def update(self, y, score, colour):
        """
        Function to update/keep track of the player's attributes during the game.

        Args:
            y (int): Keeps track of the player's y value.
            colour (list[ints]): Updates the colour of the player if different vision modes are used.
        """
        self.x = 100
        self.y = y
        self.score = score
        self.colour = colour

    def movement(self, user_input):
        """
        Function which controls the movement of the player when the user uses the keyboard and keeps track of which direction the player is going.
        
        First checks which screen is being shown and then allows the user to move the player, if the player is about to hit the top or bottom of the screen then it provides a counter velocity to stop the object from going off the screen.

        If the game is paused the player shouldn't be able to move.

        Args:
            user_input (inbuilt): Defined in main.py and keeps track whenever the user presses a certain key.
        """
        if display.state == "game_screen":
            if (user_input[pygame.K_w]):
                self.y -= game_setting.speed
                self.direction = "up"
            elif (user_input[pygame.K_s]):
                self.y += game_setting.speed
                self.direction = "down"
            
            if (self.y + 60) >= display.GAMEHEIGHT:
                self.y -= game_setting.speed
            elif self.y <= 0:
                self.y += game_setting.speed
            
        if display.state == "pause_screen":
            if (user_input[pygame.K_w]):
                self.y -= 0
            elif (user_input[pygame.K_s]):
                self.y += 0
    
    
    def functions(self, user_input):
        """
        Function which calls and updates other functions above, used to keep track of multiple changes with one line.
        """
        self.draw_updatescreen()
        self.update(self.y, self.score, self.colour)
        self.movement(user_input)

#Player creation.
player = Player(display.BLACK, display.SCREENHEIGHT / 2)
        



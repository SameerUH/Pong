#Imports/file management to allowing use of other modules/objects.
import pygame
from .display import display
from game_settings import game_setting

#Enemy class:
class Enemy(pygame.sprite.Sprite):
    """
    Class for the enemy user (player on the right):

    Attributes:
        colour (int): Colour of the enemy.
        x (int): x-coordinate of the enemy, set as a constant as they shouldn't be able to move in the x-axis.
        y (int): y-coordinate of the enemy, set as a variable to be passed through as a parameter.
        width, height (int): Size of the enemy.
        score (int): Score of the enemy.
        direction (string): Stores the direction the enemy is going to be used in the balls movement function.
        shape (inbuilt): Uses other attributes to display the enemy.
        hitbox (inbuilt): Uses other attributes to display the hitbox of the enemy (for testing purposes)
    """

    def __init__(self, colour, y):
        """
        Constructor of the enemy class.

        Args:
            colour (int): Initial colour of the enemy.
            y (int): Initial y-coordinate of the enemy, set as a variable to be passed through as a parameter.
        """
        self.colour = colour
        self.x = 1050
        self.y = y
        self.width = 20
        self.height = 60
        self.score = 0
        self.direction = "normal"
        self.hitbox = pygame.draw.rect(display.SCREEN, self.colour, (self.x, self.y, self.width, self.height), 1)

    def draw_updatescreen(self):
        """
        Function which displays the enemy using the 'pygame.draw.rect' function, whilst also keeping track of where the hitbox is.
        """
        self.shape = pygame.draw.rect(display.SCREEN, self.colour, (self.x, self.y, self.width, self.height), 0)
        self.hitbox = pygame.draw.rect(display.SCREEN, self.colour, (self.x, self.y, self.width, self.height), 1)
    
    def update(self, y, score, colour):
        """
        Function which constantly updates variables of the enemy if settings are changed or the behaviour of the game changes.

        Args:
            y (int): Tracks the y-coordinate of the enemy.
            score (int): Tracks the score of the enemy.
            colour (list[int]): List of integers (using the RGB scale) to display the colour of the enemy.
        
        """
        self.y = y
        self.score = score
        self.colour = colour

    def movement(self, user_input):
        """
        Function which controls the movement of the enemy when the user uses the keyboard and keeps track of the direction the enemy is going.
        
        First checks which screen is being shown and then allows the user to move the enemy, if the enemy is about to hit the top or bottom of the screen then it provides a counter velocity to stop the object from going off the screen.

        If the game is paused the enemy shouldn't be able to move.

        Args:
            user_input (inbuilt): Defined in main.py and keeps track whenever the user presses a certain key.
        """
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
        """
        Function which uses and calls the other functions above, making it easier to update multiple values and checks simultaneously.

        Args:
            user_input (inbuilt): Defined in main.py and is passed as a parameter to keep track of which key has been pressed.
        """
        self.draw_updatescreen()
        self.update(self.y, self.score, self.colour)
        self.movement(user_input)

#Object creation
enemy = Enemy(display.BLACK, display.SCREENHEIGHT / 2)
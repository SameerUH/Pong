#Imports
import pygame


class Display(pygame.sprite.Sprite):
    """
    Class to control the screen of the game, allows other modules/files to make changes without causing errors (Such as deadlocks or circular waits).

    Attributes:
        SCREENWIDTH, SCREENHEIGHT (int): Width and height of the screen.
        SCREENSIZE (list): Stores the width and height in a list to be used with inbuilt functions.
        GAMEHEIGHT (int): Height of the game to allow other text such as points and buttons to be displayed without altering the behaviour of the game.
        Colours (list[int]): NOT ACTUALLY IN A LIST, but each colour has a RGB value set to it which is used for attributes of other objects in the game.
        state (string): Controls which screen the program is on.
        vision (string): Controls whether or not the game is in colourblind mode or note.
        paused (boolean): Decided whether or not the game has been paused or not.
    """
    
    def __init__(self, state, vision):
        """
        Constructor for the display object.

        Args:
            state (string): Sets the initial screen value of the game.
            vision (string): Sets the initial vision mode of the game.
        """
        self.SCREENWIDTH = 1150
        self.SCREENHEIGHT = 700
        self.SCREENSIZE = [self.SCREENWIDTH, self.SCREENHEIGHT]
        self.SCREEN = pygame.display.set_mode(self.SCREENSIZE)
        self.GAMEHEIGHT = 600
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GRAY = (211, 211, 211)
        self.BLUE = (0, 0, 255)
        self.DARK_GRAY = (100, 100, 100)
        self.GREEN = (0,255,0)
        self.PURPLE = (255, 0, 255)
        self.LIGHT_BLUE = (173, 216, 230)
        self.ORANGE = (255, 165, 0)
        self.YELLOW = (255, 215, 0)
        self.MAROON = (128, 0, 0)
        self.state = state
        self.vision = vision
        self.paused = None

#Object creation with parameters passed in.
display = Display("intro_screen", "normal_mode")
import pygame


class Display(pygame.sprite.Sprite):
    def __init__(self, state, vision):
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


display = Display("start_screen", "normal_mode")
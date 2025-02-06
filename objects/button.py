#Imports/access to other files/modules.
import pygame, sys, math
from .display import display
from .ball import ball
from game_settings import game_setting
pygame.init()


class Button(pygame.sprite.Sprite):
    """
    Class for the buttons/text in the game.

    Attributes:
        colour (list[ints]): Background colour of the button which is passed in through the display object.
        x, y (int): Coordinates of the button.
        width, height (int): Controls the size of the button.
        shape (inbuilt): Creates the rectangular shape of the button.
        text (string): Stores the text of the button passed through the object creation.
        font_size (int): Stores the size of the font for the text.
        display_text (inbuilt): Renders the text to be displayed.
        display_text_rect (inbuilt): Gets the shape of the text to be displayed..
        display.SCREEN.blit (inbuilt): Displays the text on the button.
        """
    
    def __init__(self, colour, x, y, width, height, text, font_size):
        """
        Constructor for the button class.

        Args:
            colour (int): Initial background colour of the buttons.
            x, y (int): Initial coordinates for the buttons in the game.
            width, height (int): Initial size of the buttons.
            shape (inbuilt): Initial rectangular shape of the button.
            text (string): Initial text of the buttons.
            font_size (int): Initial size of the font for the text.
        """
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = text
        self.font_size = font_size
    
    def draw_updatescreen(self):
        """
        Function which constantly displays the button.

        Uses inbuilt functions such as .Font, .Rect, .render etc, to control the attributes of the text.
        """
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(display.SCREEN, self.colour, self.shape)
        font = pygame.font.Font('freesansbold.ttf', self.font_size)
        display_text = font.render(self.text, True, display.WHITE)
        display_text_rect = display_text.get_rect()
        display_text_rect.center = (self.x + (self.width/2), self.y + (self.height / 2) )
        display.SCREEN.blit(display_text, display_text_rect)
    
    def interaction(self, mouse_pos, mouse_clicked):
        """
        Function which controls what happens when each button is clicked.

        First checks if the mouse is within the button shape, then checks if the button has been clicked, finally checks which screen is being displayed and which button has been clicked.
        
        Args:
            mouse_pos (list[int]): Constantly tracks the mouse position to check if it's in a button shape or not.
            mouse_clicked (boolean): Tracks when the mouse has been clicked using booleans (True/False).
        """
        if mouse_pos[1] < self.shape[1] + self.shape[3] and mouse_pos[1] > self.shape[1]:
            if mouse_pos[0] > self.shape[0] and mouse_pos[0] < self.shape[0] + self.shape[2]:
                if mouse_clicked:
                    #Intro screen buttons:
                    if display.state == "intro_screen":
                        if self.text == "SKIP":
                            display.state = "start_screen"

                    #Start screen buttons:
                    if display.state == "start_screen":
                        if self.text == "PLAY GAME":
                            display.state = "computer_decider_screen"

                        elif self.text == "SETTINGS":
                            display.state = "settings_screen"

                        elif self.text == "QUIT":
                            pygame.quit()
                            sys.exit()
                    
                    #Gamemode screen buttons:
                    elif display.state == "computer_decider_screen":
                        if self.text == "2 PLAYERS":
                            display.state = "game_screen"
                            game_setting.computer = False
                        
                        elif self.text == "COMPUTER":
                            display.state = "game_screen"
                            game_setting.computer = True
                        
                        elif self.text == "GO BACK":
                            display.state = "start_screen"
                    
                    #Main game screen buttons:
                    elif display.state == "game_screen":
                        if self.text == "PAUSE":
                            display.state = "pause_screen"

                    elif display.state == "pause_screen":
                        if self.text == "CONTINUE":
                            display.state = "game_screen"

                        elif self.text == "END GAME":
                            display.state = "start_screen"

                    #Settings screen buttons:
                    elif display.state == "settings_screen":
                        if self.text == "GO BACK":
                            display.state = "start_screen"

                        elif self.text == "SPEED: NORMAL":
                            self.text = "SPEED: FAST"
                            self.colour = display.GREEN
                            game_setting.x_velocity_min, game_setting.x_velocity_max = 1.5, 2
                            game_setting.y_velocity_min, game_setting.y_velocity_max = 1.3, 1.6
                            game_setting.speed = 2
                        
                        elif self.text == "SPEED: FAST":
                            self.text = "SPEED: SLOW"
                            self.colour = display.RED
                            game_setting.x_velocity_min, game_setting.x_velocity_max = 0.5, 1
                            game_setting.y_velocity_min, game_setting.y_velocity_max = 0.4, 0.7
                            game_setting.speed = 0.5
                            
                        elif self.text == "SPEED: SLOW":
                            self.text = "SPEED: NORMAL"
                            self.colour = display.YELLOW
                            game_setting.x_velocity_min, game_setting.x_velocity_max = 1, 1.5
                            game_setting.y_velocity_min, game_setting.y_velocity_max = 0.7, 1
                            game_setting.speed = 1
                            
                        elif self.text == "COLOURBLIND":
                            self.text = "NORMAL"
                            self.colour = display.DARK_GRAY
                            display.vision = "colourblind_mode"
                            
                        elif self.text == "NORMAL":
                            self.text = "COLOURBLIND"
                            self.colour = display.BLUE
                            display.vision = "normal_mode"
                        

                        elif self.text == "SCORE:MAX":
                            game_setting.score = 1
                            self.text = "SCORE: 1"

                        elif self.text == f"SCORE: {game_setting.score}":
                            game_setting.score += 1
                            self.text = f"SCORE: {game_setting.score}"
                            if game_setting.score > 10:
                                game_setting.score = math.inf
                                self.text = "SCORE:MAX"

                    #Winner screen buttons:
                    elif display.state == "winner_screen":
                        if self.text == "QUIT":
                            display.state = "start_screen"
                        
                    pygame.time.delay(100) #Delay to stop multiple inputs when the mouse has been clicked once.
                            

    def update(self, x, y): 
        """
        Function which updates the x and y values of certain buttons/text.

        Args:
            x (int): Tracks the x-coordinate of the object.
            y (int): Tracks the y-coordinate of the object.
        """
        self.x = x
        self.y = y
    
    def functions(self, mouse_pos, mouse_clicked):
        """
        Function which contains the functions above to call with one line. (Avoids messy code)
        
        Args:
            mouse_pos (list[int]): Used for interaction checks.
            mouse_clicked (boolean): Also used for interaction checks.
        """
        self.draw_updatescreen()
        self.interaction(mouse_pos, mouse_clicked)
        self.update(self.x, self.y)

#Creation of all the buttons/text that are used in the program with parameters passed through:

#Intro screen:
SKIP = Button(display.DARK_GRAY, 450, 600, 300, 100, "SKIP", 50)

#Start screen:
PONG_TITLE = Button(display.DARK_GRAY, 425, 50, 300, 100, "PONG", 50)
PLAY_GAME = Button(display.BLUE, 425, 200, 300, 100, "PLAY GAME", 50)
SETTINGS = Button(display.RED, 200, 400, 300, 100, "SETTINGS", 50)
QUIT = Button(display.PURPLE, 600, 400, 300, 100, "QUIT", 50)

#Main game:
PAUSE = Button(display.GREEN, 425, 600, 300, 100, "PAUSE", 50)

#Pause screen:
CONTINUE = Button(display.GREEN, 200, 400, 300, 100, "CONTINUE", 50)
PAUSED = Button(display.BLACK, 400, 200, 300, 100, "PAUSED", 50)
END_GAME = Button(display.RED, 600, 400, 300, 100, "END GAME", 50)

#Settings screen:
GO_BACK = Button(display.ORANGE, 100, 200, 300, 100, "GO BACK", 50)
COLOURBLIND = Button(display.BLUE, 700, 200, 300, 100, "COLOURBLIND", 35)
SPEED = Button(display.YELLOW, 700, 400, 300, 100, "SPEED: NORMAL", 35)
SCORE = Button(display.MAROON, 100, 400, 325, 100, "SCORE:MAX", 50)

#Winner screen:
CONGRATULATIONS = Button(display.GREEN, 300, 50, 600, 100, "CONGRATULATIONS!!!", 50)
WINNER = Button(display.BLUE, 375, 225, 400, 100, "NONE", 50)

#Computer decider screen:
TWO_PLAYER = Button(display.BLUE, 200, 300, 300, 100, "2 PLAYERS", 50)
COMPUTER = Button(display.RED, 600, 300, 300, 100, "COMPUTER", 50)
GAMEMODE = Button(display.DARK_GRAY, 400, 100, 325, 100, "GAMEMODE", 50)
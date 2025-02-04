#Imports/access from other modules/files.
import pygame, random as rand
from .display import display
from game_settings import game_setting


#Ball class:
class Ball(pygame.sprite.Sprite):
    """
    Class for the ball in the game.

    Attributes:
        colour (int): The colour of the ball which is passed in through the display object.
        x, y (int): Coordinates of the ball.
        radius (int): Size of the ball.
        x_velocity (int): Speed of the ball which either decrements/increments the x-coordinate to display ball movement on the x-axis.
        y_velocity (int): Speed of the ball which either decrements/increments the y-coordinate to display movement on the y-axis.
        temp_x_velocity, temp_y_velocity (int): Stores the current x and y velocity so the program remembers the speed of the ball when the game is paused.
    """
    
    def __init__(self, colour, x, y):
        """
        Constructer for the ball class

        Args:
            colour (int): Sets the colour of the ball.
            x (int): Sets the initial x-coordinate.
            y (int): Sets the initial y-coordinate.        
        """
        self.colour = colour
        self.x = x
        self.y = y
        self.radius = 15
        self.x_velocity = game_setting.x_velocity_min
        self.y_velocity = 0
        self.temp_x_velocity = self.x_velocity
        self.temp_y_velocity = self.y_velocity
        self.shape = pygame.draw.circle(display.SCREEN, self.colour, (self.x, self.y), self.radius)
        self.wall_hit = False
        self.wall_predict_x = self.x
        self.wall_predict_y = self.y
        self.direction = "unknown"
    
    def draw_updatescreen(self):
        """
        Function which constantly draws the ball using the inbuilt (pygame.draw.circle) function.
        
        Uses self to use the updated variables of the ball and has a hitbox line commented for debugging purposes.
        """

        self.shape = pygame.draw.circle(display.SCREEN, self.colour, (self.x, self.y), self.radius)
        #self.hitbox = pygame.draw.rect(SCREEN, BLUE, (self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2), 1)
    
    def update(self, x, y, x_velocity, y_velocity, colour, wall_hit):
        """
        Function which constantly updates the values of the ball to allow changes in the game.

        Args:
            x (int): x-coordinate of the ball.
            y (int): y-coordinate of the ball.
            x_velocity (int): Speed/direction of the ball on the x-axis.
            y_velocity (int): Speed/direction of the ball on the y-axis.
            colour (int): Colour of the ball which can be changed through the colourblind setting.
        """

        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.temp_x_velocity = self.x_velocity
        self.temp_y_velocity = self.y_velocity
        self.colour = colour
        self.wall_hit = wall_hit
        self.wall_predict_x = self.wall_predict_x
        self.wall_predict_y = self.wall_predict_y
        self.direction = self.direction


    def movement(self):
        """
        Function which constantly moves the ball depending on the velocity variables of the ball.
        """

        self.x -= self.x_velocity
        self.y -= self.y_velocity

        if self.y_velocity == 0:
            self.wall_hit = True
    
    def collision(self):
        """
        Function which bounces the ball in the opposite direction when it hits the top or bottom wall.
        """

        #Ball colliding with top and bottom wall:
        
        if self.y < 0:
            self.y_velocity = -abs(self.y_velocity)
            self.wall_hit = True
            ball.wall_predict_y = ball.y
            ball.wall_predict_x = ball.x
        elif ball.y > display.GAMEHEIGHT - 10: #-10 to make it look realistic, before part of the ball would cross over the blue outline.
            self.wall_hit = True
            self.y_velocity = abs(self.y_velocity)
            ball.wall_predict_y = ball.y
            ball.wall_predict_x = ball.x

        

    def functions(self):
        """
        Stores the functions above in one main function, making it easier to call and update multiple functions/variables at once.
        """

        self.draw_updatescreen()
        self.update(self.x, self.y, self.x_velocity, self.y_velocity, self.colour, self.wall_hit)
        self.collision()
        self.movement()


ball = Ball(display.RED, (display.SCREENWIDTH / 2), (display.SCREENHEIGHT / 2))
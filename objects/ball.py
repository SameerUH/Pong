#Imports/access from other modules/files.
import pygame, random as rand
from .player import player
from .enemy import enemy
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
    
    def draw_updatescreen(self):
        """
        Function which constantly draws the ball using the inbuilt (pygame.draw.circle) function.
        
        Uses self to use the updated variables of the ball and has a hitbox line commented for debugging purposes.
        """
        self.shape = pygame.draw.circle(display.SCREEN, self.colour, (self.x, self.y), self.radius)
        #self.hitbox = pygame.draw.rect(SCREEN, BLUE, (self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2), 1)
    
    def update(self, x, y, x_velocity, y_velocity, colour):
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

    def movement(self):
        """
        Function which constantly moves the ball depending on the velocity variables of the ball.
        """
        self.x -= self.x_velocity
        self.y -= self.y_velocity
    
    def collision(self, player, enemy, game_setting):
        """
        Checks when the ball collides with the players and changes it's behaviour accordingly. Uses '-abs' function to use convert positive speeds to negatives making the ball go the opposite direction.

        Parameters:
            player (object): Object on the left of the screen which the player controls.
            enemy (object): Object on the right of the screen that another player controls.
            game_setting (object): Manages the behaviour of the entire game such as maximum score, state, speed etc.

        Output:
            Depending on the direction the players are going, the ball with move up or down, the angle at which the ball moves is random.
        """
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
        """
        Function which constantly checks if the player has gained a point by checking if the x value has passed a certain value. If it has it updates the score and sets the ball back to the center of the game.

        Args:
            player (object): Updates the score variable in the player object.
        
        """
        if self.x > display.SCREENWIDTH:
            self.x, self.y = display.SCREENWIDTH / 2, display.SCREENHEIGHT / 2
            self.x_velocity = rand.choice([1, 1])
            self.y_velocity = 0
            player.score += 1
    
    def enemy_score(self, enemy):
        """
        Function which constantly checks if the enemy has gained a point by checking if the x value has passed a certain value. If it has it updates the enemy's score and sets the ball back the center of the game.

        Args:
            enemy (object): Updates the score variable in the enemy object.

        """
        if self.x < 0:
            self.x, self.y = display.SCREENWIDTH / 2, display.SCREENHEIGHT / 2
            self.x_velocity = rand.choice([1, 1])
            self.y_velocity = 0
            enemy.score += 1
    
    def functions(self):
        """
        Stores the functions above in one main function, making it easier to call and update multiple functions/variables at once.
        """
        self.draw_updatescreen()
        self.update(self.x, self.y, self.x_velocity, self.y_velocity, self.colour)
        self.collision(player, enemy, game_setting)
        self.movement()
        self.player_score(player)
        self.enemy_score(enemy)


ball = Ball(display.RED, (display.SCREENWIDTH / 2), (display.SCREENHEIGHT / 2))
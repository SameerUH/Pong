#Imports/file management to allowing use of other modules/objects.
import pygame, random as rand
from .display import display
from .player import player
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

    def movement(self, user_input, ball):
        """
        Function which controls the movement of the enemy when the user uses the keyboard and keeps track of the direction the enemy is going.
        
        First checks which screen is being shown and then allows the user to move the enemy, if the enemy is about to hit the top or bottom of the screen then it provides a counter velocity to stop the object from going off the screen.

        If the game is paused the enemy shouldn't be able to move.

        Args:
            user_input (inbuilt): Defined in main.py and keeps track whenever the user presses a certain key.
        """
        if display.state == "game_screen":
            if game_setting.computer == False:
                if (user_input[pygame.K_UP]):
                    self.y -= game_setting.speed
                    self.direction = "up"
                elif (user_input[pygame.K_DOWN]):
                    self.y += game_setting.speed
                    self.direction = "down"
                else:
                    self.direction = "stationary"
            
            elif game_setting.computer == True:
                if self.y > ball.y:
                    self.y -= game_setting.speed
                    self.direction = "up"
                elif self.y < ball.y:
                    self.y += game_setting.speed
                    self.direction = "down"
                else:
                    self.direction = "stationary"
    
        if display.state == "pause_screen":
            if (user_input[pygame.K_UP]):
                self.y -= 0
            elif (user_input[pygame.K_DOWN]):
                self.y += 0
        
        if (self.y + 60) >= display.GAMEHEIGHT:
            self.y -= game_setting.speed
        elif self.y <= 0:
            self.y += game_setting.speed

    def collision(self, ball):
        """
        Checks when the ball collides with the enemy and changes it's behaviour accordingly. Uses '-abs' function to use convert positive speeds to negatives making the ball go the opposite direction.

        Parameters:
            Ball (object): Collides with players and used to score points.

        Output:
            Depending on the direction the enemy are going, the ball with move up or down, the angle at which the ball moves is random.
        """

        #Ball colliding with enemy:
        if ball.shape.colliderect(self.hitbox):
            ball.wall_hit = False
            ball.x_velocity = rand.uniform(game_setting.x_velocity_min, game_setting.x_velocity_max)
            if enemy.direction == "up":
                ball.y_velocity = rand.uniform(game_setting.y_velocity_min, game_setting.y_velocity_max)
            elif enemy.direction == "down":
                ball.y_velocity = rand.uniform(-abs(game_setting.y_velocity_min), -abs(game_setting.y_velocity_max))

    def enemy_score(self, ball):
        """
        Function which constantly checks if the enemy has gained a point by checking if the x value has passed a certain value. If it has it updates the score and sets the ball back to the center of the game.

        Args:
            Ball (object): Collides with players and used to score points.
        """
        
        if ball.x < 0:
            ball.x, ball.y = display.SCREENWIDTH / 2, display.SCREENHEIGHT / 2
            ball.x_velocity = rand.choice([1, 1])
            ball.y_velocity = 0
            self.score += 1
    

    def functions(self, user_input, ball):
        """
        Function which uses and calls the other functions above, making it easier to update multiple values and checks simultaneously.

        Args:
            user_input (inbuilt): Defined in main.py and is passed as a parameter to keep track of which key has been pressed.
        """
        self.draw_updatescreen()
        self.update(self.y, self.score, self.colour)
        self.movement(user_input, ball)
        self.collision(ball)
        self.enemy_score(ball)

#Object creation
enemy = Enemy(display.BLACK, display.SCREENHEIGHT / 2)
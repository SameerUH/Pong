#Gonna try and add animations to the screen, possibly an intro one saying pong with the pygame.draw.line feature.
import pygame
import pygame.gfxdraw
from objects import display

animation_speed = 0.5
letter_p = 550
p_count = 0
letter_p_2 = 100
def intro_screen():
    global letter_p, animation_speed, p_count, letter_p_2
    display.SCREEN.fill(display.BLACK)
    if letter_p != 93:
        letter_p -= animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (100, 550), (100, letter_p), 15)
    elif letter_p_2 != 300:
        letter_p_2 += animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (100, 550), (100, letter_p), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (100, 100), (letter_p_2, 100), 15)
    else:
        pygame.draw.line(display.SCREEN, display.WHITE, (100, 550), (100, letter_p), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (100, 100), (letter_p_2, 100), 15)
        pygame.time.wait(2000)
        display.state = "start_screen"

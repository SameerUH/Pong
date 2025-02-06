#Imports/file management.
import pygame
from objects import display, SKIP

#Speed at which the letters are drawn at.
animation_speed = 1

#Letter P start coordinates.
letter_p = 550
letter_p_2 = 100
letter_p_3 = 100
letter_p_4 = 285

#Letter O start coordinates.
letter_o = 550
letter_o_2 = 350
letter_o_3 = 100
letter_o_4 = 525

#Letter N start coordinates.
letter_n = 550
letter_n_2 = 600
letter_n_3 = 93
letter_n_4 = 550


#Letter G start coordinates.
letter_g = 1050
letter_g_2 = 100
letter_g_3 = 868
letter_g_4 = 558
letter_g_5 = 1057

def intro_screen(mouse_pos, mouse_clicked):
    """
    Function draws the intro scene for the game.

    Does so by constantly drawing a line with an always updating end coordinate by incrementing/decrementing with the animation speed to display a line being drawn and make it look as if someone is writing the word PONG. The behaviour of this is controlled with selection statements (if, elif, else) to determine the end coordinates of the each line.

    It waits for the previous letters to be written before starting to write the next letter and then waits for 1 second and changes to the start screen. Also contains a skip button and when clicked it instantly jumps to the start screen.

    
    """

    global animation_speed, letter_p, letter_p_2, letter_p_3, letter_p_4, letter_o, letter_o_2, letter_o_3, letter_o_4, letter_n, letter_n_2, letter_n_3, letter_n_4, letter_g, letter_g_2, letter_g_3, letter_g_4, letter_g_5

    #Constantly makes sure the background is black and that the SKIP button is shown.
    display.SCREEN.fill(display.BLACK)
    SKIP.functions(mouse_pos, mouse_clicked)

    #LETTER P:
    if letter_p != 93:
        letter_p -= animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (75, 558), (75, letter_p), 15)
    elif letter_p_2 != 275:
        letter_p_2 += animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (75, 558), (75, letter_p), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (75, 100), (letter_p_2, 100), 15)
    elif letter_p_3 != 275:
        letter_p_3 += animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (75, 558), (75, letter_p), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (75, 100), (letter_p_2, 100), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_p_2, 93), (letter_p_2, letter_p_3), 15)
    elif letter_p_4 != 75:
        letter_p_4 -= animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (75, 558), (75, letter_p), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (75, 100), (letter_p_2, 100), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_p_2, 93), (letter_p_2, letter_p_3), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (282, letter_p_3), (letter_p_4, letter_p_3), 15)
    else:
        pygame.draw.line(display.SCREEN, display.WHITE, (75, 558), (75, letter_p), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (75, 100), (letter_p_2, 100), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_p_2, 93), (letter_p_2, letter_p_3), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (282, letter_p_3), (letter_p_4, letter_p_3), 15)


    #LETTER O:
    if letter_o != 93 and letter_p_4 == 75:
        letter_o -= animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (350, 558), (350, letter_o), 15)
    elif letter_o != 93 and letter_p_4 != 75:
        pygame.draw.line(display.SCREEN, display.BLACK, (350, 558), (350, letter_o), 15)
    elif letter_o_2 != 525 and letter_o == 93:
        letter_o_2 += animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (350, 558), (350, letter_o), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (350, 100), (letter_o_2, 100), 15)
    elif letter_o_3 != 552:
        letter_o_3 += animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (350, 558), (350, letter_o), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (350, 100), (letter_o_2, 100), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (518, 100), (518, letter_o_3), 15)
    elif letter_o_4 != 343:
        letter_o_4 -= animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (350, 558), (350, letter_o), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (350, 100), (letter_o_2, 100), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (518, 100), (518, letter_o_3), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_o_2, letter_o_3), (letter_o_4, letter_o_3), 15)
    else:
        pygame.draw.line(display.SCREEN, display.WHITE, (350, 558), (350, letter_o), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (350, 100), (letter_o_2, 100), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (518, 100), (518, letter_o_3), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_o_2, letter_o_3), (letter_o_4, letter_o_3), 15)
    
    #LETTER N:
    if letter_n != 93 and letter_o_4 == 343:
        letter_n -= animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (600, 558), (600, letter_n), 15)
    elif letter_n != 93 and letter_o_4 != 343:
        pygame.draw.line(display.SCREEN, display.BLACK, (600, 558), (600, letter_n), 15)
    elif letter_n_2 != 775 and letter_n_3 != 558 and letter_n == 93:
        letter_n_2 += (animation_speed / 4.5)
        letter_n_3 += (animation_speed / 2)
        pygame.draw.line(display.SCREEN, display.WHITE, (600, 558), (600, letter_n), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (600, letter_n), (letter_n_2, letter_n_3), 15)
    elif letter_n_4 != 93:
        letter_n_4 -= animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (600, 558), (600, letter_n), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (600, letter_n), (letter_n_2, letter_n_3), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_n_2, letter_n_3), (letter_n_2, letter_n_4), 15)
    else:
        pygame.draw.line(display.SCREEN, display.WHITE, (600, 558), (600, letter_n), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (600, letter_n), (letter_n_2, letter_n_3), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_n_2, letter_n_3), (letter_n_2, letter_n_4), 15)
    
    #LETTER G:
    if letter_g != 875 and letter_n_4 == 93:
        letter_g -= animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (1057, 100), (letter_g, 100), 15)
    elif letter_g != 875 and letter_n_4 != 93:
        pygame.draw.line(display.SCREEN, display.BLACK, (1057, 100), (letter_g, 100), 15)
    elif letter_g_2 != 558 and letter_g == 875:
        letter_g_2 += animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (1057, 100), (letter_g, 100), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_g, 93), (letter_g, letter_g_2), 15)
    elif letter_g_3 != 1050:
        letter_g_3 += animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (1057, 100), (letter_g, 100), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_g, 93), (letter_g, letter_g_2), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (868, letter_g_2), (letter_g_3, letter_g_2), 15)
    elif letter_g_4 != 400:
        letter_g_4 -= animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (1057, 100), (letter_g, 100), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_g, 93), (letter_g, letter_g_2), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (868, letter_g_2), (letter_g_3, letter_g_2), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_g_3, 565), (letter_g_3, letter_g_4), 15)
    elif letter_g_5 != 950:
        letter_g_5 -= animation_speed
        pygame.draw.line(display.SCREEN, display.WHITE, (1057, 100), (letter_g, 100), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_g, 93), (letter_g, letter_g_2), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (868, letter_g_2), (letter_g_3, letter_g_2), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_g_3, 565), (letter_g_3, letter_g_4), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (1057, letter_g_4), (letter_g_5, letter_g_4), 15)
    else:
        pygame.draw.line(display.SCREEN, display.WHITE, (1057, 100), (letter_g, 100), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_g, 93), (letter_g, letter_g_2), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (868, letter_g_2), (letter_g_3, letter_g_2), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (letter_g_3, 565), (letter_g_3, letter_g_4), 15)
        pygame.draw.line(display.SCREEN, display.WHITE, (1057, letter_g_4), (letter_g_5, letter_g_4), 15)
    
    #Pause at the end and transition to the start screen.
    if letter_g_5 == 950:
        pygame.time.wait(1000)
        display.state = "start_screen"
        


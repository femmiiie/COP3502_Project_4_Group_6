#IMPORTS
#double import for type casting
import pygame
from pygame import *

from board import Board
from helper_methods import *
from constants import *
import globals

pygame.init()



#Renders all Main Menu Elements, Buttons, Etc.
def render_menu(screen:Surface, mouse_pos:tuple[int, int], current_event:int):
    screen.fill('blue')

    easy_location = draw_button(screen, WINDOW_LENGTH_CENTER - 200, 500, 10, 'EASY', WHITE, BLACK)
    medium_location = draw_button(screen, WINDOW_LENGTH_CENTER, 500, 10, 'MEDIUM', WHITE, BLACK)
    hard_location = draw_button(screen, WINDOW_LENGTH_CENTER + 200, 500, 10, 'HARD', WHITE, BLACK)
    exit_location = draw_button(screen, 10, 10, 10, "EXIT", WHITE, BLACK)

    if current_event == pygame.MOUSEBUTTONUP:
        if check_if_pressed(mouse_pos, easy_location):
            start_game(30, screen)
        elif check_if_pressed(mouse_pos, medium_location):
            start_game(40, screen)
        elif check_if_pressed(mouse_pos, hard_location):
            start_game(50, screen)
        elif check_if_pressed(mouse_pos, exit_location):
            exit()
            
            

#Renders all Game Elements, Handles Game Logic, Etc.
def render_game(screen:Surface, mouse_pos:tuple[int, int], current_event:int):
    screen.fill('red')
    space = 50
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                pygame.draw.rect(screen, (0, 0, 0), (i * space + 450, j * space, space + 1, space + 1), width=3,)
            else:
                pygame.draw.rect(screen, (255, 255, 50), (i * space + 450, j * space, space + 1, space + 1), width=3,)
    #board_object.draw()


if __name__ == "__main__":
    #General pygame initialization
    screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    current_event:int

    #Main Game Loop
    while globals.running:
        mouse_pos = pygame.mouse.get_pos()
        

        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                exit()
            else:
                current_event = event.type

        if globals.in_menu:
            render_menu(screen, mouse_pos, current_event)

        else:
            render_game(screen, mouse_pos, current_event)

        
        
        pygame.display.flip()



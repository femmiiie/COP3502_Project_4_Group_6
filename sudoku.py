
#TODOS:
#add location and size parameters to cell (and board?) class
#   would make it easier to address sizes of specific cell when drawing
#create all buttons and both menus
#   i have rendering functions for both started, may have to be renamed since we will prob do input/game handling in it too


#IMPORTS
#double import for type casting
import pygame
from pygame import *
from sudoku_generator import SudokuGenerator, generate_sudoku


pygame.init()

#CONSTANTS
WINDOW_HEIGHT = 720
WINDOW_HEIGHT_CENTER = WINDOW_HEIGHT/2
WINDOW_LENGTH = 1280
WINDOW_LENGTH_CENTER = WINDOW_LENGTH/2
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DEFAULT_FONT = pygame.font.Font(None, 50)


#GLOBAL FLAGS
running = True
in_menu = True

def start_game(removed:int)->None:
    global in_menu
    in_menu = not in_menu
    global sudoku, board
    sudoku, board = generate_sudoku(9, 30)
    sudoku.print_board()

def end_game()->None:
    global in_menu
    in_menu = not in_menu
    global sudoku, board
    del sudoku, board


#Currently only accounts for text centering
#Will try to do button centering soon
def draw_button(screen:Surface, left_edge:int, top_edge:int, border:int, text:str, text_color:tuple, background_color:tuple)->Rect:
    text_object = DEFAULT_FONT.render(text, 0, text_color)
    sizes = (text_object.get_width() + border, text_object.get_height() + border)
    positions = (left_edge - (border//2), top_edge - (border//2))
    coords = pygame.Rect(positions[0], positions[1], sizes[0], sizes[1])

    pygame.draw.rect(screen, background_color, coords)
    screen.blit(text_object, (left_edge, top_edge))

    return coords
        
#True if area clicked, False otherwise
def check_if_pressed(mouse_pos:tuple[int, int], button_location:Rect)->bool:
    return True


#Renders all Main Menu Elements, Buttons, Etc.
def render_menu(screen:Surface, mouse_pos:tuple[int, int], current_event:int):
    screen.fill('blue')

    easy_location = draw_button(screen, WINDOW_LENGTH_CENTER - 200, 500, 10, 'EASY', WHITE, BLACK)
    medium_location = draw_button(screen, WINDOW_LENGTH_CENTER, 500, 10, 'MEDIUM', WHITE, BLACK)
    hard_location = draw_button(screen, WINDOW_LENGTH_CENTER + 200, 500, 10, 'HARD', WHITE, BLACK)
    exit_location = draw_button(screen, 10, 10, 10, "EXIT", WHITE, BLACK)

    if current_event == pygame.MOUSEBUTTONUP:
        if check_if_pressed(mouse_pos, easy_location):
            start_game(30)
        elif check_if_pressed(mouse_pos, medium_location):
            start_game(40)
        elif check_if_pressed(mouse_pos, hard_location):
            start_game(50)
        elif check_if_pressed(mouse_pos, exit_location):
            exit()
            
            

#Renders all Game Elements, Handles Game Logic, Etc.
def render_game(screen:Surface, mouse_pos:tuple[int, int], current_event:int):
    screen.fill('red')


if __name__ == "__main__":
    #General pygame initialization
    screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    current_event:int

    #Main Game Loop
    while running:
        mouse_pos = pygame.mouse.get_pos()
        

        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                running = False
            else:
                current_event = event.type

        if in_menu:
            render_menu(screen, mouse_pos, current_event)

        else:
            render_game(screen, mouse_pos, current_event)

        
        
        pygame.display.flip()



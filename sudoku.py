
#TODOS:
#add location and size parameters to cell (and board?) class
#   would make it easier to address sizes of specific cell when drawing
#create all buttons and both menus
#   i have rendering functions for both started, may have to be renamed since we will prob do input/game handling in it too


#IMPORTS
#double import for type casting
import pygame
from pygame import *
from sudoku_generator import generate_sudoku


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

def start_game(removed:int, screen:Surface)->None:
    global in_menu
    in_menu = not in_menu
    global sudoku, board
    board = generate_sudoku(9, 30, screen)

def end_game()->None:
    global in_menu
    in_menu = not in_menu
    global sudoku, board
    del sudoku, board


def draw_button(screen:Surface, x_pos:int, y_pos:int, border_size:int, text:str, text_color:tuple, background_color:tuple)->Rect:
    text_object = DEFAULT_FONT.render(text, 0, text_color)

    button_size = (text_object.get_width() + border_size, text_object.get_height() + border_size)
    text_position = (x_pos - (button_size[0]//2), y_pos - (button_size[1]//2))

    box_position = (text_position[0] - (border_size//2), text_position[1] - (border_size//2))
    coordinates = pygame.Rect(box_position[0], box_position[1], button_size[0], button_size[1])
    
    pygame.draw.rect(screen, background_color, coordinates)
    screen.blit(text_object, text_position)

    return coordinates
        
#True if area clicked, False otherwise
def check_if_pressed(mouse_pos:tuple[int, int], button:Rect)->bool:
    if button.left <= mouse_pos[0] <= button.right and button.top <= mouse_pos[1] <= button.bottom:
        return True
    else:
        return False


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
    sudoku.board_object.draw()


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
                exit()
            else:
                current_event = event.type

        if in_menu:
            render_menu(screen, mouse_pos, current_event)

        else:
            render_game(screen, mouse_pos, current_event)

        
        
        pygame.display.flip()



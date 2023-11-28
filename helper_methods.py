import pygame
from pygame import *
from sudoku_generator import generate_sudoku
from constants import *



def start_game(removed:int, screen:Surface)->None:
    global in_menu
    in_menu = not in_menu
    global board
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
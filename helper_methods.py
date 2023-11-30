import pygame
from pygame import *
from sudoku_generator import generate_sudoku
from constants import *
import globals
from math import floor




def start_game(removed:int, screen:Surface)->None:
    globals.in_menu = not globals.in_menu
    globals.board = generate_sudoku(9, removed)


def end_game()->None:
    globals.in_menu = not globals.in_menu
    globals.board = object


def draw_button(screen:Surface, x_pos:int, y_pos:int, border_size:int, text:str, text_color:tuple, background_color:tuple)->Rect:
    text_object = DEFAULT_FONT.render(text, text_color)[0]
    common_height = DEFAULT_FONT.get_rect("A").height

    button_size = (text_object.get_width() + border_size, common_height + border_size)
    text_position = (x_pos - (button_size[0]//2), y_pos - (button_size[1]//2))

    box_position = (text_position[0] - (border_size//2), text_position[1] - (border_size//2))
    coordinates = pygame.Rect(box_position[0], box_position[1], button_size[0], button_size[1])
    
    pygame.draw.rect(screen, background_color, coordinates, 0,  8)
    screen.blit(text_object, text_position)

    return coordinates


#True if area clicked, False otherwise
def check_if_pressed(mouse_pos:tuple[int, int], button:Rect)->bool:
    if button.left <= mouse_pos[0] <= button.right and button.top <= mouse_pos[1] <= button.bottom:
        return True
    else:
        return False
    

def check_menu(screen, mouse_pos:tuple[int, int], buttons:list[Rect])->None:
    if check_if_pressed(mouse_pos, buttons[0]):
        start_game(30, screen)
    elif check_if_pressed(mouse_pos, buttons[1]):
        start_game(40, screen)
    elif check_if_pressed(mouse_pos, buttons[2]):
        start_game(50, screen)
    elif check_if_pressed(mouse_pos, buttons[3]):
        exit()


def check_box_selection(mouse_pos:tuple[int, int], offsets:tuple[int, int], box_size:int):
    selection = (
        floor((mouse_pos[0] - offsets[0]) / box_size),
        floor((mouse_pos[1] - offsets[1]) / box_size)
    )
    if 0 <= selection[0] <= 8 and 0 <= selection[1] <= 8:
        globals.board.set_selected(selection[0], selection[1])
    else:
        globals.board.set_selected(9, 9)


def check_game(screen, mouse_pos:tuple[int, int], buttons:list[Rect])->None:
    if check_if_pressed(mouse_pos, buttons[0]):
        globals.board.reset_to_original()
        print('reset!')
    elif check_if_pressed(mouse_pos, buttons[1]):
        end_game()
    elif check_if_pressed(mouse_pos, buttons[2]):
        exit()


def try_move_selected(pressed, selected):
    if pressed[pygame.K_w] | pressed[pygame.K_UP]:
        globals.board.set_selected(selected[0], selected[1]-1)
    elif pressed[pygame.K_s] | pressed[pygame.K_DOWN]:
        globals.board.set_selected(selected[0], selected[1]+1)
    elif pressed[pygame.K_a] | pressed[pygame.K_LEFT]:
        globals.board.set_selected(selected[0]-1, selected[1])
    elif pressed[pygame.K_d] | pressed[pygame.K_RIGHT]:
        globals.board.set_selected(selected[0]+1, selected[1])

    selected = globals.board.get_selected()
    if selected[0] > 8:
        globals.board.set_selected(8, selected[1])
    elif selected[1] > 8:
        globals.board.set_selected(selected[0], 8)
    elif selected[0] < 0:
        globals.board.set_selected(0, selected[1])
    elif selected[1] < 0:
        globals.board.set_selected(selected[0], 0)

def try_update_cell(pressed, selected):
    sketched = globals.board.board[selected[0]][selected[1]].get_sketched_value()

    #if theres a faster way of doing this please do it
    #my brain is fried
    if pressed[pygame.K_0]:
        sketched = 0
    elif pressed[pygame.K_1]:
        sketched = 1
    elif pressed[pygame.K_2]:
        sketched = 2
    elif pressed[pygame.K_3]:
        sketched = 3
    elif pressed[pygame.K_4]:
        sketched = 4
    elif pressed[pygame.K_5]:
        sketched = 5
    elif pressed[pygame.K_6]:
        sketched = 6
    elif pressed[pygame.K_7]:
        sketched = 7
    elif pressed[pygame.K_8]:
        sketched = 8
    elif pressed[pygame.K_9]:
        sketched = 9

    globals.board.board[selected[0]][selected[1]].set_sketched_value(sketched)
    print(sketched)

    


def display_title_elements(screen:Surface):
    title_contents : list[Surface] = [
        TITLE_FONT.render("COP3502 PROJECT 4:", BLACK)[0],
        TITLE_FONT.render("SUDOKU", BLACK)[0]
        ]
    
    subtitle_contents : list[Surface] = [
        SUBTITLE_FONT.render("Sandro Mocevic", BLACK)[0],
        SUBTITLE_FONT.render("Aaron Gallego", BLACK)[0],
        SUBTITLE_FONT.render("Yash Patel", BLACK)[0]
        ]
    
    common_height = TITLE_FONT.get_rect("A").height
    for i, text in enumerate(title_contents):
        center_pos = (WINDOW_LENGTH_CENTER, (i*75) + common_height + 15)
        screen.blit(text, text.get_rect(center=center_pos))
    common_height = SUBTITLE_FONT.get_rect("A").height
    for i, text in enumerate(subtitle_contents):
        center_pos = (WINDOW_LENGTH_CENTER, (i*55) + common_height + 175)
        screen.blit(text, text.get_rect(center=center_pos))


def display_board_elements(screen:Surface, box_size:int, offsets:tuple[int, int]):
    #don't ask how i figured this out i have no idea
    #makes it so box lines are accented
    width_matrix = [0, 1, 2, 2, 3, 4, 4, 5, 6, 7]

    cell_font = pygame.freetype.SysFont("Calibri", box_size-10)
    sketch_font = pygame.freetype.SysFont("Calibri", box_size-20)
    selected = globals.board.get_selected()
    distances = (
        (selected[0]*box_size + offsets[0]) - width_matrix[selected[0]], 
        (selected[1]*box_size + offsets[1]) - width_matrix[selected[1]])
    
    if selected[0] < 9 and selected[1] < 9:
        box_coordinates = pygame.draw.rect(screen, HIGHLIGHTED_COLOR_1, (distances[0], distances[1], box_size + 1, box_size + 1), box_size)
    
    # sketches board and cells
    for i in range(9):
        for j in range(9):
            distances = (
                (i*box_size + offsets[0]) - width_matrix[i], 
                (j*box_size + offsets[1]) - width_matrix[j])
            box_coordinates = pygame.draw.rect(screen, BLACK, (distances[0], distances[1], box_size + 1, box_size + 1), 2)

            if globals.board.board[i][j].get_cell_value() != 0:
                cell_surf = cell_font.render(str(globals.board.board[i][j].get_cell_value()), BLACK)[0]
                cell_rect = cell_surf.get_rect(center=box_coordinates.center)
                screen.blit(cell_surf, cell_rect)
            elif globals.board.board[i][j].get_sketched_value() != 0:
                sketch_offset = (box_coordinates.centerx - (box_size//10), 
                                 box_coordinates.centery - (box_size//10))
                cell_surf = sketch_font.render(str(globals.board.board[i][j].get_sketched_value()), SKETCHED_CELL_COLOR)[0]
                cell_rect = cell_surf.get_rect(center=sketch_offset)
                screen.blit(cell_surf, cell_rect)

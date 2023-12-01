import pygame
from pygame import *
from sudoku_generator import generate_sudoku
from constants import *
import globals
from math import floor




def start_game(removed:int, screen:Surface)->None:
    globals.state = globals.possible_states[1]
    globals.board = generate_sudoku(9, removed)


def end_game()->None:
    globals.state = globals.possible_states[0]
    globals.board = object



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


def check_game(mouse_pos:tuple[int, int], buttons:list[Rect])->None:
    if check_if_pressed(mouse_pos, buttons[0]):
        globals.board.reset_to_original()
    elif check_if_pressed(mouse_pos, buttons[1]):
        end_game()
    elif check_if_pressed(mouse_pos, buttons[2]):
        exit()

def check_finish(mouse_pos:tuple[int, int], buttons:list[Rect]):
    if check_if_pressed(mouse_pos, buttons[0]):
        exit()
    elif check_if_pressed(mouse_pos, buttons[1]):
        globals.state = globals.possible_states[0]


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
    if globals.board.board[selected[0]][selected[1]].get_cell_value() != 0:
        return
    
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
    elif pressed[pygame.K_9] or pressed[pygame.K_KP_4]:
        sketched = 9

    globals.board.board[selected[0]][selected[1]].set_sketched_value(sketched)

    
def try_submit_sketch(pressed, selected):
    sketched = globals.board.board[selected[0]][selected[1]].get_sketched_value()
    if (pressed[pygame.K_RETURN] or pressed[pygame.K_KP_ENTER]) and (sketched != 0):
        globals.board.board[selected[0]][selected[1]].set_cell_value(sketched)
        globals.board.board[selected[0]][selected[1]].set_sketched_value(0)
        globals.board.board[selected[0]][selected[1]].set_entered(True)

        if globals.board.is_full():
            globals.state = globals.possible_states[3]

            if globals.board.check_board():
                globals.state = globals.possible_states[2]
    


def determine_color(row, col):
    if globals.board.board[row][col].get_entered():
        return NUM_COLOR
    else:
        return BLACK








#IMPORTS
#double import for type casting
import pygame
from pygame import *

import pygame.freetype

#type casting imports
from cell import Cell
from board import Board

from helper_methods import *
from constants import *
import globals

pygame.init()


#Renders all Main Menu Elements, Buttons, Etc.
def render_menu(screen:Surface, mouse_pos:tuple[int, int], current_event):
    screen.fill(BACKGROUND_COLOR)

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


    easy_location : Rect = draw_button(screen, WINDOW_LENGTH_CENTER - 200, 500, 30, '  Easy  ', WHITE, BUTTON_COLOR)
    medium_location : Rect = draw_button(screen, WINDOW_LENGTH_CENTER, 500, 30, 'Medium', WHITE, BUTTON_COLOR)
    hard_location : Rect = draw_button(screen, WINDOW_LENGTH_CENTER + 200, 500, 30, '  Hard  ', WHITE, BUTTON_COLOR)
    exit_location : Rect = draw_button(screen, WINDOW_LENGTH_CENTER, 600, 30, "  Exit  ", WHITE, BUTTON_COLOR)

    if current_event.type == pygame.MOUSEBUTTONUP:
        check_menu(screen, mouse_pos, [
            easy_location,
            medium_location,
            hard_location,
            exit_location
        ])
            

#Renders all Game Elements, Handles Game Logic, Etc.
def render_game(screen: Surface, mouse_pos: tuple[int, int], current_event):
    screen.fill(BACKGROUND_COLOR)
    box_size = 50
    offsets = (WINDOW_LENGTH_CENTER - 4.5*box_size - 125, WINDOW_HEIGHT_CENTER - 4.5*box_size)
    cell_font = pygame.freetype.SysFont("Calibri", box_size-10)

    #don't ask how i figured this out i have no idea
    #makes it so box lines are accented
    width_matrix = [0, 1, 2, 2, 3, 4, 4, 5, 6, 7]
    
    #renders background for selected element
    selected = globals.board.get_selected()
    distances = ((selected[0]*box_size + offsets[0]) - width_matrix[selected[0]], (selected[1]*box_size + offsets[1]) - width_matrix[selected[1]])
    if selected[0] < 9 and selected[1] < 9:
        box_coordinates = pygame.draw.rect(screen, HIGHLIGHTED_COLOR_1, (distances[0], distances[1], box_size + 1, box_size + 1), box_size)
    
    # sketches board and cells
    for i in range(9):
        for j in range(9):
            distances = ((i*box_size + offsets[0]) - width_matrix[i], (j*box_size + offsets[1]) - width_matrix[j])
            box_coordinates = pygame.draw.rect(screen, BLACK, (distances[0], distances[1], box_size + 1, box_size + 1), 2)

            if globals.board.board[i][j].get_cell_value() != 0:
                cell_surf = cell_font.render(str(globals.board.board[i][j].get_cell_value()), BLACK)[0]
                cell_rect = cell_surf.get_rect(center=box_coordinates.center)
                screen.blit(cell_surf, cell_rect)

            else:
                pass
    
    button_x_pos = offsets[0] + 13*box_size
    reset_location = draw_button(screen, button_x_pos, WINDOW_HEIGHT_CENTER-100, 30, " Reset ", WHITE, BUTTON_COLOR)
    restart_location = draw_button(screen, button_x_pos, WINDOW_HEIGHT_CENTER, 30, "Restart", WHITE, BUTTON_COLOR)
    exit_location = draw_button(screen, button_x_pos, WINDOW_HEIGHT_CENTER+100, 30, "   Exit   ", WHITE, BUTTON_COLOR)
    
    if current_event.type == pygame.MOUSEBUTTONUP:
        check_game(screen, mouse_pos, [
            reset_location,
            restart_location,
            exit_location
        ])
        check_box_selection(mouse_pos, offsets, box_size)



if __name__ == "__main__":
    #General pygame initialization
    screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT), pygame.NOFRAME)
    clock = pygame.time.Clock()
    current_event:pygame.event.Event

    #Main Game Loop
    while globals.running:
        mouse_pos = pygame.mouse.get_pos()
        
        current_event = pygame.event.poll()
        if current_event.type == pygame.QUIT:
            exit()
        #print(current_event)

        if globals.in_menu:
            render_menu(screen, mouse_pos, current_event)

        else:
            render_game(screen, mouse_pos, current_event)

        pygame.display.flip()



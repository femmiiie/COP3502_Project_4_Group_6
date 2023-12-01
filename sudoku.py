#IMPORTS
#double import for type casting
import pygame
from pygame import *
import pygame.freetype

#type casting imports
from cell import Cell
from board import Board

from helper_methods import *
from display_methods import *
from constants import *
import globals

pygame.init()



#Renders all Main Menu Elements, Buttons, Etc.
def render_menu(screen:Surface, mouse_pos:tuple[int, int], current_event):

    display_title_elements(screen)
    
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
    box_size = 50
    offsets = (
        WINDOW_LENGTH_CENTER - (4.5 * box_size) - 125, 
        WINDOW_HEIGHT_CENTER - (4.5 * box_size))
    
    display_board_elements(screen, box_size, offsets)
    
    button_x_pos = offsets[0] + 13*box_size
    reset_location = draw_button(screen, button_x_pos, WINDOW_HEIGHT_CENTER-100, 30, " Reset ", WHITE, BUTTON_COLOR)
    restart_location = draw_button(screen, button_x_pos, WINDOW_HEIGHT_CENTER, 30, "Restart", WHITE, BUTTON_COLOR)
    exit_location = draw_button(screen, button_x_pos, WINDOW_HEIGHT_CENTER+100, 30, "   Exit   ", WHITE, BUTTON_COLOR)

    num_offsets = (offsets[0] - 1.2*box_size, offsets[1] + 10*box_size)
    num_locations = [draw_button(screen, num_offsets[0] + i*1.3*box_size, num_offsets[1], 25, str(i), NUM_COLOR, NUM_BUTTON_COLOR) for i in range(10)]
    
    if current_event.type == pygame.MOUSEBUTTONUP:
        check_box_selection(mouse_pos, offsets, box_size)
        check_game(mouse_pos, [
            reset_location,
            restart_location,
            exit_location
        ])
    elif current_event.type == pygame.KEYDOWN:
        
        pressed = pygame.key.get_pressed()
        selected = globals.board.get_selected()

        if (0 <= selected[0] <= 8) and (0 <= selected[1] <= 8):
            try_move_selected(pressed, selected)
            try_update_cell(pressed, selected)
            try_submit_sketch(pressed, selected)
        

def render_win(screen: Surface, mouse_pos: tuple[int, int], current_event):
    common_height = TITLE_FONT.get_rect("A").height
    text = TITLE_FONT.render("WINNER!", BLACK)[0]
    center_pos = (WINDOW_LENGTH_CENTER, 90 + common_height)
    screen.blit(text, text.get_rect(center=center_pos))

    exit_location = draw_button(screen, WINDOW_LENGTH_CENTER-100, 500, 30, "Exit", WHITE, BUTTON_COLOR)
    play_location = draw_button(screen, WINDOW_LENGTH_CENTER+100, 500, 30, "Play Again", WHITE, BUTTON_COLOR)

    if current_event.type == pygame.MOUSEBUTTONUP:
        check_finish(mouse_pos, [
            exit_location,
            play_location
        ])

def render_loss(screen: Surface, mouse_pos: tuple[int, int], current_event):
    common_height = TITLE_FONT.get_rect("A").height
    text = TITLE_FONT.render("GAME OVER:(", BLACK)[0]
    center_pos = (WINDOW_LENGTH_CENTER, 90 + common_height)
    screen.blit(text, text.get_rect(center=center_pos))

    exit_location = draw_button(screen, WINDOW_LENGTH_CENTER-100, 500, 30, "Exit", WHITE, BUTTON_COLOR)
    play_location = draw_button(screen, WINDOW_LENGTH_CENTER+100, 500, 30, "Play Again", WHITE, BUTTON_COLOR)

    if current_event.type == pygame.MOUSEBUTTONUP:
        check_finish(mouse_pos, [
            exit_location,
            play_location
        ])



if __name__ == "__main__":
    #General pygame initialization
    screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT), pygame.NOFRAME)
    clock = pygame.time.Clock()
    current_event:pygame.event.Event

    #Main Game Loop
    while globals.running:
        screen.fill(BACKGROUND_COLOR)
        
        mouse_pos = pygame.mouse.get_pos()
        
        #Using Poll Instead of Get to Prevent 'Phantom Holding'
        current_event = pygame.event.poll()
        if current_event.type == pygame.QUIT:
            exit()

        match globals.state:
            case "menu":
                render_menu(screen, mouse_pos, current_event)
            case "game":
                render_game(screen, mouse_pos, current_event)
            case "win":
                render_win(screen, mouse_pos, current_event)
            case "loss":
                render_loss(screen, mouse_pos, current_event)
            

        pygame.display.flip()



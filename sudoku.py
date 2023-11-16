#IMPORTS
import pygame
from sudoku_generator import SudokuGenerator


#CONSTANTS
WINDOW_HEIGHT = 720
WINDOW_LENGTH = 1280
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


#GLOBAL FLAGS
running = True
in_menu = True


#Renders all Main Menu Elements, Buttons, Etc.
def render_menu(screen):
    screen.fill('blue')
    text = pygame.font.Font(None, 100)
    textObj = text.render("Testing 123", 0, (255,255,255))
    screen.blit(textObj, (WINDOW_LENGTH/2, WINDOW_HEIGHT/2))


#Renders all Game Elements, Handles Game Logic, Etc.
def render_game(screen):
    screen.fill('red')


if __name__ == "__main__":
    #General pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    

    #Main Game Loop
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                in_menu = not in_menu

        if in_menu:
            render_menu(screen)

        else:
            render_game(screen)

        
        
        pygame.display.flip()
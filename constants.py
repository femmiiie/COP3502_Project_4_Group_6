import pygame.freetype
pygame.freetype.init()

#CONSTANTS
WINDOW_HEIGHT = 720
WINDOW_HEIGHT_CENTER = WINDOW_HEIGHT/2
WINDOW_LENGTH = 1280
WINDOW_LENGTH_CENTER = WINDOW_LENGTH/2

BLACK = (52,72,97)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SKETCHED_CELL_COLOR = (100, 120, 140)
HIGHLIGHTED_COLOR_1 = (187,222,251)
BACKGROUND_COLOR = (240, 240, 240)
BUTTON_COLOR = (90, 123, 192)

DEFAULT_FONT = pygame.freetype.SysFont("Calibri", 50)
TITLE_FONT = pygame.freetype.Font('Arimo/static/Arimo-Bold.ttf', 75)
SUBTITLE_FONT = pygame.freetype.Font('Arimo/static/Arimo-Medium.ttf', 50)

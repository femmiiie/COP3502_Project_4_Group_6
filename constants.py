import pygame.freetype
pygame.freetype.init()
pygame.font.init()

#CONSTANTS
WINDOW_HEIGHT = 720
WINDOW_HEIGHT_CENTER = WINDOW_HEIGHT/2
WINDOW_LENGTH = 1280
WINDOW_LENGTH_CENTER = WINDOW_LENGTH/2
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (245, 245, 245)
BUTTON_COLOR = (90, 123, 192)
DEFAULT_FONT = pygame.freetype.SysFont("Calibri", 50)
TITLE_FONT = pygame.freetype.Font('Arimo/static/Arimo-Bold.ttf', 75)
SUBTITLE_FONT = pygame.freetype.Font('Arimo/static/Arimo-Medium.ttf', 50)

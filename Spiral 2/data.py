import instructor_provided as ip
import pygame
import pygame.freetype
import timer
pygame.freetype.init()

class Data:
    
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    GRID_DIM = 15
    WORLD = ip.initialize("1920_by_1080.csv")
    img_w = 16
    img_h = 9
    dims = width, height = SCREEN_WIDTH, SCREEN_HEIGHT 
    WIN = pygame.display.set_mode(dims)
    pygame.display.set_caption('CS110 Flight Simulator')
    icon = pygame.image.load("images/airplane.jpg")
    pygame.display.set_icon(icon)
    BACKGROUND = pygame.Surface(dims)
    GLOBAL_TIMER = timer.Timer()
    GLOBAL_TIMER.start()
    RUNNING = True
    font = pygame.freetype.SysFont("Comic Sans MS", 80)
    
import instructor_provided as ip
import pygame
import pygame.freetype
import timer
pygame.freetype.init()

class Data:
    """Intial Data for games, called in instance and passed around
    """    
    SCREEN_WIDTH = 1920 # Need to change to dynamic
    SCREEN_HEIGHT = 1080 # Need to change to dynnamic
    GRID_DIM = 15 # ???
    WORLD = ip.initialize("maps/1920_by_1080.csv") # Can select the map currently on my one, however if you choose a smaller map the program will break...
    img_w = 16 # Deprecated
    img_h = 9 # Deprecated
    dims = width, height = SCREEN_WIDTH, SCREEN_HEIGHT # PYGAME IS WERID
    WIN = pygame.display.set_mode(dims)
    COLS = pygame.Surface(dims)
    COLS.set_alpha(0) # Makes the surface invisible
    pygame.display.set_caption('CS110 Flight Simulator')
    icon = pygame.image.load("images/airplane.jpg")
    pygame.display.set_icon(icon)
    BACKGROUND = pygame.Surface(dims)
    GLOBAL_TIMER = timer.Timer()
    GLOBAL_TIMER.start()
    RUNNING = True
    font = pygame.freetype.SysFont("Comic Sans MS", 80)
    AI_SPEED = 1.5
    AI_MISSILE_COOLDOWN = 2
    JET_SPEED = 1.5
    JET_SPEED_2 = 1.5
    MISSILE_SPEED = 4.0
    MISSILE_COOLDOWN = 2.0

    
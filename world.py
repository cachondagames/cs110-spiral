from typing import Type
import data
import pygame
import sys

Data = data.Data() # Doing this because we dont ever call back to it. 

class World:
    """World Class
    """    
    
    def draw_tile(self, pic, x, y):
        """Draws a tile to the screen

        Args:
            pic (string): G,M,R,T,B,E,bg1. Type of picture to draw
            x (int): X Coord of top left of photo
            y (int): Y Coord of top left of photo
        """        
        path = None
        if pic == "G":
            path = "images/grass.png"
        elif pic == "M":
            path = "images/mountain.png"
        elif pic == "R":
            path = "images/road.png"
        elif pic == "T":
            path = "images/trees.png"
        elif pic == "B":
            path = "images/base.png"
        elif pic == "E":
            path = "images/explosion.png"
        elif pic == "bg1": # loads a premade map if it has already ran once
            Data.BACKGROUND.blit(pygame.image.load("images/background1.png"), (0,0))
            return
        temppic = pygame.image.load(path) # type: ignore 
        temppic = pygame.transform.scale(temppic, (Data.img_w, Data.img_h))
        Data.BACKGROUND.blit(temppic, (x * 16, y * 9))

    def draw_world(self):
        """Attempted to draw the world to the screen, will only ever draw the entire world once, if the world has already been draw it will load a presaved image instead to save time.
        """        
        try: # attemps to load the background
            pygame.image.load("images/background1.png")
        except FileNotFoundError: # will run if the background was never made
            y_temp = 0
            try:
                for row in Data.WORLD:
                    x_temp = 0
                    for item in row:
                        self.draw_tile(item, x_temp, y_temp)
                        x_temp += 1
                    y_temp += 1
                pygame.image.save(Data.BACKGROUND, "images/background1.png") # Saves the drawn background to WD for use again
            except TypeError:
                sys.exit()
        else:
            self.draw_tile("bg1", 0, 0)

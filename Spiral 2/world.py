from typing import Type
import data
import pygame

Data = data.Data()

class World:
    
    def draw_tile(self, pic, x, y):
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
        elif pic == "bg1":
            Data.BACKGROUND.blit(pygame.image.load("images/background1.png"), (0,0))
            return
        temppic = pygame.image.load(path)
        temppic = pygame.transform.scale(temppic, (Data.img_w, Data.img_h))
        Data.BACKGROUND.blit(temppic, (x * 16, y * 9))

    def draw_world(self):
        try:
            pygame.image.load("images/background1.png")
        except FileNotFoundError:
            y_temp = 0
            try:
                for row in Data.WORLD:
                    x_temp = 0
                    for item in row:
                        self.draw_tile(item, x_temp, y_temp)
                        x_temp += 1
                    y_temp += 1
                pygame.image.save(Data.BACKGROUND, "images/background1.png")
            except TypeError:
                print(x_temp, y_temp)
        else:
            self.draw_tile("bg1", 0, 0)

import pygame
import data
import timer
import world
import math

def dist_point(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class Missile():
    
    def __init__(self, xcoord, ycoord, angle, data):
        self.x = xcoord
        self.y = ycoord
        self.DATA = data
        self.angle = angle
        self.missile = pygame.image.load("images/missile_east.png")
        self.missile = pygame.transform.scale(self.missile, (60, 60))
        self.rect = self.missile.get_rect()
        self.xint = xcoord
        self.yint = ycoord
        self.timeexploded = None
        self.check = True
        
    def draw(self, win):
        img_copy = pygame.transform.rotate(self.missile, self.angle)
        rotated_rect = img_copy.get_rect()
        rotated_rect.size = (20,20)
        rotated_rect.x = self.x
        rotated_rect.y = self.y
        self.rect = rotated_rect
        pygame.draw.rect(win, (0,0,255), rotated_rect)
        win.blit(img_copy, rotated_rect)
        
    def move(self, speed):
        cx, cy = (speed * math.cos(self.angle/57.2957795)) + self.x, -(speed * math.sin(self.angle/57.2957795)) + self.y
        dx, dy = cx - self.x, cy - self.y
        if abs(dx) > 0 or abs(dy) > 0:
            dist = math.hypot(dx, dy)
            self.x += min(dist, speed) * dx/dist
            self.y += min(dist, speed) * dy/dist
            
    def moveChecker(self):
        if dist_point(self.xint, self.yint, self.x, self.y) >= 4 * 120:
            return True
        else:
            return False
    
    def explode(self):
        self.missile = pygame.image.load("images/explosion.png")
        self.missile = pygame.transform.scale(self.missile, (80, 80))
        self.check = False
        
    def timeChecker(self):
        if self.DATA.GLOBAL_TIMER.getTime() - self.timeexploded >= 3:
            return True
        else:
            return False
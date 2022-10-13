import pygame
import math

class Jet():
    def __init__(self, xcoord, ycoord, second, data):
        self.missiles = []
        self.second = second
        self.DATA = data
        self.x = xcoord
        self.y = ycoord
        self.missile_cooldown = True
        self.missile_cooldown_time_int = None
        self.missile_cooldown_time_final = None
        if second == True:
            self.plane = pygame.image.load("images/hostile_fighter_east.png")
            self.plane = pygame.transform.scale(self.plane, (50, 50))
        else:
            self.plane = pygame.image.load("images/friendly_fighter_east.png")
            self.plane = pygame.transform.scale(self.plane, (50, 50))
        self.rect = self.plane.get_rect()
        self.angle = 0
    
    def draw(self, win):
        img_copy = pygame.transform.rotate(self.plane, self.angle)
        rotated_rect = img_copy.get_rect(center = (round(self.x), round(self.y)))
        x1, y1 = rotate_point(self.x - 20, self.y + 10, self.angle/57.2957795, self.x, self.y)
        x2, y2 = rotate_point(self.x - 20, self.y - 10, self.angle/57.2957795, self.x, self.y)
        x3, y3 = rotate_point(self.x + 20, self.y, self.angle/57.2957795, self.x, self.y)
        self.rect = pygame.draw.polygon(win, (0,255,0), ( (x1,y1) , (x2,y2), (x3,y3) ) )
        win.blit(img_copy, rotated_rect)
        
    def move(self, speed):
        cx, cy = (speed * math.cos(self.angle/57.2957795)) + self.x, -(speed * math.sin(self.angle/57.2957795)) + self.y
        dx, dy = cx - self.x, cy - self.y
        if abs(dx) > 0 or abs(dy) > 0:
            dist = math.hypot(dx, dy)
            self.x += min(dist, speed) * dx/dist
            self.y += min(dist, speed) * dy/dist
            if self.x >= self.DATA.SCREEN_WIDTH:
                self.x = self.DATA.SCREEN_WIDTH
            if self.x <= 0:
                self.x = 0
            if self.y >= self.DATA.SCREEN_HEIGHT:
                self.y = self.DATA.SCREEN_HEIGHT
            if self.y <= 0:
                self.y = 0
    
    def missileCooldown(self):
        if self.DATA.GLOBAL_TIMER.getTime() - self.missile_cooldown_time_int >= 1:
            self.missile_cooldown = True
        else:
            self.missile_cooldown = False
    
def rotate_point(rx, ry, angle, px, py):
  s = math.sin(angle)
  c = math.cos(angle)
 
  rx -= px
  ry -= py
 
  xnew = rx * c - ry * s
  ynew = -(rx * s + ry * c)
 
  rx = xnew + px
  ry = ynew + py
  
  return rx,ry

        


        
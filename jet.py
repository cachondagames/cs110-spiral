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
        rotated_rect.size = (20,20)
        rotated_rect.center = (self.x + 30, self.y - 20)
        self.rect = rotated_rect
        pygame.draw.rect(win, (255,0,0), rotated_rect)
        pygame.draw.rect(win, (0,255,0), self.rect)
        win.blit(img_copy, rotated_rect)
        
    def move(self, speed):
        cx, cy = (speed * math.cos(self.angle/57.2957795)) + self.x, -(speed * math.sin(self.angle/57.2957795)) + self.y
        dx, dy = cx - self.x, cy - self.y
        if abs(dx) > 0 or abs(dy) > 0:
            dist = math.hypot(dx, dy)
            self.x += min(dist, speed) * dx/dist
            self.y += min(dist, speed) * dy/dist
            if self.x >= self.DATA.SCREEN_WIDTH - 325:
                self.x = self.DATA.SCREEN_WIDTH - 325
            elif self.x <= 0 + 325:
                self.x = 0 + 325
            elif self.y >= self.DATA.SCREEN_HEIGHT - 200:
                self.y = self.DATA.SCREEN_HEIGHT - 200
            elif self.y <= 0 + 200:
                self.y = 0 + 200
    
    def missileCooldown(self):
        if self.DATA.GLOBAL_TIMER.getTime() - self.missile_cooldown_time_int >= 1:
            self.missile_cooldown = True
        else:
            self.missile_cooldown = False
        


        
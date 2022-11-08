import pygame
import math
import missile
import data as d


class Jet(pygame.Surface):
    """Jet Object, Creates a brand new jet
    """    
    def __init__(self, xcoord: float, ycoord:float , second: bool, data, AI = False):
        """Initals values of Jet

        Args:
            xcoord (double): Intial X Coord
            ycoord (double): Inital Y Coord
            second (bool): Is second player or not
            data (data): Interal data structure
            AI (bool, optional): Is jet AI or not. Defaults to False.
        """        
        self.missiles:list[missile.Missile] = []
        self.second: bool = second
        self.DATA: d.Data = data
        self.x = xcoord
        self.y = ycoord
        self.missile_cooldown: bool = True
        self.missile_cooldown_time_int = None
        self.missile_cooldown_time_final = None
        if second == True:
            self.plane = pygame.image.load("images/hostile_fighter_east.png")
            self.plane = pygame.transform.scale(self.plane, (50, 50))
        else:
            self.plane = pygame.image.load("images/friendly_fighter_east.png")
            self.plane = pygame.transform.scale(self.plane, (50, 50))
        self.rect: pygame.rect.Rect = self.plane.get_rect()
        self.rect_heat: pygame.rect.Rect = self.plane.get_rect()
        self.angle: float = 0
        self.AI: bool = AI
    
    def draw(self, win: pygame.surface.Surface, col: pygame.Surface):
        """Draws the jet onto the screen

        Args:
            win (Surface): Window to draw jet to.
            col (Surface): Window in which to check for collisions
        """        
        img_copy = pygame.transform.rotate(self.plane, self.angle)
        rotated_rect = img_copy.get_rect(center = (round(self.x), round(self.y)))
        x1, y1 = rotate_point(self.x - 20, self.y + 10, self.angle/57.2957795, self.x, self.y)
        x2, y2 = rotate_point(self.x - 20, self.y - 10, self.angle/57.2957795, self.x, self.y)
        x3, y3 = rotate_point(self.x + 20, self.y, self.angle/57.2957795, self.x, self.y)
        
        xc, yc = rotate_point(self.x + 40, self.y, self.angle/57.2957795, self.x, self.y)
        xL_1, yL_1 = rotate_point(self.x + 40, self.y - 40, self.angle/57.2957795, self.x, self.y)
        xL_2, yL_2 = rotate_point(self.x + 200, self.y - 150, self.angle/57.2957795, self.x, self.y)
        xR_1, yR_1 = rotate_point(self.x + 40, self.y + 40, self.angle/57.2957795, self.x, self.y)
        xR_2, yR_2 = rotate_point(self.x + 200, self.y + 150, self.angle/57.2957795, self.x, self.y)
        xM, yM = rotate_point(self.x + 200, self.y, self.angle/57.2957795, self.x, self.y)        
        self.rect = pygame.draw.polygon(col, (0,255,0), ( (x1,y1) , (x2,y2), (x3,y3) ) )
        self.rect_heat = pygame.draw.polygon(col, (255,0,0), ( (xc,yc) , (xL_1,yL_1), (xL_2,yL_2), (xM, yM), (xR_2, yR_2), (xR_1,yR_1) ) )
        win.blit(img_copy, rotated_rect)
        
    def move(self, speed: float):
        """Moves the jet

        Args:
            speed (double): Speed in which to move the jet at.
        """        
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
        """Function to check if the jet has shot a missile within its cooldown period
        
        Returns:
            Boolean : Does not return, sets Jet interal value to either T/F
        """        
        if self.AI == False:
            if self.DATA.GLOBAL_TIMER.getTime() - self.missile_cooldown_time_int >= self.DATA.MISSILE_COOLDOWN:
                self.missile_cooldown = True
            else:
                self.missile_cooldown = False
        else:
            if self.DATA.GLOBAL_TIMER.getTime() - self.missile_cooldown_time_int >= self.DATA.AI_MISSILE_COOLDOWN:
                self.missile_cooldown = True
            else:
                self.missile_cooldown = False
    
    def checkheatseek(self, Jet: "Jet") -> bool:
        if (self.rect_heat.contains(Jet.rect)):
            return True
        return False

    
def rotate_point(rx: float, ry: float, angle: float, px: float, py: float) -> tuple[float, float]:
    """Roatate any point x angle

    Args:
        rx (double): Point X to rotate
        ry (double): Point Y to rotate
        angle (double): Angle to rotate by(in radians)
        px (double): Point X of rotation
        py (double): Point Y of rotation

    Returns:
        tuple : Returns a tuple with float of the new point x , y
    """
    s = math.sin(angle)
    c = math.cos(angle)

    rx -= px
    ry -= py

    xnew = rx * c - ry * s
    ynew = -(rx * s + ry * c)

    rx = xnew + px
    ry = ynew + py

    return rx,ry

        


        
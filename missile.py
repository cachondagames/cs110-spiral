import pygame
import data
import timer
import world
import math

def dist_point(x1, y1, x2, y2):
    """Regular point distance formula

    Args:
        x1 (double): X1
        y1 (double): Y1
        x2 (double): X2
        y2 (double): Y2

    Returns:
        double: Distance between two points
    """    
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class Missile():
    """My own missile class
    """    
    def __init__(self, xcoord, ycoord, angle, data):
        """Missile start

        Args:
            xcoord (double): Starting X Coord
            ycoord (double): Starting Y Coord
            angle (double): Angle at which it is traveling
            data (Data): Data Set
        """        
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
        
    def draw(self, win, col):
        """Draws the missile onto the screen

        Args:
            win (Surface): Window to draw jet to.
            col (Surface): Window in which to check for collisions
        """        
        img_copy = pygame.transform.rotate(self.missile, self.angle)
        rotated_rect = img_copy.get_rect(center = (round(self.x), round(self.y)))
        x1, y1 = rotate_point(self.x - 20, self.y + 10, self.angle/57.2957795, self.x, self.y)
        x2, y2 = rotate_point(self.x - 20, self.y - 10, self.angle/57.2957795, self.x, self.y)
        x3, y3 = rotate_point(self.x + 20, self.y, self.angle/57.2957795, self.x, self.y)
        self.rect = pygame.draw.polygon(col, (0,255,0), ( (x1,y1) , (x2,y2), (x3,y3) ) )
        win.blit(img_copy, rotated_rect)
        
    def move(self, speed):
        """Moves the missile

        Args:
            speed (double): Moves the missile by this speed
        """        
        cx, cy = (speed * math.cos(self.angle/57.2957795)) + self.x, -(speed * math.sin(self.angle/57.2957795)) + self.y
        dx, dy = cx - self.x, cy - self.y
        if abs(dx) > 0 or abs(dy) > 0:
            dist = math.hypot(dx, dy)
            self.x += min(dist, speed) * dx/dist
            self.y += min(dist, speed) * dy/dist
            
    def moveChecker(self):
        """Checks if the missile has moved far enough to be considered exploded

        Returns:
            bool: Returns True if it moved far enough, Returns False if it still can move
        """        
        if dist_point(self.xint, self.yint, self.x, self.y) >= 4 * 120:
            return True
        else:
            return False
    
    def explode(self):
        """Exlodes the missile
        """        
        self.missile = pygame.image.load("images/explosion.png")
        self.missile = pygame.transform.scale(self.missile, (80, 80))
        self.check = False
        
    def timeChecker(self):
        """Check if the missile has been exploded long enough to delete it

        Returns:
            bool: True if has been exploded longer than 3 seconds other returns false
        """        
        if self.DATA.GLOBAL_TIMER.getTime() - self.timeexploded >= 3:
            return True
        else:
            return False
    
    def heatseeker(self):
        pass
   
def rotate_point(rx, ry, angle, px, py):
    """Roatate any point x angle

    Args:
        rx (double): Point X to rotate
        ry (double): Point Y to rotate
        angle (double): Angle to rotate by(in radians)
        px (double): Point X of rotation
        py (double): Point Y of rotation

    Returns:
        tuple : Returns a tuple with double of the new point x , y
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
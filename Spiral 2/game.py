import world
import data
import pygame
import jet
import listener
import random
import sys
import PySimpleGUI as sg

WORLD = world.World()
Jets = []
pygame.init()
pygame.freetype.init()

class Game(object):
    
    def __init__(self):
        self.DATA = data.Data()
        WORLD.draw_world()
        self.DATA.RUNNING = True

    def start(self):
        sg.ChangeLookAndFeel('Dark')
        
        layout = [[sg.Text('             Please select the option you would like to play!')],      
                 [sg.B("2 Player", size = (25,1)), sg.B("1 Player", size = (25, 1))]]      

        window = sg.Window('CS110 Flight Simulator', layout)    
        event, values = window.read()    
        window.close()
        if event == "2 Player":
            gameType = "2 Player"
        else:
            gameType = "1 Player"
        self.gameStart(gameType)
  
    def gameStart(self, gameType):
        global Jets       
        if gameType == "2 Player":
            self.jets()
            while self.DATA.RUNNING:
                self.DATA.WIN.blit(self.DATA.BACKGROUND, (0,0))
                listener.Listeners.listen_keyboard(Jets[0], Jets[1])
                pygame.display.flip()
            Jets.clear()
            Game().start()
        else:
            sys.exit()
            
    def jets(self):
        global Jets
        Jet1 = jet.Jet(random.randint(self.DATA.SCREEN_WIDTH/4 , self.DATA.SCREEN_WIDTH * (3/4)), random.randint(self.DATA.SCREEN_HEIGHT/4 , self.DATA.SCREEN_HEIGHT * (3/4)), False, self.DATA)
        Jet2 = jet.Jet(random.randint(self.DATA.SCREEN_WIDTH/4 , self.DATA.SCREEN_WIDTH * (3/4)), random.randint(self.DATA.SCREEN_HEIGHT/4 , self.DATA.SCREEN_HEIGHT * (3/4)), True, self.DATA)
        Jets.append(Jet1)
        Jets.append(Jet2)

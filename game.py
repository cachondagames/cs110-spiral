import world
import data
import pygame
import jet
import listener
import random
import sys
import PySimpleGUI as sg
import ai_listener

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
                 [sg.B("2 Player", size = (25,1)), sg.B("1 Player", size = (25, 1)),sg.B("Options", size = (25,1))]]      

        window = sg.Window('CS110 Flight Simulator', layout)    
        event, values = window.read()    
        window.close()
        if event == "2 Player":
            gameType = "2 Player"
        elif event == "1 Player":
            gameType = "1 Player"
        elif event == "Options":
            layout = [[sg.Text('             Please select the option you would like to change')],      
                 [sg.B("AI Speed", size = (25,1)), sg.B("AI Missiles", size = (25, 1)),sg.B("Back to Main Menu", size = (25,1))]]
            options = sg.Window("CS110 Flight Simulator", layout)
            event, values = options.read()
            options.close()
            if event == "AI Speed":
                choice, _ = sg.Window('Continue?', [[sg.T('Do you want to continue?')], [sg.Yes(s=10), sg.No(s=10)]], disable_close=True).read(close=True)
                pass
            elif event == "AI Missiles":
                pass
            elif event == "Back to Main Menu":
                self.start()
            else:
                sys.exit()
        else:
            sys.exit()
        self.gameStart(gameType)
  
    def gameStart(self, gameType):
        global Jets       
        if gameType == "2 Player":
            self.jets()
            while self.DATA.RUNNING:
                self.DATA.WIN.blit(self.DATA.BACKGROUND, (0,0))
                listener.listen_keyboard(Jets[0], Jets[1])
                pygame.display.flip()
            Jets.clear()
            Game().start()
        elif gameType == "1 Player":
            self.jets()
            while self.DATA.RUNNING:
                self.DATA.WIN.blit(self.DATA.BACKGROUND, (0,0))
                ai_listener.listen_keyboard(Jets[0], Jets[1])
                pygame.display.flip()
            Jets.clear()
            Game().start()
        else:
            sys.exit()
            
    def jets(self):
        global Jets
        Jet1 = jet.Jet(random.randint(int(self.DATA.SCREEN_WIDTH/4) , int(self.DATA.SCREEN_WIDTH * (3/4))), random.randint(int(self.DATA.SCREEN_HEIGHT/4) , int(self.DATA.SCREEN_HEIGHT * (3/4))), False, self.DATA)
        Jet2 = jet.Jet(random.randint(int(self.DATA.SCREEN_WIDTH/4) , int(self.DATA.SCREEN_WIDTH * (3/4))), random.randint(int(self.DATA.SCREEN_HEIGHT/4) , int(self.DATA.SCREEN_HEIGHT * (3/4))), True, self.DATA)
        Jets.append(Jet1)
        Jets.append(Jet2)

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
    """Creates a Game object
    """    
    def __init__(self):
        """Starts the game, draws the world to the screen, and intializes the local data set
        """        
        self.DATA = data.Data()
        WORLD.draw_world()
        self.DATA.RUNNING = True

    def start(self):
        """Allows player to select 1/2 player and change options before starting. Recursive.
        """        
        sg.ChangeLookAndFeel('Dark')
        
        layout = [[sg.Text('             Please select the option you would like to play!')],      
                 [sg.B("2 Player", size = (25,1)), sg.B("1 Player", size = (25, 1)),sg.B("Options", size = (25,1))]]      

        window = sg.Window('CS110 Flight Simulator', layout)    
        event, values = window.read()      # type: ignore
        window.close()
        if event == "2 Player":
            gameType = "2 Player"
        elif event == "1 Player":
            gameType = "1 Player"
        elif event == "Options":
            layout = [[sg.Text('             Please select the option you would like to change')],      
                 [sg.B("AI Speed", size = (25,1)), sg.B("AI Missile Cooldown", size = (25, 1)), sg.B("Missile Speed", size = (25,1)), sg.B("Jet Speed", size = (25,1)) ,sg.B("Back to Main Menu", size = (25,1))]]
            options = sg.Window("CS110 Flight Simulator", layout)
            event, values = options.read()  # type: ignore
            options.close()
            if event == "AI Speed":
                choice = sg.Window('AI Speed', layout = [[sg.Text('                    AI Speed Slider', key='-OUTPUT-')],
                                                            [sg.T('0',size=(4,1), key='-LEFT-'),
                                                            sg.Slider((0,20), key='-SLIDER-', orientation='h', enable_events=True, disable_number_display=False, default_value = self.DATA.AI_SPEED, resolution=.1),
                                                            sg.T('MAX', size=(4,1), key='-RIGHT-')],
                                                            [sg.Button('Exit')]])
                while True:             # Event Loop
                    event, values = choice.read() # type: ignore
                    if event == sg.WIN_CLOSED or event == 'Exit':
                        break
                self.DATA.AI_SPEED = values["-SLIDER-"]
                choice.close()
                self.start()
                print(values["-SLIDER-"])
            elif event == "AI Missile Cooldown":
                choice = sg.Window('AI Missiles', layout = [[sg.Text('                    AI Missiles Slider', key='-OUTPUT-')],
                                                            [sg.T('0',size=(4,1), key='-LEFT-'),
                                                            sg.Slider((0,3), key='-SLIDER-', orientation='h', enable_events=True, disable_number_display=False, default_value = self.DATA.AI_MISSILE_COOLDOWN, resolution=.1),
                                                            sg.T('MAX', size=(4,1), key='-RIGHT-')],
                                                            [sg.Button('Exit')]])
                while True:             # Event Loop
                    event, values = choice.read() # type: ignore
                    if event == sg.WIN_CLOSED or event == 'Exit':
                        break
                self.DATA.AI_MISSILE_COOLDOWN = values["-SLIDER-"]
                choice.close()
                self.start()
            elif event == "Missile Speed":
                choice = sg.Window('MS', layout = [[sg.Text('                    Missile Speed Slider', key='-OUTPUT-')],
                                                            [sg.T('0',size=(4,1), key='-LEFT-'),
                                                            sg.Slider((0,3), key='-SLIDER-', orientation='h', enable_events=True, disable_number_display=False, default_value = self.DATA.MISSILE_SPEED, resolution=.1),
                                                            sg.T('MAX', size=(4,1), key='-RIGHT-')],
                                                            [sg.Button('Exit')]])
                while True:             # Event Loop
                    event, values = choice.read() # type: ignore
                    if event == sg.WIN_CLOSED or event == 'Exit':
                        break
                self.DATA.MISSILE_SPEED = values["-SLIDER-"]
                choice.close()
                self.start()
            elif event == "Jet Speed":
                choice = sg.Window('Jet Speed', layout = [[sg.Text('                    Jet Speed Slider', key='-OUTPUT-')],
                                                            [sg.T('0',size=(4,1), key='-LEFT-'),
                                                            sg.Slider((0,3), key='-SLIDER-', orientation='h', enable_events=True, disable_number_display=False, default_value = self.DATA.JET_SPEED, resolution=.1),
                                                            sg.T('MAX', size=(4,1), key='-RIGHT-')],
                                                            [sg.Button('Exit')]])
                while True:             # Event Loop
                    event, values = choice.read() # type: ignore
                    if event == sg.WIN_CLOSED or event == 'Exit':
                        break
                self.DATA.JET_SPEED = values["-SLIDER-"]
                choice.close()
                self.start()
            elif event == "Back to Main Menu":
                self.start()
            else:
                sys.exit()
        else:
            sys.exit()
        self.gameStart(gameType) # type: ignore
  
    def gameStart(self, gameType):
        """Actually begins the gameplay based on the type of game selected

        Args:
            gameType (string): 1/2 Player
        """        
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
            self.jets(True)
            while self.DATA.RUNNING:
                self.DATA.WIN.blit(self.DATA.BACKGROUND, (0,0))
                ai_listener.listen_keyboard(Jets[0], Jets[1])
                pygame.display.flip()
            Jets.clear()
            Game().start()
        else:
            sys.exit()
            
    def jets(self, Ai = False):
        """Creates the Jets for use by the game

        Args:
            Ai (bool, optional): If the game has an Ai jet present or not. Defaults to False.
        """        
        global Jets
        Jet1 = jet.Jet(random.randint(int(self.DATA.SCREEN_WIDTH/4) , int(self.DATA.SCREEN_WIDTH * (3/4))), random.randint(int(self.DATA.SCREEN_HEIGHT/4) , int(self.DATA.SCREEN_HEIGHT * (3/4))), False, self.DATA)
        if Ai == True:
            Jet2 = jet.Jet(random.randint(int(self.DATA.SCREEN_WIDTH/4) , int(self.DATA.SCREEN_WIDTH * (3/4))), random.randint(int(self.DATA.SCREEN_HEIGHT/4) , int(self.DATA.SCREEN_HEIGHT * (3/4))), True, self.DATA, True)
        else:
            Jet2 = jet.Jet(random.randint(int(self.DATA.SCREEN_WIDTH/4) , int(self.DATA.SCREEN_WIDTH * (3/4))), random.randint(int(self.DATA.SCREEN_HEIGHT/4) , int(self.DATA.SCREEN_HEIGHT * (3/4))), True, self.DATA)
        Jets.append(Jet1)
        Jets.append(Jet2)

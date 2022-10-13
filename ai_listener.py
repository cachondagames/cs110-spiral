import pygame
import sys
import missile
import math

def listen_keyboard(Jet1, JetAi):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        if Jet1.angle == 360:
            Jet1.angle = 1
        else: 
            Jet1.angle += 1
    if key[pygame.K_RIGHT]:
        if Jet1.angle == 0:
            Jet1.angle = 359
        else:
            Jet1.angle -= 1
    Jet1.move(1)
    Jet1.draw(Jet1.DATA.WIN, Jet1.DATA.COLS)
    ai_move(Jet1, JetAi)
    JetAi.draw(JetAi.DATA.WIN, JetAi.DATA.COLS)

def ai_move(Jet1, JetAi):
    target_angle = Jet1.angle
    move_angle = math.fabs(target_angle - JetAi.angle)
    if move_angle <= 180:
        if JetAi.angle == 0:
            JetAi.angle = 359
        else:
            JetAi.angle -= 1
    else:
        if JetAi.angle == 360:
            JetAi.angle = 1
        else:
            JetAi.angle += 1

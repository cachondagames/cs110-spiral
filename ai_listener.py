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
    JetAi.move(1)
    JetAi.draw(JetAi.DATA.WIN, JetAi.DATA.COLS)

def ai_move(Jet1, JetAi):
    target_coord = translate(list(Jet1.rect.center))
    current_coord = translate(list(JetAi.rect.center))
    x_dist = target_coord[0] - current_coord[0]
    y_dist = target_coord[1] - current_coord[1]
    try:
        theta = math.atan(y_dist/x_dist) * 57.2957795
        cx, cy = (1 * math.cos(JetAi.angle/57.2957795)) + JetAi.x, -(1 * math.sin(JetAi.angle/57.2957795)) + JetAi.y
        alpha = math.atan(cy / cx) * 57.2957795
    except ZeroDivisionError:
        theta = 90
        alpha = 90
    move_angle = 180 - (theta + alpha)
    text = Jet1.DATA.font.render(str(move_angle) + "  " + str(JetAi.angle) , (0,0,0))
    text_rect = text[0].get_rect(center=(Jet1.DATA.SCREEN_WIDTH/2, Jet1.DATA.SCREEN_HEIGHT/2))
    Jet1.DATA.WIN.blit(text[0], text_rect)
    if JetAi.angle != Jet1.angle:
        JetAi.angle - move_angle
        JetAi.angle + move_angle
        if move_angle < 180:
            if JetAi.angle == 360:
                JetAi.angle = 1
                JetAi.angle += 1
            else: 
                JetAi.angle += 1
        else:
            if JetAi.angle == 0:
                JetAi.angle = 359
                JetAi.angle -= 1
            else:
                JetAi.angle -= 1

def translate(coords):
    if coords[0] >= 960:
        coords[0] =  coords[0] - 960
    else:
        coords[0] = -960 + coords[0]
    if coords[1] >= 540:
        coords[1] = coords[1] - 540
    else:
        coords[1] = -540 + coords[1]
    return coords

def untranslate(coords):
    if coords[0] >= 960:
        coords[0] =  coords[0] + 960
    else:
        coords[0] = -960 - coords[0]
    if coords[1] >= 540:
        coords[1] = coords[1] + 540
    else:
        coords[1] = -540 - coords[1]
    return coords 


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
    angle = JetAi.vect.angle_to(Jet1.vect)
    text = Jet1.DATA.font.render(str(angle) , (0,0,0))
    text_rect = text[0].get_rect(center=(Jet1.DATA.SCREEN_WIDTH/2, Jet1.DATA.SCREEN_HEIGHT/2))
    Jet1.DATA.WIN.blit(text[0], text_rect)
    if JetAi.angle + angle > 360:
        temp = (JetAi.angle + angle) - 360
        JetAi.angle = temp
    elif JetAi.angle - angle < 0:
        temp = (JetAi.angle - angle)
        JetAi.angle = 360 - math.fabs(temp)
    else:
        JetAi.angle += angle
    # target_point_x, target_point_y = Jet1.rect.center
    # current_point_x, current_point_y = JetAi.rect.center
    # dist_x = math.fabs(target_point_x - current_point_x)
    # dist_y = math.fabs(target_point_y - current_point_y)
    # try:
    #     target_angle = math.atan(dist_y / dist_x) * 57.2957795
    # except ZeroDivisionError:
    #     target_angle = 90
    # move_angle = JetAi.angle - (target_angle)
    # JetAi.angle = move_angle
    # print(target_angle)
    # print(move_angle)
    # print(JetAi.angle)
    # if move_angle < 180 and move_angle > -180:
    #     if JetAi.angle == 0:
    #         JetAi.angle = 359
    #     else:
    #         JetAi.angle -= 1
    # else:
    #     if JetAi.angle == 360:
    #         JetAi.angle = 1
    #     else: 
    #         JetAi.angle += 1

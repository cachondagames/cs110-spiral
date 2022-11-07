import pygame
import sys
import missile
import math
import time
import jet

def listen_keyboard(Jet1: jet.Jet, JetAi: jet.Jet):
    """Function that checks for keyboard inputs and handles missile update tracking

    Args:
        Jet1 (Jet): Player 1 Jet
        JetAi (Jet, optional): AI Jet
    """    
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
    if key[pygame.K_UP]:
        if Jet1.DATA.JET_SPEED + .02 >= 7:
            Jet1.DATA.JET_SPEED = 7
        else:
            Jet1.DATA.JET_SPEED += .02
    if key[pygame.K_DOWN]:
        if Jet1.DATA.JET_SPEED - .02 <= .1:
            Jet1.DATA.JET_SPEED = .1
        else:
            Jet1.DATA.JET_SPEED -= .02
    Jet1.move(Jet1.DATA.JET_SPEED)
    Jet1.draw(Jet1.DATA.WIN, Jet1.DATA.COLS)
    ai_move(Jet1, JetAi)
    JetAi.move(JetAi.DATA.AI_SPEED)
    JetAi.draw(JetAi.DATA.WIN, JetAi.DATA.COLS)
    if key[pygame.K_SPACE]:
        if Jet1.missile_cooldown == True:
            Jet1.missiles.append(missile.Missile(Jet1.x, Jet1.y, Jet1.angle, Jet1.DATA, Jet1.checkheatseek(JetAi)))
            Jet1.missile_cooldown_time_int = Jet1.DATA.GLOBAL_TIMER.getTime()
            Jet1.missileCooldown()
        else:
            Jet1.missileCooldown()

    if len(Jet1.missiles) > 0:
        for mis in Jet1.missiles:
            if mis.moveChecker() and mis.check == True:
                mis.explode()
                mis.move(0)
                mis.angle = 0
                mis.draw(mis.DATA.WIN, Jet1.DATA.COLS)
                mis.timeexploded = Jet1.DATA.GLOBAL_TIMER.getTime()
                check = False
                continue
            if mis.check == False and mis.timeChecker():
                Jet1.missiles.pop(Jet1.missiles.index(mis))
                continue
            if mis.check:
                if mis.heatseek:
                    mis.heatseeker(JetAi)
                mis.move(Jet1.DATA.MISSILE_SPEED)
                mis.draw(Jet1.DATA.WIN, Jet1.DATA.COLS)
                if mis.rect.collidepoint((JetAi.rect.centerx,JetAi.rect.centery)):
                    mis.DATA.RUNNING = False  # type: ignore
                    text = mis.DATA.font.render("Player 1 Wins!" , (0,0,0))
                    text_rect = text[0].get_rect(center=(mis.DATA.SCREEN_WIDTH/2, mis.DATA.SCREEN_HEIGHT/2))
                    mis.DATA.WIN.blit(text[0], text_rect)
                    pygame.display.flip()
                    time.sleep(5)
            else:
                mis.move(0)
                mis.draw(mis.DATA.WIN, Jet1.DATA.COLS)
    if len(JetAi.missiles) > 0:
        for mis in JetAi.missiles:
            if mis.moveChecker() and mis.check == True:
                mis.explode()
                mis.move(0)
                mis.angle = 0
                mis.draw(mis.DATA.WIN, JetAi.DATA.COLS)
                mis.timeexploded = JetAi.DATA.GLOBAL_TIMER.getTime()
                check = False
                continue
            if mis.check == False and mis.timeChecker():
                JetAi.missiles.pop(JetAi.missiles.index(mis))
                continue
            if mis.check:
                if mis.heatseek:
                    mis.heatseeker(Jet1)
                mis.move(JetAi.DATA.MISSILE_SPEED)
                mis.draw(JetAi.DATA.WIN, JetAi.DATA.COLS)
                if mis.rect.collidepoint((Jet1.rect.centerx,Jet1.rect.centery)):
                    mis.DATA.RUNNING = False  # type: ignore
                    text = mis.DATA.font.render("Computer Wins!" , (0,0,0))
                    text_rect = text[0].get_rect(center=(mis.DATA.SCREEN_WIDTH/2, mis.DATA.SCREEN_HEIGHT/2))
                    mis.DATA.WIN.blit(text[0], text_rect)
                    pygame.display.flip()
                    time.sleep(5)
            else:
                mis.move(0)
                mis.draw(mis.DATA.WIN, JetAi.DATA.COLS)

def ai_move(Jet1: jet.Jet, JetAi: jet.Jet):
    """Currently handles the next AI movement, still need to reimplement NN (Weights)

    Args:
        Jet1 (Jet): Player 1 Jet
        JetAi (Jet)): AI Jet
    """    
    px, py = JetAi.rect.center
    x,y, = Jet1.rect.center
    dx, dy = x - px, y - py
    if math.hypot(dx,dy) < (360):
            if JetAi.missile_cooldown == True:
                JetAi.missiles.append(missile.Missile(JetAi.x, JetAi.y, JetAi.angle, JetAi.DATA, JetAi.checkheatseek(Jet1)))
                JetAi.missile_cooldown_time_int = JetAi.DATA.GLOBAL_TIMER.getTime()
                JetAi.missileCooldown()
            else:
                JetAi.missileCooldown()
    try: # Needed because of reverse Y coord, only computes values between -Pi, Pi thus when ontop of eachother vertically will result in a division by 0
        angle = -math.atan(dy/dx) * 57.2957795
    except ZeroDivisionError:
        if dy >= 0:
            angle = 270
        else:
            angle = 90
    if dx < 0:
        angle += 180
    JetAi.angle = angle
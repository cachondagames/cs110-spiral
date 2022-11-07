import pygame
import sys
import missile
import time
import jet

def listen_keyboard(Jet1: jet.Jet, Jet2: jet.Jet):
    """Function that checks for keyboard inputs and handles missile update tracking

    Args:
        Jet1 (Jet): Player 1 Jet
        Jet2 (Jet, optional): Player 2/AI Jet. Defaults to None.
    """    
    if Jet2 == None: ## Deprecated but too scared to delete
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
    else:
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
        if key[pygame.K_a]:
            if Jet2.angle == 360:
                Jet2.angle = 1
            else: 
                Jet2.angle += 1
        if key[pygame.K_d]:
            if Jet2.angle == 0:
                Jet2.angle = 359
            else:
                Jet2.angle -= 1
        if key[pygame.K_w]:
            if Jet2.DATA.JET_SPEED_2 + .02 >= 7:
                Jet2.DATA.JET_SPEED_2 = 7
            else:
                Jet2.DATA.JET_SPEED_2 += .02
        if key[pygame.K_s]:
            if Jet2.DATA.JET_SPEED_2 - .02 <= .1:
                Jet2.DATA.JET_SPEED_2 = .1
            else:
                Jet2.DATA.JET_SPEED_2 -= .02
        if key[pygame.K_SPACE]:
            if Jet1.missile_cooldown == True:
                
                Jet1.missiles.append(missile.Missile(Jet1.x, Jet1.y, Jet1.angle, Jet1.DATA, Jet1.checkheatseek(Jet2)))
                Jet1.missile_cooldown_time_int = Jet1.DATA.GLOBAL_TIMER.getTime()
                Jet1.missileCooldown()
            else:
                Jet1.missileCooldown()
        if key[pygame.K_LSHIFT]:
            if Jet2.missile_cooldown == True:
                Jet2.missiles.append(missile.Missile(Jet2.x, Jet2.y, Jet2.angle, Jet2.DATA, Jet2.checkheatseek(Jet1)))
                Jet2.missile_cooldown_time_int = Jet2.DATA.GLOBAL_TIMER.getTime()
                Jet2.missileCooldown()
            else:
                Jet2.missileCooldown()
        Jet1.move(Jet1.DATA.JET_SPEED)
        Jet1.draw(Jet1.DATA.WIN, Jet1.DATA.COLS)
        Jet2.move(Jet2.DATA.JET_SPEED_2)
        Jet2.draw(Jet2.DATA.WIN, Jet2.DATA.COLS)
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
                        mis.heatseeker(Jet2)
                    mis.move(mis.DATA.MISSILE_SPEED)
                    mis.draw(Jet1.DATA.WIN, Jet1.DATA.COLS)
                    if mis.rect.collidepoint((Jet2.rect.centerx,Jet2.rect.centery)):
                        mis.DATA.RUNNING = False  # type: ignore
                        text = mis.DATA.font.render("Player 1 Wins!" , (0,0,0))
                        text_rect = text[0].get_rect(center=(mis.DATA.SCREEN_WIDTH/2, mis.DATA.SCREEN_HEIGHT/2))
                        mis.DATA.WIN.blit(text[0], text_rect)
                        pygame.display.flip()
                        time.sleep(5)
                else:
                    mis.move(0)
                    mis.draw(mis.DATA.WIN, Jet1.DATA.COLS)
        if len(Jet2.missiles) > 0:
            for mis in Jet2.missiles:
                if mis.moveChecker() and mis.check == True:
                    mis.explode()
                    mis.move(0)
                    mis.angle = 0
                    mis.draw(mis.DATA.WIN, Jet2.DATA.COLS)
                    mis.timeexploded = Jet2.DATA.GLOBAL_TIMER.getTime()
                    check = False
                    continue
                if mis.check == False and mis.timeChecker():
                    Jet2.missiles.pop(Jet2.missiles.index(mis))
                    continue
                if mis.check:
                    if mis.heatseek:
                        mis.heatseeker(Jet1)
                    mis.move(mis.DATA.MISSILE_SPEED)
                    mis.draw(Jet2.DATA.WIN, Jet2.DATA.COLS)
                    if mis.rect.collidepoint((Jet1.rect.centerx,Jet1.rect.centery)):
                        mis.DATA.RUNNING = False  # type: ignore
                        text = mis.DATA.font.render("Player 2 Wins!" , (0,0,0))
                        text_rect = text[0].get_rect(center=(mis.DATA.SCREEN_WIDTH/2, mis.DATA.SCREEN_HEIGHT/2))
                        mis.DATA.WIN.blit(text[0], text_rect)
                        pygame.display.flip()
                        time.sleep(5)
                else:
                    mis.move(0)
                    mis.draw(mis.DATA.WIN, Jet2.DATA.COLS)
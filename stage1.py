import random
import pygame
from teemo import Teemo
from sys import exit
from minions import Minion
from pygame.locals import *
from gameoverscreen import gameoverscreen
steps = 10
from finishcreen import Finishscreen
from bullet import Bullet


moving = [pygame.image.load("teemo.png"),pygame.image.load("teemomove1.png"),pygame.image.load("teemo.png"),pygame.image.load("teemomove2.png") ]


def gameover(lose = False):
    if lose == True:
        gameoverscreen(start = True)
def victory(win = False):
    if win == True:
        Finishscreen(start = True)

def healthbar(self, surface):
    x, y = self.rect.x, self.rect.y
    w, h = self.image.get_size()
    bar_x = x - 12
    bar_y = y + h / 3
    surface.fill((255, 0, 0), (bar_x, bar_y, 100, 16))
    surface.fill((0, 255, 0), (bar_x, bar_y, self.life, 4))

def stage1screen(level,start=False):
    if start == True:
        pygame.mouse.set_visible(False)
        pygame.mixer.init()
        pygame.mixer.music.load("Event 14.mp3")
        pygame.mixer.music.set_volume(.5)
        sounddead = pygame.mixer.Sound('Arknights death sound.mp3')
        sound = pygame.mixer.Sound('shot.mp3')
        laugh_sound = pygame.mixer.Sound('teemolaugh.mp3')
        pygame.mixer.music.play()
        mark_pic = pygame.image.load('markfin.png').convert_alpha()
        mark_pic_rect = mark_pic.get_rect()
        font = pygame.font.SysFont("arial", 64)
        clock = pygame.time.Clock()
        time_passed = clock.tick(30)
        time_passed_seconds = time_passed / 300.0
        screen = pygame.display.set_mode((1800, 900))
        dart = pygame.image.load("dart.png").convert_alpha()
        teemo = pygame.image.load("teemo.png").convert_alpha()
        minions = pygame.image.load("minion.png").convert_alpha()
        minions2 = pygame.image.load("minion_attack.png").convert_alpha()
        map = pygame.image.load("map.png").convert_alpha()
        kill_count = 0
        screen.fill((255, 255, 255))
        bullet_group = pygame.sprite.Group()
        tim = Teemo(teemo, dart, moving)
        tim.set_pos()
        teemo = pygame.sprite.Group()

        mins = pygame.sprite.Group()
        teemo.add(tim)

        all_sprite = pygame.sprite.Group()
        all_sprite.add(teemo)


        while True:
            x, y = pygame.mouse.get_pos()
            x -= mark_pic.get_width() / 2
            y -= mark_pic.get_height() / 2

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        pygame.quit()
                        try:
                            exit()
                        finally:
                            return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    bullet_group.add(Bullet(dart, tim))
                    sound.play()



            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                tim.movement(-steps, 0)
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                tim.movement(steps, 0)
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                tim.movement(0, -steps)
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                tim.movement(0, steps)
            if keys[K_1]:
                kill_count += 50
            if keys[K_BACKSPACE]:
                sounddead.play()
                screen.fill((255, 255, 255))
                lose = font.render('Hi LOSER~', True, (255, 0, 0))
                screen.blit(lose,(750,700))
                pygame.mixer.quit()
                pygame.mouse.set_visible(True)
                return False

            time_passed = clock.tick(30)
            time = time_passed/1000

            if len(mins) <= 5 and random.random() < 0.02:
                mins.add(Minion(minions, minions2, tim, level))
            elif len(mins) > 5:
                mins = mins



            hit_mins = pygame.sprite.groupcollide(bullet_group,mins,True, False)
            if hit_mins:
                for minion in hit_mins.values():
                    minion[0].collide(1)
                    if minion[0].is_dead():
                        minion[0].kill()
                        kill_count += 1
                        laugh_sound.play()

            if kill_count >= 10:
                pygame.mixer.quit()
                victory(win = True)
                return False

            for tim in teemo:
                tim.collide(mins, 5)
                if tim.is_dead():
                    tim.kill()
                    sounddead.play()
                    screen.fill((255, 255, 255))
                    lose= font.render('Hi LOSER~', True, (255, 0, 0))
                    screen.blit(lose,(750,700))
                    pygame.mixer.quit()
                    pygame.mouse.set_visible(True)
                    return False


            screen.blit(map,(0,0))
            bullet_group.update(time)
            bullet_group.draw(screen)
            all_sprite.update(time)
            mins.update(time)
            mins.draw(screen)
            all_sprite.draw(screen)
            screen.blit(mark_pic, (x,y))
            tim.update(time)
            healthcode = font.render('Health:  ' + str(tim.health()), True, (255, 255, 255))
            killboard = font.render('Kill Count: ' + str(kill_count), True, (255, 255, 255))
            screen.blit(killboard,(1400,0))
            screen.blit(healthcode,(100,0))
            pygame.display.update()


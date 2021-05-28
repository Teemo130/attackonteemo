import random
import pygame
from teemo import Teemo
from sys import exit
from minions import Minion
from pygame.locals import *

from boss import Boss
from finisgcreen11 import Finishscreen
from bullet import Bullet
from shroom import Shroom
from canoon import Canon
from cannonshell import Canshell
from flame import Fire


moving = [pygame.image.load("teemo.png"),pygame.image.load("teemomove1.png"),pygame.image.load("teemo.png"),pygame.image.load("teemomove2.png") ]
"""tools"""
fire = pygame.image.load("fire_reverse.png")
flames = pygame.image.load("fire.png")
steps = 10
spike = pygame.image.load("spike.png")
def gameover(lose = False):
    while lose == True:
        pygame.mixer.music.stop()
        pygame.mouse.set_visible(True)
        pygame.display.set_caption("Attack On Teemo")
        screen = pygame.display.set_mode((1800, 900), FULLSCREEN)
        screen.fill((255, 255, 255))
        start = "please start again"
        my_font = pygame.font.SysFont("arial", 60)
        my_font.set_bold(True)
        name_surface = my_font.render(start, True, (255, 0, 0), (255, 255, 255))
        pygame.image.save(name_surface, "again.png")
        title = "GAME OVER"
        my_font2 = pygame.font.SysFont("arial", 100)
        name_surface1 = my_font2.render(title, True, (0, 0, 0), (255, 255, 255))
        pygame.image.save(name_surface1, "gameover.png")
        game_ov = pygame.image.load("gameover.jpg").convert_alpha()
        start_pic = pygame.image.load('again.png').convert_alpha()
        title_pic = pygame.image.load('gameover.png').convert_alpha()
        screen.blit(game_ov, (0, 0))
        screen.blit(start_pic, (700, 450))
        screen.blit(title_pic, (700, 100))
        start_button = start_button = pygame.Rect(700, 450, 1200, 520)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        mouse_press = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if mouse_press[0] and start_button.collidepoint(mouse_pos):
            # load screen
            Boss_screen(11,True)
        pygame.display.update()
def victory(win = False):
    if win == True:
        Finishscreen(10, start = True)

def healthbar(self, surface):
    x, y = self.rect.x, self.rect.y
    w, h = self.image.get_size()
    bar_x = x - 12
    bar_y = y + h / 3
    surface.fill((255, 0, 0), (bar_x, bar_y, 100, 16))
    surface.fill((0, 255, 0), (bar_x, bar_y, self.life, 4))

#------------------------------------------------------------------------------------------------------------------


def Boss_screen(level, start=False):
    if start == True:
        """sound"""
        pygame.mouse.set_visible(False)
        pygame.mixer.init()
        pygame.mixer.music.load("Event 09.mp3")
        pygame.mixer.music.set_volume(.5)
        sounddead = pygame.mixer.Sound('Arknights death sound.mp3')
        sound = pygame.mixer.Sound('shot.mp3')
        laugh_sound = pygame.mixer.Sound('teemolaugh.mp3')
        pygame.mixer.music.play()

        """pictures"""
        screen = pygame.display.set_mode((1800, 900), pygame.FULLSCREEN)
        mark_pic = pygame.image.load('Mark_white.png').convert_alpha()
        mark_pic_rect = mark_pic.get_rect()
        font = pygame.font.SysFont("arial", 64)
        clock = pygame.time.Clock()
        dart = pygame.image.load("dart.png").convert_alpha()
        teemo = pygame.image.load("teemo.png").convert_alpha()
        minions = pygame.image.load("minion_Elite.png").convert_alpha()
        minions2 = pygame.image.load("minion_attack.png").convert_alpha()
        canonmin = pygame.image.load("minion_cannonelite.png").convert_alpha()
        map = pygame.image.load("bossmap.png").convert_alpha()
        shr = pygame.image.load("shroom.png").convert_alpha()
        canonpic = pygame.image.load("cannon.png").convert_alpha()
        bang = pygame.image.load("shroom_explosion.png").convert_alpha()
        bosspic = pygame.image.load("boss.png").convert_alpha()
        bossdampic = pygame.image.load("boss_damge.png").convert_alpha()
        bosslimpic = pygame.image.load("boss_limit.png").convert_alpha()
        time_passed = clock.tick(30)
        time_passed_seconds = time_passed / 300.0


        #----------------------------------------------------------------------------------------------
        """groups and sprite"""
        bullet_group = pygame.sprite.Group()
        tim = Teemo(teemo, moving)
        tim.set_pos()
        bossdrag = Boss(bosspic,bossdampic,bosslimpic)
        boss_sprite = pygame.sprite.Group()
        boss_sprite.add(bossdrag)
        teemo = pygame.sprite.Group()
        shrooms = pygame.sprite.Group()
        mins = pygame.sprite.Group()
        teemo.add(tim)
        canoons = pygame.sprite.Group()
        all_sprite = pygame.sprite.Group()
        all_sprite.add(teemo)
        shroom_count = 3
        canonfire = pygame.sprite.Group()
        boss_fire = pygame.sprite.Group()
        spike_group = pygame.sprite.Group()

        while True:
            """make teemo shoot to the mid point of the ponter(which is the mark)"""
            x, y = pygame.mouse.get_pos()
            x -= mark_pic.get_width() / 2
            y -= mark_pic.get_height() / 2
            mouse = pygame.mouse.get_pos()


            """shooting part for teemo"""
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
                    bullet_group.add(Bullet(dart, tim, mouse, 50))
                    sound.play()
                if event.type == pygame.KEYDOWN:
                    if event == K_ESCAPE:
                        pygame.quit()
                        exit()


            """moving and cheats"""
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
                sounddead.play()
                gameover(lose=True)
                pygame.mouse.set_visible(True)
            if keys[K_SPACE] and shroom_count >= 1:
                shrooms.add(Shroom(shr, bang, tim))
                shroom_count -= 1
            if keys[K_BACKSPACE]:
                for tim in teemo:
                    tim.lose_hp(-1000)

            time_passed = clock.tick(30)
            time = time_passed/1000

            """spawning minions, canons, and fire the canon"""
            if len(mins) < 2 and random.random() < 0.02 and bossdrag.get_hp() <= 500:
                mins.add(Minion(minions, minions2, tim, level))
            elif len(mins) >= 2:
                mins = mins

            if len(canoons) < 1 and random.random() < 0.02 and bossdrag.get_hp() <= 200:
                can = Canon(canonmin, tim, level)
                canoons.add(can)
            elif len(canoons) >= 1:
                canoons = canoons
            if len(canoons) > 0 and random.random() < 0.05:
                canonfire.add(Canshell(canonpic, can, tim, 15))

            if len(boss_fire) < 1 and (random.random() < 0.05 and random.random()> 0):
                boss_fire.add(Fire(fire))
            elif len(boss_fire) < 1 and (random.random() > 0.05 and random.random()< 0.1):
                boss_fire.add(Fire(flames))
            if len(spike_group) < 4 and random.random() < 0.05:
                spike_group.add(Canshell(spike, bossdrag, tim, 15))
            elif len(spike_group) >+4:
                spike_group = spike_group

            """collisions"""
            hit_teemo = pygame.sprite.groupcollide(canonfire, teemo, True, False)
            for fires in boss_fire:
                burn_teemo = pygame.sprite.collide_mask(fires,tim)
                if burn_teemo:
                    for tim in teemo:
                        tim.lose_hp(10)

            pinch_teemo = pygame.sprite.groupcollide(spike_group,teemo, True, False)
            if hit_teemo:
                for teemo in hit_teemo.values():
                    teemo[0].lose_hp(100)


            if pinch_teemo:
                for teemo in pinch_teemo.values():
                    teemo[0].lose_hp(35)

            for bullet in bullet_group:
                hit_drag = pygame.sprite.collide_mask(bullet, bossdrag)
                if hit_drag:
                    bossdrag.collide(tim.damage_dult(.01))
                    bullet.kill()
                    if bossdrag.is_dead():
                        bossdrag.kill()
                        laugh_sound.play()

            for shrom in shrooms:
                boom_drag = pygame.sprite.collide_mask(shrom, bossdrag)
                if boom_drag:
                    bossdrag.collide(30)
                    shrom.kill()
                    if bossdrag.is_dead():
                        bossdrag.kill()
                        laugh_sound.play()

            hit_cans = pygame.sprite.groupcollide(bullet_group, canoons, True, False)
            boom_cans = pygame.sprite.groupcollide(shrooms, canoons, False, False)
            if hit_cans:
                for canon in hit_cans.values():
                    canon[0].collide(1)
                    if canon[0].is_dead():
                        canon[0].kill()
                        laugh_sound.play()

            if boom_cans:
                for shroom in shrooms:
                    shroom.collide(canoons)
                for canon in boom_cans.values():
                    canon[0].collide(40)
                    if canon[0].is_dead():
                        canon[0].kill()
                        laugh_sound.play()


            hit_mins = pygame.sprite.groupcollide(bullet_group,mins,True, False)
            boom_mins = pygame.sprite.groupcollide(shrooms,mins, False, False)
            if hit_mins:
                for minion in hit_mins.values():
                    minion[0].collide(1)
                    if minion[0].is_dead():
                        minion[0].kill()
                        laugh_sound.play()

            if boom_mins:
                for shroom in shrooms:
                    shroom.collide(mins)
                for minion in boom_mins.values():
                    minion[0].collide(5)
                    if minion[0].is_dead():
                        minion[0].kill()
                        laugh_sound.play()

            for tim in teemo:
                touch_drag = pygame.sprite.collide_mask(tim, bossdrag)
                tim.collide(mins, 5)
                tim.collide(canonfire,100)
                tim.collide(canoons, 1)
                if touch_drag:
                    tim.collide(boss_sprite, 20)
                if tim.is_dead():
                    tim.kill()
                    sounddead.play()
                    gameover(lose=True)
                    pygame.mouse.set_visible(True)
                    return False

            """calculate the killing numbers"""
            if bossdrag.get_hp() <= 0:
                pygame.mixer.quit()
                victory(win = True)
                return False

            screen.blit(map,(-200,0))
            boss_fire.update(time)
            boss_fire.draw(screen)
            bullet_group.update(time)
            bullet_group.draw(screen)
            boss_sprite.update()
            bossdrag.update()
            boss_sprite.draw(screen)
            spike_group.update(time)
            spike_group.draw(screen)
            canonfire.update(time)
            canonfire.draw(screen)
            canoons.update(time)
            canoons.draw(screen)
            shrooms.update(time)
            shrooms.draw(screen)
            all_sprite.update(time)
            mins.update(time)
            mins.draw(screen)
            all_sprite.draw(screen)
            screen.blit(mark_pic, (x,y))
            tim.update(time)
            healthcode = font.render('Health:  ' + str(tim.health()), True, (255, 255, 255))
            killboard = font.render('BOSS: ' + str(bossdrag.get_hp()), True, (255, 255, 255))
            screen.blit(killboard,(1400,0))
            screen.blit(healthcode,(100,0))
            pygame.display.update()
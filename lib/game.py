import sys, pygame, shutil, os
from pygame.locals import *
from pygame.font import *
from random import random as rng
from msvcrt import getche

import _thread, threading

enemy_hp = 500

def shoot(screen, thread_name, projectile_image, projectile_speed, projectile_damage, player_pos, walls, enemy_object):
    projectile = pygame.image.load(projectile_image)
    projectile_object = projectile.get_rect()
    projectile_object = projectile_object.move(player_pos[0] + 50, player_pos[1] + 30)

    print(thread_name + " is active.")
    
    while not projectile_object.colliderect(walls[1]):
        projectile_object = projectile_object.move(projectile_speed, 0)
        screen.blit(projectile, projectile_object)
        pygame.display.flip()
        
        if projectile_object.colliderect(enemy_object):
            global enemy_hp
            enemy_hp -= projectile_damage
            break
    
    print(thread_name + " is dead.")
        
    #projectile_object = projectile_object.move(-5000,-5000)
    #screen.blit(projectile, projectile_object)
    #pygame.display.flip()
    
def game(screen, window_size, background_color, colors):

    #objects speeds
    fireball_speed = 2
    iceball_speed = 1
    
    #projectiles damage
    fireball_damage = 200
    iceball_damage = 50
    
    global enemy_hp
    
    #enemy_hp
    enemy_hp_font = Font('font/LCD.ttf', 24)
    enemy_hp_text = enemy_hp_font.render(str(enemy_hp) + " / 500", True, colors["white"], colors["black"])
    enemy_hp_object = enemy_hp_text.get_rect()
    enemy_hp_object.center = (540, 220)
    
    #define fps
    clock = pygame.time.Clock()
    
    #game loop + object preset
    while True:
        
        #setting up scene
        #game happens in the sub loop
    
        #images & objects
        player = pygame.image.load("img/player.png")
        player = pygame.transform.scale(player, (100, 100))
        player_object = player.get_rect()
        player_object = player_object.move(150,230)
        player_pos = [150, 230]

        #enemy_hp = 500
        enemy = pygame.image.load("img/enemy.png")
        enemy = pygame.transform.scale(enemy, (85, 100))
        enemy_object = enemy.get_rect()
        enemy_object = enemy_object.move(500,230)
        enemy_pos = [500, 230]
        lock_enemy = False
        
        vertical_left_wall = pygame.image.load("img/vertical_wall.png")
        vertical_left_wall_object = vertical_left_wall.get_rect()
        vertical_left_wall_object = vertical_left_wall_object.move(0,0)

        vertical_right_wall = pygame.image.load("img/vertical_wall.png")
        vertical_right_wall_object = vertical_right_wall.get_rect()
        vertical_right_wall_object = vertical_right_wall_object.move(999,0)

        horizontal_up_wall = pygame.image.load("img/horizontal_wall.png")
        horizontal_up_wall_object = horizontal_up_wall.get_rect()
        horizontal_up_wall_object = horizontal_up_wall_object.move(0,0)

        horizontal_down_wall = pygame.image.load("img/horizontal_wall.png")
        horizontal_down_wall_object = horizontal_down_wall.get_rect()
        horizontal_down_wall_object = horizontal_down_wall_object.move(0,599)

        walls = [vertical_left_wall_object, vertical_right_wall_object, horizontal_down_wall_object, horizontal_up_wall_object]
        
        #threads count
        thread_count = 0
        
        #game loop
        while True:
            
            #set fps
            clock.tick(60)
            
            #fill_background_color
            screen.fill(background_color)
            
            #array of all keys pressed
            keys_pressed = pygame.key.get_pressed()
            
            #utility keys
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            
                if((keys_pressed[pygame.K_RALT] or keys_pressed[pygame.K_LALT]) and keys_pressed[pygame.K_F4]) or keys_pressed[pygame.K_ESCAPE]: sys.exit()
                                
                #player_movement
                elif keys_pressed[pygame.K_k]:
                    try:
                        thread_count += 1
                        
                        #shoot(
                               #screen,
                               #thread_name,
                               #projectile_image,
                               #projectile_speed,
                               #projectile_damage,
                               #player_pos,
                               #walls,
                               #enemy_object,
                               #enemy_hp
                               #)
                        
                        _thread.start_new_thread( shoot, (
                                                          screen,
                                                          "Thread " + str(thread_count),
                                                          "img/fireball.png",
                                                          fireball_speed,
                                                          fireball_damage,
                                                          player_pos,
                                                          walls,
                                                          enemy_object
                                                          )
                                                )
                    except:
                       print("Error: unable to start thread")
                       
                elif keys_pressed[pygame.K_j]:
                    try:
                        thread_count += 1
                        
                        #shoot(
                               #screen,
                               #thread_name,
                               #projectile_image,
                               #projectile_speed,
                               #projectile_damage,
                               #player_pos,
                               #walls,
                               #enemy_object,
                               #enemy_hp
                               #)
                        
                        _thread.start_new_thread( shoot, (
                                                          screen,
                                                          "Thread " + str(thread_count),
                                                          "img/iceball.png",
                                                          iceball_speed,
                                                          iceball_damage,
                                                          player_pos,
                                                          walls,
                                                          enemy_object
                                                          )
                                                )
                    except:
                       print("Error: unable to start thread")
                       
                else:
                    pass
                    
            if enemy_hp <= 0 and lock_enemy == False:
                enemy_object = enemy_object.move(-5000,-5000)
                enemy_hp_object = enemy_hp_object.move(-5000,-5000)
                lock_enemy = True
            
            enemy_hp_text = enemy_hp_font.render(str(enemy_hp) + " / 500", True, colors["white"], colors["black"])
            
            #render entities
            screen.blit(player, player_object)
            screen.blit(enemy, enemy_object)           
            screen.blit(enemy_hp_text, enemy_hp_object)
            
            #render walls
            screen.blit(vertical_left_wall, vertical_left_wall_object)
            screen.blit(vertical_right_wall, vertical_right_wall_object)
            screen.blit(horizontal_up_wall, horizontal_up_wall_object)
            screen.blit(horizontal_down_wall, horizontal_down_wall_object)
            
            #pygame.display.update()
            pygame.display.flip()
import sys, pygame, shutil, os
from pygame.locals import *
from random import random as rng
from msvcrt import getche

from game import game

#start
pygame.init()
pygame.display.set_caption('Wizards')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#screen_sizes
window_size = 1000, 600
screen = pygame.display.set_mode(window_size)

colors = {
            "black":(0, 0, 0),
            "white":(255,255,255),
            "random":(int(rng() * 1000 % 256), int(rng() * 1000 % 256), int(rng() * 1000 % 256) )
         }

background_color = colors["black"]

game(screen, window_size, background_color, colors)
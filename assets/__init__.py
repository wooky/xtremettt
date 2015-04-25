import pygame
from background import Background

human = None
random = None
blocking = None
smart = None
jon = None

background = None

font = "Comic Sans MS"

custom = {'x': None, 'o': None}

def init(screen):
	global human, random, blocking, smart, jon, background
	human = random = blocking = smart = jon = pygame.image.load("assets/human.png").convert_alpha()
	
	background = Background(screen, pygame.image.load("assets/title.png").convert_alpha())

import pygame
from background import Background

pic = {}
background = None

font = "Comic Sans MS"

custom = {'x': None, 'o': None}

def init(screen):
	global pic, background
	
	pic['human'] = pygame.image.load("assets/human.png").convert_alpha()
	pic['random'] = pygame.image.load("assets/random.png").convert_alpha()
	pic['blocking'] = pygame.image.load("assets/blocking.png").convert_alpha()
	pic['smart'] = pygame.image.load("assets/smart.png").convert_alpha()
	pic['jon'] = pygame.image.load("assets/jon.png").convert_alpha()
	
	background = Background(screen, pygame.image.load("assets/title.png").convert_alpha())

import pygame
from background import Background

human = None
random = None
blocking = None
smart = None
jon = None

background = None

font = "Comic Sans MS"

customx = None
customo = None

def init(screen):
	global human, random, blocking, smart, jon, background
	human = pygame.image.load("assets/human.png").convert_alpha()
	random = pygame.image.load("assets/random.png").convert_alpha()
	blocking = pygame.image.load("assets/blocking.png").convert_alpha()
	smart = pygame.image.load("assets/smart.png").convert_alpha()
	jon = pygame.image.load("assets/jon.png").convert_alpha()
	
	background = Background(screen, pygame.image.load("assets/title.png").convert_alpha())

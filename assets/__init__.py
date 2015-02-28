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
	human = pygame.image.load("assets/human.png").convert()
	random = pygame.image.load("assets/random.png").convert()
	blocking = pygame.image.load("assets/blocking.png").convert()
	smart = pygame.image.load("assets/smart.png").convert()
	jon = pygame.image.load("assets/jon.png").convert()
	
	background = Background(screen, pygame.image.load("assets/title.png").convert())

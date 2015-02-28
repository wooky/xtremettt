import pygame, assets
from screen.title import TitleScreen
from screen.exit import WussScreen

pygame.display.init()
pygame.font.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Super Extreme Tic-Tac-Toe")

assets.init(screen)
font = pygame.font.SysFont(assets.font, 16)
white = pygame.Color("white")
black = pygame.Color("black")

clock = pygame.time.Clock()

currentScreen = TitleScreen(screen)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): currentScreen = WussScreen(screen)
		currentScreen = currentScreen.event(event)
	
	currentScreen.logic()
	
	fps = font.render(str(int(clock.get_fps())) + " FPS", True, white)
	fps_rect = fps.get_rect()
	fps_rect.topright = (width, 0)
	
	currentScreen.draw()
	
	screen.blit(fps, fps_rect)
	pygame.display.flip()
	clock.tick(15)
	
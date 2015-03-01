import pygame, assets, thread
from screen.title import TitleScreen
from screen.exit import WussScreen
from server.server import Server

pygame.font.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Super Extreme Tic-Tac-Toe")

assets.init(screen)
font = pygame.font.SysFont(assets.font, 16)
white = (255,255,255)
black = (0,0,0)

clock = pygame.time.Clock()

server = Server(0)
thread.start_new_thread(server.run, ())

currentScreen = TitleScreen(screen)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): currentScreen = WussScreen(screen)
		currentScreen = currentScreen.event(event)
	
	currentScreen.logic()
	
	fps = font.render(str(int(clock.get_fps())) + " FPS", True, white, black)
	fps_rect = fps.get_rect()
	fps_rect.topright = (width, 0)
	
	currentScreen.draw()
	
	screen.blit(fps, fps_rect)
	pygame.display.flip()
	clock.tick(15)
	
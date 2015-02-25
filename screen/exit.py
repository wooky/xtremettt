import pygame, textwrap, sys

class WussScreen:
	def __init__(self, screen):
		self.screen = screen
		ayy = u"""	░░░░░░▄▀▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒█
					░░░░█▒▒▄▀▀▀▀▀▄▄▒▒▒▒▒▒▒▒▒▄▄▀▀▀▀▀▀▄
					░░▄▀▒▒▒▄█████▄▒█▒▒▒▒▒▒▒█▒▄█████▄▒█
					░█▒▒▒▒▐███████▌▌▒█▒▒▒▒▒█▒▐██████▌▒█
					▀▒▒▒▒▒▒▀█████▀▒▒█▒░▄▒▄█▒▒▀█████▀▒▒▒█
					▒▒▐▒▒▒░░░░▒▒▒▒▒█▒░▒▒▀▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█
					▒▌▒▒▒░░░▒▒▒▒▒▄▀▒░▒▄█▄█▄▒▀▄▒▒▒▒▒▒▒▒▒▒▒▌
					▒▌▒▒▒▒░▒▒▒▒▒▒▀▄▒▒█▌▌▌▌▌█▄▀▒▒▒▒▒▒▒▒▒▒▒▐
					▒▐▒▒▒▒▒▒▒▒▒▒▒▒▒▌▒▒▀███▀▒▌▒▒▒▒▒▒▒▒▒▒▒▒▌
					▀▀▄▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒█
					▀▄▒▀▄▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▒▒▒▄▄▄▄▒▒▒▒▒▒▄▄▀
					▒▒▀▄▒▀▄▀▀▀▄▀▀▀▀▄▄▄▄▄▄▄▀░░░░▀▀▀▀▀▀
					▒▒▒▒▀▄▐▒▒▒▒▒▒▒▒▒▒▒▒▒▐
					░▄▄▄░░▄░░▄░▄░░▄░░▄░░░░▄▄░▄▄░░░▄▄▄░░░▄▄▄
					█▄▄▄█░█▄▄█░█▄▄█░░█░░░█░░█░░█░█▄▄▄█░█░░░█
					█░░░█░░█░░░░█░░░░█░░░█░░█░░█░█░░░█░█░░░█
					▀░░░▀░░▀░░░░▀░░░░▀▀▀░░░░░░░░░▀░░░▀░▀▄▄▄▀"""
		lmao = ayy.splitlines()
		font = pygame.font.SysFont("Courier New", 18)
		
		self.surfs = []
		self.rects = []
		
		for i in range(len(lmao)):
			surf = font.render(textwrap.dedent(lmao[i]), True, (255,255,255))
			rect = surf.get_rect()
			rect.left = 100
			rect.top = 0 if i==0 else self.rects[i-1].bottom
			
			self.surfs.append(surf)
			self.rects.append(rect)
	
	def event(self, event):
		return self
	
	def logic(self):
		pass
	
	def draw(self):
		self.screen.fill((0,0,0))
		for i in range(len(self.surfs)): self.screen.blit(self.surfs[i], self.rects[i])
		pygame.display.flip()
		pygame.time.wait(1000)
		sys.exit()
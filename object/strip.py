import pygame, assets

class Strip:
	def __init__(self, screen, caption, color):
		self.screen = screen
		self.color = color
		
		font = pygame.font.SysFont(assets.font, 20)
		self.rect = pygame.Rect(0, 0, screen.get_width(), font.size(caption)[1] + 4)
		self.rect.centery = screen.get_height()/2
		
		self.caption_surf = font.render(caption, True, (255,255,255))
		self.caption_rect = self.caption_surf.get_rect()
		self.caption_rect.center = (screen.get_width()/2, screen.get_height()/2)
		
	def draw(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		self.screen.blit(self.caption_surf, self.caption_rect)
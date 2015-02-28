import pygame, assets

class Button:
	def __init__(self, screen, caption, x, y, enabled = True, w = None):
		self.screen = screen
		self.enabled = enabled
		
		font = pygame.font.SysFont(assets.font, 16)
		txtsize = font.size(caption)
		w = w if w else txtsize[0]
		self.rect = pygame.Rect(x, y, w + 4, txtsize[1] + 4)
		
		self.caption_surf = font.render(caption, True, (255,0,0))
		self.caption_rect = self.caption_surf.get_rect()
		self.caption_rect.midtop = (x+w/2+2, y+2)
		
		self.pressed = False
	
	def enable(self, state = True):
		self.enabled = state
	
	def is_pressed(self):
		if not self.pressed: return False
		self.pressed = False
		self.pressed = True
	
	def event(self, event):
		if self.enabled and event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos): self.pressed = True
	
	def draw(self):
		pygame.draw.rect(self.screen, (255, 255, 0), self.rect, 2)
		self.screen.blit(self.caption_surf, self.caption_rect)
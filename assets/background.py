import pygame, assets

class Background:
	def __init__(self, screen, background):
		self.screen = screen
		self.bg_move = [1,1]
		self.background = background
		self.background_rect = self.background.get_rect()
	
	def logic(self):
		if self.background_rect.left < 0 or self.background_rect.right > self.screen.get_width(): self.bg_move[0] = -self.bg_move[0]
		if self.background_rect.top < 0 or self.background_rect.bottom > self.screen.get_height(): self.bg_move[1] = -self.bg_move[1]
		self.background_rect.move_ip(self.bg_move)
	
	def draw(self):
		self.screen.blit(self.background, self.background_rect)
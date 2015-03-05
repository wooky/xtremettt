import pygame, assets
from options import OptionsScreen

class TitleScreen:
	def __init__(self, screen):
		self.screen = screen
		
		big_font = pygame.font.SysFont(assets.font, 90)
		small_font = pygame.font.SysFont(assets.font, 24)
		
		self.heading = small_font.render("Super Extreme", True, (255,255,255))
		self.title = big_font.render("TIC-TAC-TOE", True, (255,255,255))
		self.title_shadow = big_font.render("TIC-TAC-TOE", True, (192,192,192))
		self.start = small_font.render("Press ENTER to start!", True, (255,255,255))
				
		self.title_shadow_rect = self.title_shadow.get_rect()
		self.title_shadow_rect.center = (screen.get_width()/2, screen.get_height()/2)
		
		self.title_rect = self.title_shadow_rect.move(-10, -10)
		
		self.heading_rect = self.heading.get_rect()
		self.heading_rect.topleft = self.title_rect.topleft
		self.heading_rect.left -= 5
		
		self.start_rect = self.start.get_rect()
		self.start_rect.center = (self.title_shadow_rect.centerx, (self.title_rect.bottom + screen.get_height())/2)
				
	def event(self, event):
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
			OptionsScreen.instance = OptionsScreen(self.screen)
			return OptionsScreen.instance
		else: return self
	
	def logic(self):
		assets.background.logic()
	
	def draw(self):
		self.screen.fill((0,0,0))
		assets.background.draw()
		self.screen.blit(self.title_shadow, self.title_shadow_rect)
		self.screen.blit(self.title, self.title_rect)
		self.screen.blit(self.heading, self.heading_rect)
		self.screen.blit(self.start, self.start_rect)
		
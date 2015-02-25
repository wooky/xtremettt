import pygame, assets
from object.textbox import Textbox
from object.radiogroup import RadioGroup
from game import GameScreen

class OptionsScreen:
	def __init__(self, screen, player_x = "", player_o = "", type_x = 0, type_o = 0):
		self.screen = screen
		
		font = pygame.font.SysFont(assets.font, 36)
		self.title = font.render("Select Your Players!", True, (255,255,255))
		self.title_rect = self.title.get_rect()
		self.title_rect.midtop = (screen.get_width()/2, 0)
		
		font = pygame.font.SysFont(assets.font, 24)
		self.player_x_title = font.render("Player X", True, (255,255,255))
		self.player_o_title = font.render("Player O", True, (255,255,255))
		
		font = pygame.font.SysFont(assets.font, 20)
		self.footer = font.render("Enter players' names and types and press ENTER to begin1!!!13!", True, (255,255,255))
		
		self.player_x_rect = self.player_x_title.get_rect()
		self.player_x_rect.midtop = (screen.get_width()/4, 50)
		self.player_o_rect = self.player_o_title.get_rect()
		self.player_o_rect.midtop = (screen.get_width()*3/4, 50)
		self.footer_rect = self.footer.get_rect()
		self.footer_rect.midtop = (screen.get_width()/2, screen.get_height()*3/4)
		
		self.player_x_box = Textbox(screen, 20, self.player_x_rect.bottom + 20, screen.get_width()/2 - 40, 11, player_x)
		self.player_o_box = Textbox(screen, screen.get_width()/2 + 20, self.player_o_rect.bottom + 20, screen.get_width()/2 - 40, 11, player_o)
		
		types = ["Human Player", "Random Player", "Blocking Player", "Smart Player", "jon"]
		self.player_x_type = RadioGroup(screen, 20, self.player_x_rect.bottom + 70, type_x, True, types)
		self.player_o_type = RadioGroup(screen, screen.get_width()/2 + 20, self.player_o_rect.bottom + 70, type_o, True, types)
		
	def event(self, event):
		self.player_x_box.event(event)
		self.player_o_box.event(event)
		self.player_x_type.event(event)
		self.player_o_type.event(event)
		
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.player_x_box.get_text() and self.player_o_box.get_text():
			return GameScreen(self.screen, self.player_x_box.get_text(), self.player_o_box.get_text(), self.player_x_type.get_selection(), self.player_o_type.get_selection())
		else: return self
		
	def logic(self):
		assets.background.logic()
		self.player_x_box.logic()
		self.player_o_box.logic()
		self.player_x_type.logic()
		self.player_o_type.logic()
		
	def draw(self):
		self.screen.fill((0,0,0))
		assets.background.draw()
		self.screen.blit(self.title, self.title_rect)
		self.screen.blit(self.player_x_title, self.player_x_rect)
		self.screen.blit(self.player_o_title, self.player_o_rect)
		self.screen.blit(self.footer, self.footer_rect)
		self.player_x_box.draw()
		self.player_o_box.draw()
		self.player_x_type.draw()
		self.player_o_type.draw()
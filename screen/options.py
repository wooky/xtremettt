import pygame, assets
from collections import OrderedDict
from object.textbox import Textbox
from object.radiogroup import RadioGroup
from object.button import Button
from logic.player import HumanPlayer
from logic.ai import RandomPlayer, BlockingPlayer, SmartPlayer, jon
from camoverlay import CamOverlay
from game import GameScreen

class OptionsScreen:
	def __init__(self, screen, online = False, player_x = "", type_x = HumanPlayer, args = ("", HumanPlayer)):
		self.screen = screen
		self.online = online
		
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
		self.footer_rect.midbottom = (screen.get_width()/2, screen.get_height()-10)
		
		self.player_x_box = Textbox(screen, 20, self.player_x_rect.bottom + 20, screen.get_width()/2 - 40, 15, player_x)
		self.player_o_box = Textbox(screen, screen.get_width()/2 + 20, self.player_o_rect.bottom + 20, screen.get_width()/2 - 40, 15, args[0] if not online else "")
		
		types = ((HumanPlayer, HumanPlayer.get_type()), (RandomPlayer, RandomPlayer.get_type()), (BlockingPlayer, BlockingPlayer.get_type()), (SmartPlayer, SmartPlayer.get_type()), (jon, jon.get_type()))
		self.player_x_type = RadioGroup(screen, 20, self.player_x_rect.bottom + 70, type_x, True, *types)
		self.player_o_type = RadioGroup(screen, screen.get_width()/2 + 20, self.player_o_rect.bottom + 70, args[1] if not online else None, True, *types)
		
		self.player_x_pic_rect = pygame.Rect(20, screen.get_height() - 200, 128, 128)
		self.player_o_pic_rect = pygame.Rect(screen.get_width()/2+20, screen.get_height() - 200, 128, 128)
		
		self.player_x_take_photo = Button(screen, "Take Photo", self.player_x_pic_rect.right+4, self.player_x_pic_rect.y)
		self.player_x_clear_photo = Button(screen, "Clear Photo", self.player_x_pic_rect.right+4, self.player_x_pic_rect.y + 30)
		self.player_o_take_photo = Button(screen, "Take Photo", self.player_o_pic_rect.right+4, self.player_o_pic_rect.y)
		self.player_o_clear_photo = Button(screen, "Clear Photo", self.player_o_pic_rect.right+4, self.player_o_pic_rect.y + 30)
		
		self.local = RadioGroup(screen, screen.get_width()/2+152, screen.get_height()*3/4, online, True, (False, "Offline Play"), (True, "Online Play"))
		
		#TODO: add multiplayer elements here
		
		self.next_screen = self
		
	def event(self, event):
		self.local.event(event)
		self.player_x_box.event(event)
		self.player_x_type.event(event)
		self.player_x_take_photo.event(event)
		self.player_x_clear_photo.event(event)
		
		if self.online:
			pass
		else:
			self.player_o_box.event(event)
			self.player_o_type.event(event)
			self.player_o_take_photo.event(event)
			self.player_o_clear_photo.event(event)
		
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.player_x_box.get_text() and self.player_o_box.get_text() and self.player_x_type.get_selection() and self.player_o_type.get_selection():
				return GameScreen(self.screen, self.online, self.player_x_box.get_text(), self.player_o_box.get_text(), self.player_x_type.get_selection(), self.player_o_type.get_selection(), self.player_x_pic, self.player_o_pic)
	
		return self.next_screen
		
	def logic(self):
		assets.background.logic()
		self.local.logic()
		self.player_x_box.logic()
		self.player_x_type.logic()
		
		if self.player_x_clear_photo.is_pressed(): assets.custom['x'] = None
		elif self.player_x_take_photo.is_pressed():
			extras = () if self.online else (self.player_o_box.get_text(), self.player_o_type.get_selection())
			self.next_screen = CamOverlay(self.screen, (self.online, self.player_x_box.get_text(), self.player_x_type.get_selection(), extras), assets.custom, 'x')
		
		self.online = self.local.get_selection()
		self.player_x_pic = assets.custom['x'] if assets.custom['x'] else self.player_x_type.get_selection().get_image()
		
		if self.online:
			pass
		else:
			self.player_o_box.logic()
			self.player_o_type.logic()
			
			if self.player_o_clear_photo.is_pressed(): assets.custom['o'] = None
			elif self.player_o_take_photo.is_pressed():
				self.next_screen = CamOverlay(self.screen, (self.online, self.player_x_box.get_text(), self.player_x_type.get_selection(), (self.player_o_box.get_text(), self.player_o_type.get_selection())), assets.custom, 'o')
			
			self.player_o_pic = assets.custom['o'] if assets.custom['o'] else self.player_o_type.get_selection().get_image()
		
	def draw(self):
		self.screen.fill((0,0,0))
		assets.background.draw()
		self.screen.blit(self.title, self.title_rect)
		self.screen.blit(self.footer, self.footer_rect)
		self.local.draw()
		self.player_x_box.draw()
		self.player_x_type.draw()
		self.player_x_take_photo.draw()
		self.player_x_clear_photo.draw()
		self.screen.blit(self.player_x_pic, self.player_x_pic_rect)
		
		if self.online:
			pass
		else:
			self.screen.blit(self.player_x_title, self.player_x_rect)
			self.screen.blit(self.player_o_title, self.player_o_rect)
			self.player_o_box.draw()
			self.player_o_type.draw()
			self.player_o_take_photo.draw()
			self.player_o_clear_photo.draw()
			self.screen.blit(self.player_o_pic, self.player_o_pic_rect)
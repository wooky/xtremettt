import pygame, assets, random
from logic.board import Board

class GameScreen:
	def __init__(self, screen, player_x, player_o, type_x, type_o):
		self.screen = screen
		self.font = pygame.font.SysFont(assets.font, 20)
		big_font = pygame.font.SysFont(assets.font, 120)
		
		self.player_x = player_x
		self.player_o = player_o
		self.type_x = type_x
		self.type_o = type_o
		
		self.board = Board()
		self.x = type_x(player_x, self.board)
		self.o = type_o(player_o, self.board)
		self.x.set_opponent(self.o)
		self.o.set_opponent(self.x)
		self.turn = self.o	#hax
		
		self.player_x_surf = self.font.render(player_x, True, (255,255,255))
		self.player_x_rect = self.player_x_surf.get_rect()
		self.player_x_rect.bottomleft = (0, screen.get_height())
		
		self.player_o_surf = self.font.render(player_o, True, (255,255,255))
		self.player_o_rect = self.player_o_surf.get_rect()
		self.player_o_rect.bottomright = (screen.get_width(), screen.get_height())
		
		self.player_x_img = self.x.get_image()
		self.player_x_img_rect = self.player_x_img.get_rect()
		self.player_x_img_rect.bottomleft = (0, self.player_x_rect.top)
		
		self.player_o_img = self.o.get_image()
		self.player_o_img_rect = self.player_o_img.get_rect()
		self.player_o_img_rect.bottomright = (screen.get_width(), self.player_o_rect.top)
		
		self.lines = [	[random.randint(screen.get_width()/2-64-32, screen.get_width()/2-64+32), random.randint(384-32, 128*3+32)],
						[random.randint(screen.get_width()/2+64-32, screen.get_width()/2+64+32), random.randint(384-32, 128*3+32)],
						[random.randint(screen.get_width()/2+192-32, screen.get_width()/2+192+32), random.randint(128-32, 128+32)],
						[random.randint(screen.get_width()/2+192-32, screen.get_width()/2+192+32), random.randint(256-32, 256+32)]]
		self.mark_x = big_font.render("X", True, (255,255,255))
		self.mark_o = big_font.render("O", True, (255,255,255))
		
		self.locked = False
		self.text = None
	
	def event(self, event):
		if self.turn:
			if not self.locked: self.turn.event(event)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
			from options import OptionsScreen
			return OptionsScreen(self.screen, self.player_x, self.player_o, self.type_x, self.type_o)
		return self
	
	def logic(self):
		assets.background.logic()
	
		msg = None
		if self.board.is_changed():
			if self.board.is_winner(self.x):
				msg = self.x.get_win_text()
				self.turn = None
			elif self.board.is_winner(self.o):
				msg = self.o.get_win_text()
				self.turn = None
			elif self.board.is_filled():
				msg = "nobody is winner. all is loser"
				self.turn = None
			else:
				self.turn = self.x if self.turn == self.o else self.o
				if self.turn.taunts():
					self.counter = -10
					self.locked = True
				else:
					msg = self.turn.get_message()
		
		if self.locked == True:
			self.counter += 1
			if self.counter >= 0:
				msg = self.turn.get_message()[:self.counter/2]
				if len(msg) == len(self.turn.get_message()): self.locked = False
		elif self.turn: self.turn.logic()
		
		if msg != None: self.text = self.font.render(msg, True, (255,255,255))
		
	def draw(self):
		self.screen.fill((0,0,0))
		assets.background.draw()
		pygame.draw.line(self.screen, (255,255,255), (self.screen.get_width()/2-64, 0), self.lines[0])
		pygame.draw.line(self.screen, (255,255,255), (self.screen.get_width()/2+64, 0), self.lines[1])
		pygame.draw.line(self.screen, (255,255,255), (self.screen.get_width()/2-192, 128), self.lines[2])
		pygame.draw.line(self.screen, (255,255,255), (self.screen.get_width()/2-192, 256), self.lines[3])
		self.screen.blit(self.player_x_img, self.player_x_img_rect)
		self.screen.blit(self.player_o_img, self.player_o_img_rect)
		self.screen.blit(self.player_x_surf, self.player_x_rect)
		self.screen.blit(self.player_o_surf, self.player_o_rect)
		r = pygame.draw.rect(self.screen, (255,255,255), (self.player_x_img_rect.right+20, self.screen.get_height()-40, self.player_o_img_rect.left-self.player_x_img_rect.right-40, 30), 2)
		if self.text: self.screen.blit(self.text, r)
		
		b = self.board.get_board()
		for i in range(len(b)):
			for j in range(len(b[i])):
				if b[i][j] == self.x: mark = self.mark_x
				elif b[i][j] == self.o: mark = self.mark_o
				else: continue
				
				mark_rect = mark.get_rect()
				mark_rect.topleft = (self.screen.get_width()/2-192+128*j, i*128)
				self.screen.blit(mark, mark_rect)
		
		if not self.turn: self.screen.blit(self.font.render("THE GAME IS OVER! Press ENTER to go back to the main menu", True, (255,255,255), (255,0,0)), (0,self.screen.get_height()/2))
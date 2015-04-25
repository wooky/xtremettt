import pygame, assets

class Player:
	def __init__(self, name, board):
		self.name = name
		self.board = board
	
	@staticmethod
	def get_type(): return None
	
	@staticmethod
	def get_image(): pass
	
	@staticmethod
	def taunts(): return True
	
	def get_message(self): pass
	def get_win_text(self): return self.name + " is winner!!!"
	def set_opponent(self, opponent): self.opponent = opponent
	def event(self, event): pass
	def logic(self): pass

class HumanPlayer(Player):
	def __init__(self, name, board):
		Player.__init__(self, name, board)

	@staticmethod
	def get_type():
		return "Human Player"
		
	@staticmethod
	def get_image():
		return assets.human
	
	@staticmethod
	def taunts():
		return False
	
	def get_message(self):
		return self.name + ", it's your turn!"
	
	def event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN: self.board.put_mark(self, event.pos[1]/128, (event.pos[0] - pygame.display.Info().current_w/2 + 192)/128)
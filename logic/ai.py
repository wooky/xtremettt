import pygame, assets, random
from player import Player

def cause_victory(board, player, row, col):
	b = board.get_board()
	if b[row][col]: return None
	
	#Search horizontally
	count = 0
	for i in range(3):
		if b[row][i] == player: count += 1
	if count == 2: return True
	
	#Search vertically
	count = 0
	for i in range(3):
		if b[i][col] == player: count += 1
	if count == 2: return True
	
	#Search in a backslash formation
	if row == col:
		count = 0
		for i in range(3):
			if b[i][i] == player: count += 1
		if count == 2: return True
	
	#Search in a slash formation
	if row+col == 2:
		count = 0
		for i in range(3):
			if b[i][2-i] == player: count += 1
		if count == 2: return True
	
	#Fail
	return False

class RandomPlayer(Player):
	texts = [""]

	def __init__(self, name, board):
		Player.__init__(self, name, board)
		self.taunt = None
	
	@staticmethod
	def get_type():
		return "Random Player"
	
	@staticmethod
	def get_image():
		return assets.random
	
	def get_message(self):
		if not self.taunt: self.taunt = random.choice(RandomPlayer.texts)
		return self.taunt
		
	def logic(self):
		while not self.board.put_mark(self, random.randint(0,2), random.randint(0,2)): pass
		self.taunt = None
		
class BlockingPlayer(RandomPlayer):
	texts = [""]
	
	def __init__(self, name, board):
		RandomPlayer.__init__(self, name, board)
		self.taunt = None
	
	@staticmethod
	def get_type():
		return "Blocking Player"
	
	@staticmethod
	def get_image():
		return assets.blocking
	
	def get_message(self):
		if not self.taunt: self.taunt = random.choice(BlockingPlayer.texts)
		return self.taunt
	
	def logic(self):
		for i in range(3):
			for j in range(3):
				if cause_victory(self.board, self.opponent, i, j):
					self.board.put_mark(self, i, j)
					self.taunt = None
					return
		RandomPlayer.logic(self)
		
class SmartPlayer(BlockingPlayer):
	texts = [""]
	
	def __init__(self, name, board):
		BlockingPlayer.__init__(self, name, board)
		self.taunt = None
	
	@staticmethod
	def get_type():
		return "Smart Player"
	
	@staticmethod
	def get_image():
		return assets.smart
	
	def get_message(self):
		if not self.taunt: self.taunt = random.choice(SmartPlayer.texts)
		return self.taunt
	
	def logic(self):
		for i in range(3):
			for j in range(3):
				if cause_victory(self.board, self, i, j):
					self.board.put_mark(self, i, j)
					self.taunt = None
					return
		BlockingPlayer.logic(self)

class jon(RandomPlayer):
	def __init__(self, name, board):
		RandomPlayer.__init__(self, name, board)
		self.taunt = None
	
	@staticmethod
	def get_type():
		return "jon"
	
	@staticmethod
	def get_image():
		return assets.jon
	
	def get_message(self):
		return ""
	
	def logic(self):
		for i in range(3):
			for j in range(3):
				if cause_victory(self.board, self, i, j) == False and cause_victory(self.board, self.opponent, i, j) == False:
					self.board.put_mark(self, i, j)
					self.taunt = None
					return
		
		for i in range(3):
			for j in range(3):
				if cause_victory(self.board, self, i, j) == False:
					self.board.put_mark(self, i, j)
					self.taunt = None
					return
		
		RandomPlayer.logic(self)

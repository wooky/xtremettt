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
	texts = [	"ummmmmm     ",
				"I guess this'll work     ",
				"I'm not sure     ",
				"sdfljdfjhdfjh     "]

	def __init__(self, name, board):
		Player.__init__(self, name, board)
		self.taunt = None
	
	def get_image(self):
		return assets.random
	
	def get_message(self):
		if not self.taunt: self.taunt = random.choice(RandomPlayer.texts)
		return self.taunt
	
	def get_win_text(self):
		return "i has winned???"
		
	def logic(self):
		while not self.board.put_mark(self, random.randint(0,2), random.randint(0,2)): pass
		self.taunt = None
		
class BlockingPlayer(RandomPlayer):
	texts = [	"u wot m8     ",
				"u havin a giggle m8     ",
				"ill bash yor fockin head in     ",
				"i swer on me mum     "]
	
	def __init__(self, name, board):
		RandomPlayer.__init__(self, name, board)
		self.taunt = None
	
	def get_image(self):
		return assets.blocking
	
	def get_message(self):
		if not self.taunt: self.taunt = random.choice(BlockingPlayer.texts)
		return self.taunt
	
	def get_win_text(self):
		return "Yeah, you like that, you retard?"
	
	def logic(self):
		for i in range(3):
			for j in range(3):
				if cause_victory(self.board, self.opponent, i, j):
					self.board.put_mark(self, i, j)
					self.taunt = None
					return
		RandomPlayer.logic(self)
		
class SmartPlayer(BlockingPlayer):
	texts = [	"you can't defeat me     ",
				"I am unstoppable     ",
				"you're gonna get #rekt son     ",
				"give up now     ",
				"pansy     "]
	
	def __init__(self, name, board):
		BlockingPlayer.__init__(self, name, board)
		self.taunt = None
	
	def get_image(self):
		return assets.smart
	
	def get_message(self):
		if not self.taunt: self.taunt = random.choice(SmartPlayer.texts)
		return self.taunt
	
	def get_win_text(self):
		return "Kneel down before " + self.name
	
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
	
	def get_image(self):
		return assets.jon
	
	def get_message(self):
		if not self.taunt: self.taunt = "a" + "y"*random.randint(2,20) + " lmao     "
		return self.taunt
	
	def get_win_text(self):
		return "ayy what the fuck lmao"
	
	def logic(self):
		for i in range(3):
			for j in range(3):
				if cause_victory(self.board, self, i, j) == False and cause_victory(self.board, self.opponent, i, j) == False:
					self.board.put_mark(self, i, j)
					self.taunt = None
					return
		RandomPlayer.logic(self)

import pygame, copy

class Board:
	def __init__(self):
		self.board = [[None, None, None], [None, None, None], [None, None, None]]
		self.marks = 0
		self.changed = True
	
	def get_board(self):
		return self.board
		
	def is_filled(self):
		return self.marks == 9
	
	def is_changed(self):
		if not self.changed: return False
		
		self.changed = False
		return True
		
	def update_board(self, player, row, col):
		self.board[row][col] = player
		self.changed = True
		self.marks += 1
	
	def put_mark(self, player, row, col):
		if row < 0 or row > 2 or col < 0 or col > 2: return False
		elif self.board[row][col]: return False
		self.update_board(player, row, col)
		return True
		
	def is_winner(self, player):
		#Seek horizontally
		for row in self.board:
			if row[0] == player and row[1] == player and row[2] == player: return True
		
		#Seek vertically
		for i in range(3):
			if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player: return True
		
		#Seek in a backslash formation
		if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player: return True
		
		#Seek in a slash formation
		if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player: return True
		
		#Fail
		return False
			
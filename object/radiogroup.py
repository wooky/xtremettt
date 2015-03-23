import pygame, assets

class RadioGroup:
	def __init__(self, screen, x, y, selection, *args):
		font = pygame.font.SysFont(assets.font, 16)
		
		self.screen = screen
		self.x = x
		self.y = y
		self.r = font.size("SAMPLE SIZE")[1] / 2
		self.args = args
		
		self.selection = selection
		
		self.surfs = []
		for t in args: self.surfs.append(font.render(t[1], True, (255,255,255)))
		
		self.rects = []
		for i in range(len(args)):
			r = self.surfs[i].get_rect()
			r.topleft = (self.x + self.r*2 + 3, self.y + self.r*i*2 + 3)
			self.rects.append(r)
	
	def get_selection(self):
		return self.selection
	
	def event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] >= self.x + 2 and event.pos[0] <= self.x + 2 + self.r*2:
			index = (event.pos[1] - self.y - 3)/(self.r * 2)
			if index >= 0 and index < len(self.surfs): self.selection = self.args[index][0]
	
	def logic(self):
		pass
	
	def draw(self):
		for i in range(len(self.surfs)):
			pygame.draw.circle(self.screen, (255,0,0), (self.x+2+self.r, self.y+self.r*i*2+3+self.r), self.r, 0 if self.selection == self.args[i][0] else 2)
			self.screen.blit(self.surfs[i], self.rects[i])

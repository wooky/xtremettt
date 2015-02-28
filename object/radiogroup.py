import pygame, assets

class RadioGroup:
	def __init__(self, screen, x, y, selection, draw_border, args):
		font = pygame.font.SysFont(assets.font, 16)
		
		self.screen = screen
		self.x = x
		self.y = y
		self.r = font.size("SAMPLE SIZE")[1] / 2
		self.draw_border = draw_border
		self.args = args
		
		self.selection = args.index(selection) if selection else None
		
		self.surfs = []
		for t in args: self.surfs.append(font.render(t.get_type(), True, (255,255,255)))
		
		self.rects = []
		for i in range(len(args)):
			r = self.surfs[i].get_rect()
			r.topleft = (self.x + self.r*2 + 3, self.y + self.r*i*2 + 3)
			self.rects.append(r)
	
	def get_selection(self):
		return self.args[self.selection]
	
	def event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] >= self.x + 2 and event.pos[0] <= self.x + 2 + self.r*2:
			index = (event.pos[1] - self.y - 3)/(self.r * 2)
			if index >= 0 and index < len(self.surfs): self.selection = index
	
	def logic(self):
		pass
	
	def draw(self):
		for i in range(len(self.surfs)):
			pygame.draw.circle(self.screen, (255,0,0), (self.x+2+self.r, self.y+self.r*i*2+3+self.r), self.r, 0 if self.selection == i else 2)
			self.screen.blit(self.surfs[i], self.rects[i])

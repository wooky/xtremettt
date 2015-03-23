import pygame, assets, string

class Textbox:
	focused = None

	def __init__(self, screen, x, y, w, limit = 0, text = "", editable = True):
		self.font = pygame.font.SysFont(assets.font, 16)
	
		self.screen = screen
		self.rect = pygame.Rect(x, y, w, self.font.size("SAMPLE TEXT")[1] + 4)
		self.limit = limit
		self.text = text
		self.editable = editable
		
		self.blink_time = 0
		self.blinking = False
	
	def set_text(self, txt):
		self.text = txt
	
	def get_text(self):
		return self.text
	
	def event(self, event):
		if self.editable:
			if Textbox.focused != self and event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos): Textbox.focused = self
			elif Textbox.focused == self and event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE: self.text = self.text[:-1] 
				elif event.key >= 32 and event.key < 256 and chr(event.key) in string.printable and (self.limit == 0 or len(self.text) <= self.limit): self.text += chr(event.key)
			
	def logic(self):
		self.text_surf = self.font.render(self.text + ("_" if Textbox.focused == self and self.blinking else ""), True, (255,0,0))
		self.text_rect = self.text_surf.get_rect()
		self.text_rect.topleft = (self.rect.x+2, self.rect.y+2)
		
		if self.text_rect.width > self.rect.width:
			r = pygame.Rect(self.text_rect.width-self.rect.width+4, 0, self.rect.width, self.rect.height)
			s = pygame.Surface((self.rect.width-3, self.rect.height-3))
			s.blit(self.text_surf, (0,0), r)
			self.text_surf = s
	
		if Textbox.focused == self:
			self.blink_time += 1
			if self.blink_time == 7:
				self.blink_time = 0
				self.blinking = not self.blinking
				
	def draw(self):
		pygame.draw.rect(self.screen, (255, 255, 0), self.rect, 2)
		self.screen.blit(self.text_surf, self.text_rect)
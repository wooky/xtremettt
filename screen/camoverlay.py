import pygame, pygame.camera, assets
from object.strip import Strip

class CamOverlay:
	def __init__(self, screen, otherargs, var, val):
		pygame.camera.init()
		self.screen = screen
		self.otherargs = otherargs
		
		self.strip = None
		camlist = pygame.camera.list_cameras()
		if not camlist:
			self.strip = Strip(screen, "NO CAMERAS DETECTED!!!1 Press ENTER to return", (255,0,0))
			pygame.camera.quit()
			return
		
		self.var = var
		self.val = val
		
		self.camera = pygame.camera.Camera(camlist[0])
		self.camera.start()
		
		self.bg = pygame.Rect(screen.get_width()/8, screen.get_height()/4, screen.get_width()*3/4, screen.get_height()/2)
		
		self.rect = pygame.Rect(0, 0, 128, 128)
		self.rect.center = self.bg.center
		
		self.txt = pygame.font.SysFont(assets.font, 28).render("Press ENTER to take photo", True, (0,0,0))
		self.txt_rect = self.txt.get_rect()
		self.txt_rect.midbottom = self.bg.midbottom
	
	def event(self, event):
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
			if not self.strip:
				self.var[self.val] = self.pic
				self.camera.stop()
				pygame.camera.quit()
			from options import OptionsScreen
			return OptionsScreen(self.screen, *self.otherargs)
		
		return self
	
	def logic(self):
		img = self.camera.get_image()
		img_rect = img.get_rect()
		
		self.pic = pygame.Surface((128, 128))
		self.pic_rect = self.pic.get_rect()
		self.pic_rect.center = self.rect.center
		
		self.pic.blit(img, img_rect, (img_rect.width/2-64,img_rect.height/2-64,128,128))
	
	def draw(self):
		if self.strip:
			self.strip.draw()
			return
		
		pygame.draw.rect(self.screen, (255,255,0), self.bg)
		self.screen.blit(self.pic, self.pic_rect)
		self.screen.blit(self.txt, self.txt_rect)
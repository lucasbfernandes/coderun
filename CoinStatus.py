import pygame
import time
import Sprite_image

from pygame import *
from time import clock

class CoinStatus(pygame.sprite.Sprite):

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)
		self.statusSprite = Sprite_image.Sprite_image("images/CoinStatus - GameUFU.png",5,(69,101))

		self.rect = pygame.Rect(self.statusSprite.images[0].get_rect())
		self.rect.topleft = (0,0)

		self.statusSprite.frame = -1
		self.image = None

	def update(self):

		if self.statusSprite.frame > -1:
			self.image = self.statusSprite.images[self.statusSprite.frame]
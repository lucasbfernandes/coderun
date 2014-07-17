import pygame
import time
import Sprite_image

from time import clock
from pygame import *

class InfoCoin(pygame.sprite.Sprite):

	indexArray = [(998,327),(2808,316),(4230,320),(5411,320),(7735,320)]

	def __init__(self, index):

		pygame.sprite.Sprite.__init__(self)

		self.coinSprite = Sprite_image.Sprite_image("images/InfoCoin - GameUFU.png",1,(102,102))

		self.rect = pygame.Rect(self.coinSprite.images[0].get_rect())

		self.image = self.coinSprite.images[0]

		self.rect.topleft = self.indexArray[index]

		self.collideRect = pygame.Rect((self.rect.left + 22, self.rect.top + 18), (59,61))


	def update(self, personagem, coinStatus):

		if personagem.collideBody.colliderect(self.rect) or personagem.collideBody.colliderect(self.rect) and coinStatus.statusSprite.frame < 4:
			coinStatus.statusSprite.frame += 1
			self.kill()


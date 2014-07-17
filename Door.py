import pygame
import Sprite_image
import time
from time import clock
from pygame import *

class Door(pygame.sprite.Sprite):

	indexArray = [(737,285),(1187,285),(1638,285),(4444,285),(5254,285),(5955,285), (3576,285)]

	def __init__(self, index):

		#chamando o metodo construtor de sprite
		pygame.sprite.Sprite.__init__(self)

		self.doorClosed = Sprite_image.Sprite_image("images/DoorClosed - GameUFU.png",1,(84,192))
		self.doorOpening = Sprite_image.Sprite_image("images/DoorOpening - GameUFU.png",2,(92,192))

		self.image = self.doorClosed.images[0]
		self.rect = pygame.Rect(self.doorClosed.images[0].get_rect())

		self.rect.topleft = self.indexArray[index]
		self.lastTime = 0

		self.openDelayTime = 2
		self.closedDelayTime = 1/4

		self.inside = False
		self.firstTime = True

	def update(self, personagem, currentTime):
		
		#retorna um vetor de valores booleanos baseados no estado das teclas do teclado
		keys = pygame.key.get_pressed()

		if self.inside == True:

				if self.image == self.doorOpening.images[0]:

					if currentTime - self.lastTime >= self.openDelayTime or self.firstTime == True:

						self.image = self.doorOpening.images[1]
						self.firstTime = False
						self.lastTime = clock()

				else:
					if currentTime - self.lastTime >= self.closedDelayTime:

						self.image = self.doorOpening.images[0]
						self.lastTime = clock()


				if keys[K_x]:

					self.image = self.doorClosed.images[0]
					self.inside = False

		elif keys[K_z] and personagem.collideBody.colliderect(self.rect):

			self.image = self.doorOpening.images[0]
			self.inside = True
			self.firstTime = True
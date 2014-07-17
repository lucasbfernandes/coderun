import pygame
import time
import Sprite_image
from pygame import *
from time import clock

class LockGate(pygame.sprite.Sprite):

	def __init__(self, startPos1, startPos2, ID):

		#chamando o metodo construtor de sprite
		pygame.sprite.Sprite.__init__(self)

		self.southGate = Sprite_image.Sprite_image("images/LockGate - GameUFU.png",1,(45,116))
		self.northGate = Sprite_image.Sprite_image("images/LockGate2 - GameUFU.png",1,(45,116))

		self.southGateImage = self.southGate.images[0]
		self.northGateImage = self.northGate.images[0]

		self.southRect = pygame.Rect((self.southGate.images[0].get_rect()))
		self.northRect = pygame.Rect((self.northGate.images[0].get_rect()))

		self.southRect.topleft = startPos1
		self.northRect.topleft = startPos2

		self.southCollideRect = pygame.Rect((self.southRect.left + 15, self.southRect.top + 6), (17,104))
		self.northCollideRect = pygame.Rect((self.northRect.left + 15, self.northRect.top + 6), (17,104))

		self.firstTime = True
		self.lastTime = 0

		self.delay = 1/4
		self.movRate = 10

		self.accumulated = 0
		self.id = ID


	def update(self, openBool, currentTime, scenario):

		if openBool:

			if (currentTime - self.lastTime >= self.delay or self.firstTime) and self.accumulated < 150:

				self.northRect = self.northRect.move((0,-self.movRate))
				self.southRect = self.southRect.move((0,self.movRate))

				self.accumulated += self.movRate

				self.lastTime = clock()
				self.firstTime = False

			if self.accumulated >= 100:

				self.northCollideRect = self.northCollideRect.move((0,-self.accumulated))
				self.southCollideRect = self.southCollideRect.move((0,self.accumulated))

				if self.id == 1:
					scenario.collideWall1 = scenario.collideWall1.move((0,-2*self.accumulated))
				elif self.id == 2:
					scenario.collideWall2 = scenario.collideWall2.move((0,-2*self.accumulated))
				elif self.id == 3:
					scenario.collideWall3 = scenario.collideWall3.move((0,-2*self.accumulated))


import pygame
import time
import Sprite_image
from pygame import *
import time

class Robot(pygame.sprite.Sprite):

	def __init__(self, startPos, walkDirection, walkAmount):

		pygame.sprite.Sprite.__init__(self)
		self.walkSprite = Sprite_image.Sprite_image("images/Robo - GameUFU.png",5,(95,122))

		self.rect = pygame.Rect(self.walkSprite.images[0].get_rect())
		self.rect.topleft = startPos
		self.image = self.walkSprite.images[self.walkSprite.frame]

		self.movSpeed = 5
		self.changex = False

		self.accumulated = 0
		self.walkAmount = walkAmount

		self.currentTime = 0
		self.lastTime = 0
		self.delayRate = 0.1

		if walkDirection == "right":
			self.direction = 1
		elif walkDirection == "left":
			self.direction = 2

	def update(self):

		self.currentTime = time.clock()

		if self.direction == 1:
			self.rect = self.rect.move((self.movSpeed,0))
			self.accumulated += self.movSpeed
			self.changex = True

			if self.accumulated == self.walkAmount:
				self.accumulated = 0
				self.direction = 2

		elif self.direction == 2:
			self.rect = self.rect.move((-self.movSpeed,0))
			self.changex = False
			self.accumulated += self.movSpeed

			if self.accumulated == self.walkAmount:
				self.accumulated = 0
				self.direction = 1


		self.image = self.walkSprite.images[self.walkSprite.frame]

		if self.currentTime - self.lastTime >= self.delayRate:
			self.walkSprite.frame = (self.walkSprite.frame + 1)%self.walkSprite.total_frames
			self.lastTime = self.currentTime

		self.image = pygame.transform.flip(self.image,self.changex,False)
import pygame
import time
import Sprite_image
from pygame import *
from time import clock

class LockTerminal(pygame.sprite.Sprite):

	def __init__(self, startPos):

		#chamando o metodo construtor de sprite
		pygame.sprite.Sprite.__init__(self)

		self.terminal = Sprite_image.Sprite_image("images/LockTerminal - GameUFU.png",1,(150,150))
		self.image = self.terminal.images[0]
		
		self.rect = pygame.Rect((self.terminal.images[0].get_rect()))
		self.rect.topleft = startPos

		self.openBool = False

	def update(self, personagem):

		#retorna um vetor de valores booleanos baseados no estado das teclas do teclado
		keys = pygame.key.get_pressed()

		if keys[K_z] and personagem.collideBody.colliderect(self.rect):

			self.openBool = True
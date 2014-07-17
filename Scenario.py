import pygame
import time
import Sprite_image
import sprite_utilities
import Door
import LockSystem
import CoinStatus
import InfoCoin

from pygame import *
from time import clock


class Scenario():

	def __init__(self, img_Location, size):
		
		self.scenario = pygame.image.load(img_Location)
		self.scenarioRect = self.scenario.get_rect()

		self.rect = pygame.Rect((0,0),size)
		self.image = self.scenario.subsurface(self.rect)

		self.lightGroup = pygame.sprite.Group()
		self.blockGroup = pygame.sprite.Group()
		self.doorGroup = pygame.sprite.Group()
		self.coinGroup = pygame.sprite.Group()

		self.leftFree = True
		self.rightFree = True

		self.collideWall1 = pygame.Rect((2335,43),(14,244))
		self.collideWall2 = pygame.Rect((4168,43),(14,244))
		self.collideWall3 = pygame.Rect((7015,43),(14,244))

	def loadLight(self):

		for i in range(5):
			self.lightGroup.add(Light.Light())

	def loadBlock(self):

		for i in range(5):
			self.blockGroup.add(Blocks.Block(i))

	def loadDoor(self):

		for i in range(7):
			self.doorGroup.add(Door.Door(i))

	def loadLockSystem(self):

		self.lockSystem1 = LockSystem.LockSystem((2319,353),(2319,280),(2220,304), 1)
		self.lockSystem2 = LockSystem.LockSystem((4154,353),(4154,280),(4052,304), 2)
		self.lockSystem3 = LockSystem.LockSystem((7000,353),(7000,280),(6900,304), 3)

	def loadInfoCoin(self):

		for i in range(5):
			self.coinGroup.add(InfoCoin.InfoCoin(i))

	def loadCoinStatus(self):

		self.coinStatus = CoinStatus.CoinStatus()

	def update(self, option, personagem, robot1, robot2, robot3, robot4, robot5, robot6, robot7, movRate):

		self.tempScenario = pygame.Surface.copy(self.scenario)

		self.lightGroup.update(clock())
		self.doorGroup.update(personagem, clock())
		self.coinGroup.update(personagem, self.coinStatus)

		self.coinStatus.update()

		self.lockSystem1.update(personagem, self)
		self.lockSystem2.update(personagem, self)
		self.lockSystem3.update(personagem, self)

		#self.lightGroup.draw(self.scenario)
		#self.blockGroup.draw(self.scenario)
		self.doorGroup.draw(self.tempScenario)
		self.coinGroup.draw(self.tempScenario)

		self.tempScenario.blit(self.lockSystem1.lockGate.northGateImage, self.lockSystem1.lockGate.northRect)
		self.tempScenario.blit(self.lockSystem1.lockGate.southGateImage, self.lockSystem1.lockGate.southRect)
		self.tempScenario.blit(self.lockSystem1.lockTerminal.image, self.lockSystem1.lockTerminal.rect)

		self.tempScenario.blit(self.lockSystem2.lockGate.northGateImage, self.lockSystem2.lockGate.northRect)
		self.tempScenario.blit(self.lockSystem2.lockGate.southGateImage, self.lockSystem2.lockGate.southRect)
		self.tempScenario.blit(self.lockSystem2.lockTerminal.image, self.lockSystem2.lockTerminal.rect)

		self.tempScenario.blit(self.lockSystem3.lockGate.northGateImage, self.lockSystem3.lockGate.northRect)
		self.tempScenario.blit(self.lockSystem3.lockGate.southGateImage, self.lockSystem3.lockGate.southRect)
		self.tempScenario.blit(self.lockSystem3.lockTerminal.image, self.lockSystem3.lockTerminal.rect)

		self.tempScenario.blit(robot1.image, robot1.rect)
		self.tempScenario.blit(robot2.image, robot2.rect)
		self.tempScenario.blit(robot3.image, robot3.rect)
		self.tempScenario.blit(robot4.image, robot4.rect)
		self.tempScenario.blit(robot5.image, robot5.rect)
		self.tempScenario.blit(robot6.image, robot6.rect)
		self.tempScenario.blit(robot7.image, robot7.rect)

		if self.rect.right != self.scenarioRect.right and option == 1:

			if not personagem.firstTimeMid:
				self.leftFree = False
				self.rightFree = False

				if (not personagem.rightCollided or personagem.firstTimeCollided) and not personagem.firstTimeNotCollided:
					self.rect = self.rect.move((movRate,0))
					personagem.firstTimeCollided = False

				if personagem.firstTimeNotCollided:
					personagem.firstTimeNotCollided = False

				if self.rect.right == self.scenarioRect.right:
					self.rightFree = True
			else:
				self.leftFree = True
				self.rightFree = False

			self.image = self.tempScenario.subsurface(self.rect)

		elif self.rect.left != self.scenarioRect.left and option == 2:

			if not personagem.firstTimeMid:
				self.leftFree = False
				self.rightFree = False

				if (not personagem.leftCollided or personagem.firstTimeCollided) and not personagem.firstTimeNotCollided:
					self.rect = self.rect.move((-movRate,0))
					personagem.firstTimeCollided = False

				if personagem.firstTimeNotCollided:
					personagem.firstTimeNotCollided = False
									
				if self.rect.left == self.scenarioRect.left:
					self.leftFree = True
			else:
				self.leftFree = False
				self.rightFree = True

			self.image = self.tempScenario.subsurface(self.rect)

		elif option == 3:

			self.image = self.tempScenario.subsurface(self.rect)





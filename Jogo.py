import pygame
import personagem
import Sprite_image
import Scenario
import sprite_utilities
import LockSystem
import Robot

from pygame import *
import time

class Jogo():

	def __init__(self):

		self.scenario = Scenario.Scenario("images/Scenario - GameUFU.png",(800,500))

		self.screen = pygame.display.set_mode(self.scenario.image.get_size(), FULLSCREEN)

		self.scenario.scenario.convert()

		self.startTime = None
		self.lastTime = 0

		self.scenario.loadDoor()
		self.scenario.loadLockSystem()

		self.scenario.loadInfoCoin()
		self.scenario.loadCoinStatus()

		self.screen.blit(self.scenario.image,(0,0))
		pygame.display.set_caption("CodeRun!")

		self.gameover = False
		self.gamedone = False


		self.font = pygame.font.SysFont("arial",20)
		self.tempoAtual = 0

		#self.personagem = pygame.sprite.GroupSingle()
		self.personagem = personagem.Personagem(
		                                (0,330),
		                                "Images/Walking - GameUFU.png", 8, (121,140),
		                                "Images/Jumping - GameUFU.png",4,(121,140), 
		                                "Images/Standing - GameUFU.png",6,(121,140))

		self.robot1 = Robot.Robot((900,330), "left", 500)
		self.robot2 = Robot.Robot((1000,330), "right", 500)
		self.robot3 = Robot.Robot((1900,350), "left", 600)
		self.robot4 = Robot.Robot((3835,330), "left", 1450)
		self.robot5 = Robot.Robot((4210,330), "right", 470)
		self.robot6 = Robot.Robot((6610,330), "left", 1920)
		self.robot7 = Robot.Robot((6550,330), "left", 900)

	def robotCollision(self):

		if (self.personagem.collideHead.colliderect(self.robot1.rect)) or (self.personagem.collideBody.colliderect(self.robot1.rect)):
			return 1

		elif (self.personagem.collideHead.colliderect(self.robot2.rect)) or (self.personagem.collideBody.colliderect(self.robot2.rect)):
			return 2  

		elif (self.personagem.collideHead.colliderect(self.robot3.rect)) or (self.personagem.collideBody.colliderect(self.robot3.rect)):
			return 3

		elif (self.personagem.collideHead.colliderect(self.robot4.rect)) or (self.personagem.collideBody.colliderect(self.robot4.rect)):
			return 3

		elif (self.personagem.collideHead.colliderect(self.robot5.rect)) or (self.personagem.collideBody.colliderect(self.robot5.rect)):
			return 3

		elif (self.personagem.collideHead.colliderect(self.robot6.rect)) or (self.personagem.collideBody.colliderect(self.robot6.rect)):
			return 3

		elif (self.personagem.collideHead.colliderect(self.robot7.rect)) or (self.personagem.collideBody.colliderect(self.robot7.rect)):
			return 3

		else:
			return 0		

	def update(self):
		
		self.tempoAtual = time.clock()

		if self.personagem.rect.right == 461:

			if self.personagem.movingRight:
				self.scenario.update(1, self.personagem, self.robot1, self.robot2, self.robot3, self.robot4, self.robot5, self.robot6, self.robot7, 10)

			elif self.personagem.movingLeft:
				self.scenario.update(2, self.personagem, self.robot1, self.robot2, self.robot3, self.robot4, self.robot5, self.robot6, self.robot7, 10)

			else:
				self.scenario.update(3, self.personagem, self.robot1, self.robot2, self.robot3, self.robot4, self.robot5, self.robot6, self.robot7, 10)

		else:
			self.scenario.update(3, self.personagem, self.robot1, self.robot2, self.robot3, self.robot4, self.robot5, self.robot6, self.robot7, 0)

		if self.personagem.firstTimeMid == True:
			self.personagem.firstTimeMid = False

		if self.scenario.coinStatus.statusSprite.frame == 4 and self.personagem.collideBody.left < 420:
			self.gamedone = True

		self.robot1.update()
		self.robot2.update()
		self.robot3.update()
		self.robot4.update()
		self.robot5.update()
		self.robot6.update()
		self.robot7.update()
		self.personagem.update(self.scenario)

		self.screen.blit(self.scenario.image,(0,0))

		self.textImg = self.font.render("Tempo: " + str(round(self.tempoAtual - self.startTime,2)),1,(255,255,255))
		self.screen.blit(self.textImg, (5,472))

		self.textImg = self.font.render("Code",1,(0,255,0))
		self.screen.blit(self.textImg, (140,472))

		self.textImg = self.font.render("Run",1,(255,0,0))
		self.screen.blit(self.textImg, (190,472))

		if sprite_utilities.anyDoorInside(self.scenario) == False:
			self.screen.blit(self.personagem.image, self.personagem.rect)

		if self.robotCollision() and not sprite_utilities.anyDoorInside(self.scenario):
			self.gameover = True

		if self.scenario.coinStatus.image != None:
			self.screen.blit(self.scenario.coinStatus.image, self.scenario.coinStatus.rect)
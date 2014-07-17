import pygame
import personagem
import Sprite_image
import Scenario
import Jogo

from pygame import *
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
game = Jogo.Jogo()

startGame = True
howToPlay = False
      
title = True
firstTimeClock = False

currentTime = 0


lastTime = 0

pygame.mixer.music.load("sound/HighTension.wav")

#Game loop
var = True
while var:
	
	currentTime = time.clock()

	if startGame:
		game = Jogo.Jogo()
		pygame.mixer.music.play(-1)
		startGame = False

	for evento in pygame.event.get():
		if evento.type is pygame.QUIT:
			var = False

	keys = pygame.key.get_pressed()

	if keys[K_ESCAPE]:
		var = False

	clock.tick(60)

	if not game.gameover and not howToPlay and not game.gamedone and not title:

		if firstTimeClock:
			game.startTime = time.clock()
			firstTimeClock = False

		game.update()

	elif title:
		font8 = pygame.font.SysFont("arial",150)
		
		textImg8 = font8.render("Code",1,(0,255,0))
		game.screen.blit(textImg8, (20,150))

		textImg8 = font8.render("Run",1,(255,0,0))
		game.screen.blit(textImg8, (450,150))

		if currentTime - lastTime >= 3:
			title = False
			howToPlay = True
			game.screen.blit(game.scenario.image,(0,0))

	elif howToPlay:

		font4 = pygame.font.SysFont("arial",30)
		font5 = pygame.font.SysFont("arial",17)

		textImg4 = font4.render("COMO JOGAR",1,(0,255,0))
		game.screen.blit(textImg4, (290, 10))

		textImg4 = font4.render("Capture todas as informações secretas!",1,(255,255,255))
		game.screen.blit(textImg4, (120, 80))

		textImg5 = font5.render("Não deixe que os robôs cheguem perto de você de forma alguma!",1,(255,0,0))
		game.screen.blit(textImg5, (20,140))

		textImg5 = font5.render("Eles foram cuidadosamente programados para detectar intrusos que se aproximam deles...",1,(255,255,255))
		game.screen.blit(textImg5, (20,180))

		textImg5 = font5.render("Mas por sorte quem os desenvolveu não pensou no caso em que o intruso está atrás das portas",1,(255,255,255))
		game.screen.blit(textImg5, (20,220))

		textImg4 = font4.render("É A SUA CHANCE!",1,(0,255,0))
		game.screen.blit(textImg4, (270, 280))

		textImg5 = font5.render("Pressione a tecla Z para entrar nas portas claras e X para sair delas",1,(255,255,255))
		game.screen.blit(textImg5, (20,340))

		textImg5 = font5.render("Pressione a tecla Z para abrir o portão",1,(255,255,255))
		game.screen.blit(textImg5, (20,380))

		textImg5 = font5.render("Utilize as teclas direcionais para se movimentar e pular",1,(255,255,255))
		game.screen.blit(textImg5, (20,420))	

		textImg5 = font5.render("Pressione SPACE para começar a jogar!",1,(255,255,255))
		game.screen.blit(textImg5, (270,475))

        #retorna um vetor de valores booleanos baseados no estado das teclas do teclado
		keys = pygame.key.get_pressed()

		if keys[K_SPACE]:
			howToPlay = False
			firstTimeClock = True

	elif game.gameover:

		font1 = pygame.font.SysFont("arial",80)
		textImg1 = font1.render("VOCÊ FOI PEGO!",1,(255,0,0))

		font2 = pygame.font.SysFont("arial",20)
		textImg2 = font2.render("Pressione SPACE para jogar novamente",1,(255,255,255))

		font3 = pygame.font.SysFont("arial",20)
		textImg3 = font3.render("Pressione ESC para sair do jogo",1,(255,255,255))

		game.screen.blit(textImg1, (80,100))
		game.screen.blit(textImg2, (200, 380))
		game.screen.blit(textImg3, (200, 420))		

        #retorna um vetor de valores booleanos baseados no estado das teclas do teclado
		keys = pygame.key.get_pressed()

		if keys[K_SPACE]:
			startGame = True
			firstTimeClock = True
			howToPlay = True
		if keys[K_ESCAPE]:
			var = False

	elif game.gamedone:

		font6 = pygame.font.SysFont("arial",80)
		font7 = pygame.font.SysFont("arial",20)

		textImg6 = font6.render("VOCÊ CONSEGUIU!",1,(255,0,0))
		game.screen.blit(textImg6, (35,100))

		textImg7 = font7.render("Seu tempo: " + str(round(game.tempoAtual - game.startTime,2)),1,(255,255,255))
		game.screen.blit(textImg7, (330,300))

		textImg7 = font7.render("Pressione SPACE para jogar novamente",1,(255,255,255))
		game.screen.blit(textImg7, (200,380))

		textImg7 = font7.render("Pressione ESC para sair do jogo",1,(255,255,255))
		game.screen.blit(textImg7, (200,420))

        #retorna um vetor de valores booleanos baseados no estado das teclas do teclado
		keys = pygame.key.get_pressed()

		if keys[K_SPACE]:
			startGame = True
			firstTimeClock = True
			howToPlay = True
		if keys[K_ESCAPE]:
			var = False


	pygame.display.flip()

pygame.quit()

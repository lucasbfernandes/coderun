import pygame
import sprite_utilities
import Sprite_image
from pygame import *
import time
import math

class Personagem(pygame.sprite.Sprite): 

    movSpeed = 20

    #metodo construtor da classe Personagem
    def __init__(self, initialPosition, walkImg_location, walkQtd_spr, walkSize_spr, 
                jumpImg_location, jumpQtd_spr, jumpSize_spr, 
                standImg_Location, standQtd_spr, standSize_spr):

        #chamando o metodo construtor de sprite
        pygame.sprite.Sprite.__init__(self)

        #cria objetos do tipo Sprite_image
        self.walkSprite = Sprite_image.Sprite_image(walkImg_location,walkQtd_spr,walkSize_spr)
        self.jumpSprite = Sprite_image.Sprite_image(jumpImg_location,jumpQtd_spr,jumpSize_spr)
        self.standSprite = Sprite_image.Sprite_image(standImg_Location,standQtd_spr,standSize_spr)

        #Determina o quadro automaticamente sobre a primeira imagem da lista contida na imagem 'walkSprite' (todas as demais, tem o mesmo tamanho de rect)      
        self.rect = pygame.Rect(self.walkSprite.images[0].get_rect())

        #posicionando o rect na posicao xyPosition
        self.rect.topleft = initialPosition 

        #quadro para colisões
        self.collideHead = pygame.Rect((self.rect.left + 25,self.rect.top + 20),(71,55))
        self.collideBody = pygame.Rect((self.rect.left + 36,self.rect.top + 70),(40,65))

        #se self.changex = True: inverte image
        self.changex = False

        self.firstTimeMid = False
        self.firstTimeCollided = False
        self.firstTimeNotCollided = False


        self.passedMov = False

        self.rightCollided = False
        self.leftCollided = False

        #valor para criar um delay para que o usuário possa utilizar alguma funcionalidade
        self.debounce = 0
        #booleano que verifica se o personagem está pulando ou não
        self.jumping = False
        #booleano que verifica se o personagem está parado e de pé
        self.standing = False
        #booleano que diz se o personagem moveu para a direita
        self.movingRight = False
        #booleano que diz se o personagem moveu para a esquerda
        self.movingLeft = False

        self.falling = False

        #velocidade inicial do pulo
        self.v0 = 40
        #valor de gravidade implementado
        self.gravity = 8
        #velocidade do pulo
        self.jspeed = self.v0

        self.currentTime = 0
        self.lastTime = 0
        self.delayRate = 0.048

    #Name Mangling
    def __gravityFunction(self, scenario):

        #velocidade = velocidade + gravidade
        self.jspeed = self.jspeed + self.gravity
        self.rect = self.rect.move((0,self.jspeed))
        #o rect se move self.jspeed posições no eixo y

        self.collideHead = self.collideHead.move((0,self.jspeed))
        self.collideBody = self.collideBody.move((0,self.jspeed))

        if self.jspeed == self.v0 or sprite_utilities.blockCollision(self,scenario):
            #volta o frame para o início
            self.jumpSprite.frame = 0
            #o personagem não está pulando
            self.jumping = False


    #Name Mangling
    def __jumpVerifications(self, keys, scenario):

        #a imagem atual é a contida na posição self.walkSprite.frame
        self.image = self.jumpSprite.images[self.jumpSprite.frame]

        #se a tecla direita for pressionada...
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            #movendo para a direita
            self.movingRight = True

            if (self.rect.right < 461 or scenario.rightFree == True) and (self.rect.right != 801) and not self.passedMov and not self.rightCollided:
                
                if self.rect.right + self.movSpeed == 461:
                    self.firstTimeMid = True

                #self.rect se move self.movSpeed posições para frente
                self.rect = self.rect.move((self.movSpeed,0))
                self.collideHead = self.collideHead.move((self.movSpeed,0))
                self.collideBody = self.collideBody.move((self.movSpeed,0))

            elif self.movingRight and (self.rect.right != 801) and not self.passedMov and not self.rightCollided:

                self.collideHead = self.collideHead.move((10,0))
                self.collideBody = self.collideBody.move((10,0))
            #nao inverter
            self.changex = False

        #se a tecla esquerda for pressionada...
        elif keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            #movendo para a esquerda
            self.movingLeft = True

            if (self.rect.right > 461 or scenario.leftFree == True) and (self.rect.left != 0) and not self.passedMov and not self.leftCollided:

                if self.rect.right - self.movSpeed == 461:
                    self.firstTimeMid = True

                #self.rect se move self.movSpeed posições para frente
                self.rect = self.rect.move((-self.movSpeed,0))
                self.collideHead = self.collideHead.move((-self.movSpeed,0))
                self.collideBody = self.collideBody.move((-self.movSpeed,0))

            elif self.movingLeft and (self.rect.left != 0) and not self.passedMov and not self.leftCollided:

                self.collideHead = self.collideHead.move((-10,0))
                self.collideBody = self.collideBody.move((-10,0))

            #inverter imagem
            self.changex = True

        if sprite_utilities.lockCollision(self,scenario) or sprite_utilities.wallCollision(self, scenario):

            if not self.rightCollided and not self.leftCollided:
                self.firstTimeCollided = True

            if self.movingRight:
                self.rightCollided = True
                self.leftCollided = False
            elif self.movingLeft:
                self.leftCollided = True
                self.rightCollided = False
        else:

            if (self.rightCollided or self.leftCollided) and self.movingRight:

                self.firstTimeNotCollided = True

            self.rightCollided = False
            self.leftCollided = False

        #se o frame atual do jumpSprite não for o último
        if self.jumpSprite.frame < self.jumpSprite.total_frames:
            #próximo frame
            self.jumpSprite.frame = self.jumpSprite.frame + 1

        #se o frame atual for o último
        if self.jumpSprite.frame == self.jumpSprite.total_frames:
            
            if self.up == True:

                #se a velocidade do pulo for igual a 0
                if self.jspeed == 0:
                    #personagem caindo
                    self.up = False

                #o rect se move -self.jspeed posições no eixo y
                self.rect = self.rect.move((0,-self.jspeed))

                self.collideHead = self.collideHead.move((0,-self.jspeed))
                self.collideBody = self.collideBody.move((0,-self.jspeed))

                #velocidade = velocidade - gravidade
                self.jspeed = self.jspeed - self.gravity
            else:
                #aplica a gravidade no pulo do personagem
                self.__gravityFunction(scenario)

    #Name Mangling
    def __moveVerifications(self, keys, scenario):

        self.passedMov = True

        #se a tecla direita for pressionada e a esquerda nao estiver pressionada...
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            #movendo para a direita
            self.movingRight = True
            #o personagem não está parado
            self.standing = False

            if self.currentTime - self.lastTime >= self.delayRate:
                #vetor circular
                self.walkSprite.frame = (self.walkSprite.frame + 1)%self.walkSprite.total_frames
                self.lastTime = self.currentTime

            #nao inverter
            self.changex = False

        #se a tecla esquerda for pressionada e a direita nao estiver pressionada...
        elif keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            #movendo para a esquerda
            self.movingLeft = True
            #o personagem não está parado
            self.standing = False

            if self.currentTime - self.lastTime >= self.delayRate:
                #vetor circular
                self.walkSprite.frame = (self.walkSprite.frame + 1)%self.walkSprite.total_frames
                self.lastTime = self.currentTime

            #inverter imagem
            self.changex = True

        else: #se a tecla direita ou esquerda nao for pressionada ou se ambas estiverem pressionadas simultaneamente..
            if self.standing == True:

                if self.currentTime - self.lastTime >= self.delayRate:
                    #vetor circular
                    self.standSprite.frame = (self.standSprite.frame + 1)%self.standSprite.total_frames
                    self.lastTime = self.currentTime
            else:
                #frame do walkSprite será o primeiro
                self.walkSprite.frame = 0
                #o personagem está parado
                self.standing = True
                #frame será o primeiro
                self.standSprite.frame = 0
                #aux = tupla da localização atual do rect
                aux = self.rect.topleft
                #rect = rect da imagem do vetor de imagens na posição 0
                self.rect = pygame.Rect(self.standSprite.images[0].get_rect())
                #tupla da localização atual = aux
                self.rect.topleft = aux

        #se o personagem está parado
        if self.standing == True:
            #a imagem exibida será a imagem contida na posição self.walkSprite.frame do vetor de imagens
            self.image = self.standSprite.images[self.standSprite.frame]
        else:
            #a imagem exibida será a imagem contida na posição self.walkSprite.frame do vetor de imagens
            self.image = self.walkSprite.images[self.walkSprite.frame] 

        #se a tecla direcional para cima for pressionada
        if keys[pygame.K_UP]:
            #se o delay debounce atual for 0...
            if self.debounce == 0:
                #o frame do walkSprite será o primeiro
                self.walkSprite.frame = 0
                #o personagem está pulando!
                self.jumping = True
                #o personagem não está parado
                self.standing = False
                #valor booleano utilizado para a verificação do estado do pulo (True == Subindo)
                self.up = True
                #aux = tupla da localização atual do rect
                aux = self.rect.topleft
                #rect = rect da imagem do vetor de imagens na posição 0
                self.rect = pygame.Rect(self.jumpSprite.images[0].get_rect())
                #tupla da localização atual = aux
                self.rect.topleft = aux
            else:
                #subtrai debounce
                self.debounce = self.debounce - 1

        if(self.rect.right < 461 or scenario.rightFree) and self.movingRight and (self.rect.right != 801) and not self.rightCollided:

            if self.rect.right + self.movSpeed == 461:
                self.firstTimeMid = True

            self.rect = self.rect.move((self.movSpeed,0))
            self.collideHead = self.collideHead.move((self.movSpeed,0))
            self.collideBody = self.collideBody.move((self.movSpeed,0))


        elif self.movingRight and (self.rect.right != 801) and not self.rightCollided:
            self.collideHead = self.collideHead.move((10,0))
            self.collideBody = self.collideBody.move((10,0))


        if(self.rect.right > 461 or scenario.leftFree) and self.movingLeft and (self.rect.left != 0) and not self.leftCollided:

            if self.rect.right - self.movSpeed == 461:
                self.firstTimeMid = True

            self.rect = self.rect.move((-self.movSpeed,0))
            self.collideHead = self.collideHead.move((-self.movSpeed,0))
            self.collideBody = self.collideBody.move((-self.movSpeed,0))

        elif self.movingLeft and (self.rect.left != 0) and not self.leftCollided:
            self.collideHead = self.collideHead.move((-10,0))
            self.collideBody = self.collideBody.move((-10,0))

        if sprite_utilities.lockCollision(self,scenario) or sprite_utilities.wallCollision(self, scenario):

            if not self.rightCollided and not self.leftCollided:
                self.firstTimeCollided = True

            if self.movingRight:
                self.rightCollided = True
                self.leftCollided = False
            elif self.movingLeft:
                self.leftCollided = True
                self.rightCollided = False
        else:

            if (self.rightCollided or self.leftCollided) and self.movingRight:

                self.firstTimeNotCollided = True

            self.rightCollided = False
            self.leftCollided = False

    #atualizará o estado do personagem baseado nas teclas pressionadas
    def update(self, scenario):

        #o personagem não está movendo para a direita
        self.movingRight = False
        #o personagem não está movendo para a esquerda
        self.movingLeft = False

        self.passedMov = False

        self.currentTime = time.clock()

        #retorna um vetor de valores booleanos baseados no estado das teclas do teclado
        keys = pygame.key.get_pressed()

        #se o personagem não estiver pulando
        if self.jumping == False and not sprite_utilities.anyDoorInside(scenario):
            #verificações de movimento normal
            self.__moveVerifications(keys, scenario)
        #se o personagem estiver pulando
        if self.jumping == True and not sprite_utilities.anyDoorInside(scenario):
            #verificações de pulo
            self.__jumpVerifications(keys, scenario)

        #inverter imagem
        if self.changex == True:
            #inverter a imagem em relação ao eixo y
            self.image = pygame.transform.flip(self.image,self.changex,False)
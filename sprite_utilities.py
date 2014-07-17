import pygame
from pygame import *

def load_sprite(img_location, quantity, size):
    
    #tramento de excecao, tenta fazer este bloco, caso algo saia errado
    try:

        #carrega a imagem no caminho especificado
        imagem = pygame.image.load(img_location)
        #se ela nao tiver, converta a imagem normalmente
        imagem = imagem.convert() 
        #o metodo para superficies get_at(posicao), retorna a referencia de cor do pixel na posicao
        imagem.set_colorkey(imagem.get_at((0,0)))

        #cria moldura na posicao do tamanho do personagem na posicao (0,0)
        rect = pygame.Rect((0,0),size) 
        #inicializa uma variavel com lista vazia
        imagens = []
        for i in range(quantity):
            imagens.append(
                imagem.subsurface(
                    rect.move(i*size[0],0)))

        #retorno da lista de imagens da qual imagens = [imagem1, imagem2, ... , imagem9]
        return imagens

    #tratamento de excessao mostra a mensagem de erro gerada pelo proprio pygame
    except pygame.error as mensagem:
        
        print(mensagem)
        return None

def getRect(x):

    return x.rect

def blockCollision(personagem, scenario):

    if personagem.collideHead.collidelist(list(map(getRect,scenario.blockGroup.sprites()))) > -1:
        return True
    elif personagem.collideBody.collidelist(list(map(getRect,scenario.blockGroup.sprites()))) > -1:
        return True
    else:
        return False

def lockCollision(personagem, scenario):

    if (personagem.collideHead.colliderect(scenario.lockSystem1.lockGate.southCollideRect)) or (personagem.collideHead.colliderect(scenario.lockSystem1.lockGate.northCollideRect)):
        return 1
    elif (personagem.collideBody.colliderect(scenario.lockSystem1.lockGate.southCollideRect)) or (personagem.collideBody.colliderect(scenario.lockSystem1.lockGate.northCollideRect)):
        return 1

    elif (personagem.collideHead.colliderect(scenario.lockSystem2.lockGate.southCollideRect)) or (personagem.collideHead.colliderect(scenario.lockSystem2.lockGate.northCollideRect)):
        return 2
    elif (personagem.collideBody.colliderect(scenario.lockSystem2.lockGate.southCollideRect)) or (personagem.collideBody.colliderect(scenario.lockSystem2.lockGate.northCollideRect)):
        return 2  

    elif (personagem.collideHead.colliderect(scenario.lockSystem3.lockGate.southCollideRect)) or (personagem.collideHead.colliderect(scenario.lockSystem3.lockGate.northCollideRect)):
        return 3
    elif (personagem.collideBody.colliderect(scenario.lockSystem3.lockGate.southCollideRect)) or (personagem.collideBody.colliderect(scenario.lockSystem3.lockGate.northCollideRect)):
        return 3

    else:
        return 0

def wallCollision(personagem, scenario):

    if (personagem.collideHead.colliderect(scenario.collideWall1)) or (personagem.collideBody.colliderect(scenario.collideWall1)):
        return 1

    elif (personagem.collideHead.colliderect(scenario.collideWall2)) or (personagem.collideBody.colliderect(scenario.collideWall2)):
        return 2  

    elif (personagem.collideHead.colliderect(scenario.collideWall3)) or (personagem.collideBody.colliderect(scenario.collideWall3)):
        return 3

    else:
        return 0

def anyDoorInside(scenario):

    lista = scenario.doorGroup.sprites()

    for i in range(len(lista)):
        if lista[i].inside:
            return True

    return False


















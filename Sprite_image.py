import pygame
import sprite_utilities

from pygame import *

class Sprite_image:

	#método construtor
	def __init__(self, Img_location, Qtd_spr, Size_spr):	

		#carrega a variável self.images com um vetor de imagens
		self.images = sprite_utilities.load_sprite(Img_location, Qtd_spr, Size_spr)
		#total_frames controla o indice final da lista de imagens que vai da posicao 0 ate 8, para quando ha 9 imagens
		self.total_frames = (Qtd_spr-1)
		#controla o indice atual da lista de imagens, este ira variar de 0 a 8
		self.frame = 0
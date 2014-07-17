import pygame
import time
import LockGate
import LockTerminal
from pygame import *
from time import clock

class LockSystem():

	def __init__(self, lockGatePos1, lockGatePos2, lockTerminalPos, ID):

		self.lockGate = LockGate.LockGate(lockGatePos1, lockGatePos2, ID)
		self.lockTerminal = LockTerminal.LockTerminal(lockTerminalPos)

	def update(self, personagem, scenario):

		self.lockTerminal.update(personagem)

		self.lockGate.update(self.lockTerminal.openBool, clock(), scenario)


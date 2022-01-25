from random import randint
from math import floor

class Pokemon:
	def __init__(self, name, type, hp = 20, lvl = 1, xp = 0):
		self.name = name
		self.type = type
		self.hp = hp
		self.lvl = lvl
		self.xp = xp
	
	# Damage = current level * 1.5 + random number; round down
	def attack(self):
		return floor(self.lvl * 1.5 + randint(2, 5))

	def rest(self):
		self.hp += randint(2, 4)
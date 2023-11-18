class Player():
	def __init__(self, name):
		self.name = name
		self.air = 100
		self.health = 100
		self.inventory = []
		self.money = 50
		self.protez = 100
	def death(self, progress):
		print(50 - progress, '[СМЕРТЬ] - В глазах темнеет... Кажется это конец...')
		input('Новая игра - enter')
	def inv(self):
		print('Ваш инвентарь: ', '\n'.join(self.inventory))
import random as rand

class NPC():

	def __init__(self, name, aggressive = False, products = [], money = 0, health = 100, weapons = ['кулак']):
		self.name = name
		self.health = health
		self.weapons = weapons
		self.money = money
		self.products = products
		self.aggressive = aggressive

	def meeting(self):
		print(f'[ВСТРЕЧА] - кажется это {self.name}')
		choice = None
		while choice != '':
			choice = input('Что собираешься делать?\n enter - уйти\n t -  торговаться\n a - напасть')
			if choice == '':
				print('Ты уходишь')
				break
			elif choice == 'a' or choice == 'а':
				self.fight()
			elif choice == 't':
				print('вы поторговались')
				#self.trade(player)

	def fight(self, player):
		global all_weapons
		enemy_weapon = self.weapons[0]
		player_weapon = player.weapons[0]
		turn = True
		health = self.health
		print('--------БОЙ--------')
		print(f'{self.name} готовит {enemy_weapon[0]} для атаки...')
		while health > 0:
			if turn:
				choice = input(f'\nЧто собираешься делать? \n атака({player.weapons[0][0]}) - enter\n')
				if choice == '':
					damage = [int(player_weapon[1] * (0.5 + rand.random())) for _ in range(player_weapon[2])]
					health -= sum(damage)
					#print(f'нанесено {' + '.join(map(str, damage)} урона')
					print(f'{self.name} имеет {max(0, health)} здоровья')
			else:
				print(f'\n{self.name} атакует!')
				damage = [int(enemy_weapon[1] * (0.5 + rand.random())) for _ in range(enemy_weapon[2])]
				#print(f'нанесено {' + '.join(map(str, damage))} урона')
				player.health -= sum(damage)
				if player.health > 0:
					print('ваше здоровье -', player.health)
				else:
					print('ваше здоровье -', 0)
					player.death()
			turn = not turn
		else:
			print(self.name, f'погибает, вы получаете {round(self.money * (0.5 + rand.random()), 2)}$')


import random as rand
import time

class NPC():

	def __init__(self, name, aggressive = False, products = [], money = 0, health = 100, weapons = ['кулак'], dialogue = {}):
		self.name = name
		self.health = health
		self.weapons = weapons
		self.money = money
		self.products = products
		self.aggressive = aggressive
		self.dmgtype = 'кровотечение'
		self.dialogue = dialogue

	def meeting(self):
		print(f'[ВСТРЕЧА] - кажется это {self.name}')
		choice = None
		while choice != '':
			choice = input('Что собираешься делать?\n enter - уйти\n 1 -  торговаться\n 2 - говорить')
			if choice == '':
				print('Ты уходишь')
				break
			elif choice == '1':
				self.trade()
			elif choice == '2':
				if self.dialogue == {}:
					print(f'Похоже {self.name} не в настроении говорить')
				else:
					phrases = list(self.dialogue.keys()) #фразы которые можно сказать
					for i in range(len(phrases)):
						print(f'{i + 1} - "{phrases[i]}"') # номер фразы, фраза
					choice = input('>>>')
					print(f'{self.name}: "{self.dialogue.get(phrases[int(choice) - 1])}"')



	def fight(self, player):
		enemy_weapon = self.weapons[0]
		player_weapon = player.weapons[0]
		turn = True
		health = self.health
		period_dmg = 3
		period_dmg_counter = 0
		block = 1
		print('--------БОЙ--------')
		time.sleep(1)
		print(f'{self.name} готовит {enemy_weapon[0]} для атаки...')
		while health > 0:
			if turn:
				choice = list(input(f'\nЧто собираешься делать?(выбери два действия) \n атака({player.weapons[0][0]}) - a\n блок(50%) - b\n лечение(бинты) - h\n'))
				if len(choice) == 2:
					for i in range(2):	
						if choice[i] == 'a':
							damage = [int(player_weapon[1] * (0.5 + rand.random())* block) for _ in range(player_weapon[2])]
							health -= sum(damage)
							print(f'нанесено {' + '.join(map(str, damage))}')
							print(f'{self.name} имеет {max(0, health)} здоровья\n')
							time.sleep(1)
							if self.dmgtype == player.weapons[0][4] and rand.random() > 0.6:
								period_dmg_counter = 3
							if self.dmgtype == player.weapons[0][4] and period_dmg_counter != 0:
								health -= period_dmg
								print(f'вы наложили статус: {player.weapons[0][4]}, периодический урон - 3\n осталось этапов - {period_dmg_counter}')
								print(f'{self.name} имеет {max(0, health)} здоровья')
								period_dmg_counter -= 1
						
						if choice[i] == 'b':
							block = block * 0.5
							print('вы подготовили блок на следующую атаку противника!\n')
						
						if choice[i] == 'h':
							player.health = min(100, player.health + 25)
							print(f'вы успешно воостановили здоровье. ХП = {player.health}\n')
				else:
					print('нужно сделать два действия за ход')
			else:
				time.sleep(1)
				print(f'\n{self.name} атакует!')
				time.sleep(1)
				damage = [int(enemy_weapon[1] * (0.5 + rand.random()) * block) for _ in range(enemy_weapon[2])]
				print(f'нанесено {' + '.join(map(str, damage))} урона')
				player.health -= sum(damage)
				block = 1
				if player.health > 0:
					print('ваше здоровье -', player.health)
				else:
					print('ваше здоровье -', 0)
					player.death(0)
			turn = not turn
		else:
			time.sleep(1)
			mny = round(self.money * (0.5 + rand.random()), 2)
			print(self.name, f'погибает, вы получаете {mny}$')
			player.money += mny
	
	def trade(self):
		products = self.products
		if products == []:
			print(f'Кажется {self.name} не в настроении торговать')
			return
		print(f'{self.name} показывает свои товары')
		product = None
		while len(self.products) != 0:
			for index in range(len(products)):
				print(f'{index + 1} {products[index][0]} - {products[index][-1]}$')
			product = input(' введите номер товара\n enter - конец торговли\n')
			if product == '':
				break
			elif products[int(product) - 1][-1] <= self.player.money:
				self.player.money -= products[int(product) - 1][-1]
				self.player.inventory.append(products[int(product) - 1])
				print(f'Вы купили {products.pop(int(product) - 1)[0]}')
				print(f'Ваш баланс: {self.player.money}')
			else:
				print('вы не прошли проверку от дурака')


import json
import sys
from items_database import items
class Player():
		def __init__(self, name):
				self.name = name
				self.air = 100
				self.health = 100
				self.inventory = [['ингалятор', 'air', 25, 30]]
				self.money = 50
				self.protez = 100
				self.weapons = [['микроволновая п-ушка', 15, 1, 300, 'сбои'],['ПМ', 10, 4, 600, 'повреждение']]
				#self.things = {"Аптечка": 12, 10, 'resource', "фильтр для протеза": 100, 20, 'resource', 'арматура': 20, 30, 'weapon', 'бита': 15, 20, 'weapon', 'арбалет': 35, 50, 'weapon','одежда лоха': 30, 40, 'armour', 'кольчуга столяра': 50, 60, 'armour', 'броня ученого', 80, 100, 'armour'}

		def death(self, progress):
				print(f'{50 - progress}km [СМЕРТЬ] - В глазах темнеет... Кажется это конец...')
				sys.exit("Вы умерли")
				

		def inv(self):
				print('Ваш инвентарь: ', self.inventory)

		def use_item(self):
			item_params = [0, 1, 2]
			if len(self.inventory) == 0:
				print("В вашем инвентаре нет вещей!")
				return
			print("ваш инвентарь:")
			for i in range(len(self.inventory)):
				print(f'{i + 1} - {self.inventory[i][0]}')
			choice = input("выберите номер предмета в инвентаре, enter - выйти")
			inp = None
			while choice != '':
				inp = int(choice)
				if inp > len(self.inventory) or inp <= 0:
					print('Такого элемента в инвентаре нету!')
					break
				else:
					use_thing = self.inventory[inp-1][0]
					item_params = items.get(use_thing)
					s = f"self.{item_params[1]} += {item_params[2]}"
					exec(s)
					print(f'вы пополнили {item_params[1]}')
					self.inventory.pop(inp-1)
					choice = ''


		def save_to_file(self, filename):
				data = {
						"name": self.name,
						"air": self.air,
						"health": self.health,
						"inventory": self.inventory,
						"money": self.money,
						"protez": self.protez,
						"weapons": self.weapons
				}

				with open(filename, "w") as file:
						json.dump(data, file)

				print("Переменные игрока сохранены в файле", filename)

		@staticmethod
		def load_from_file(filename):
				with open(filename, "r") as file:
						data = json.load(file)

				player = Player(data["name"])
				player.air = data["air"]
				player.health = data["health"]
				player.inventory = data["inventory"]
				player.money = data["money"]
				player.protez = data["protez"]
				player.weapons = data["weapons"]

				print("Переменные игрока успешно загружены из файла", filename)
				return player

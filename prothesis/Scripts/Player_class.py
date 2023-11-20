import json
import sys
from items_database import items
class Player():
		def __init__(self, name):
				self.name = name
				self.air = 100
				self.health = 100
				self.inventory = []
				self.money = 50
				self.protez = 100
				self.weapons = [['микроволновая п-ушка', 15, 1, 300, 'сбои']]
				#self.things = {"Аптечка": 12, 10, 'resource', "фильтр для протеза": 100, 20, 'resource', 'арматура': 20, 30, 'weapon', 'бита': 15, 20, 'weapon', 'арбалет': 35, 50, 'weapon','одежда лоха': 30, 40, 'armour', 'кольчуга столяра': 50, 60, 'armour', 'броня ученого', 80, 100, 'armour'}

		def death(self, progress):
				print(f'{50 - progress}km [СМЕРТЬ] - В глазах темнеет... Кажется это конец...')
				sys.exit("Вы умерли")
				

		def inv(self):
				print('Ваш инвентарь: ', self.inventory)

		def use_item(self):
			if len(self.inventory) == 0:
				print("В вашем инвентаре нет вещей!")
				return
			print("ваш инвентарь:")
			for i in range(1, len(self.inventory) + 1):
				print(f'{i} - {self.inventory[i - 1]}')
			inp = int(input("выберите номер предмета в инвентаре, enter - выйти"))
			while inp != '':
				if inp > len(self.inventory) or inp <= 0:
					print('Такого элемента в инвентаре нету!')
					break
				else:
					use_thing = self.inventory[inp-1]
					for i in range(len(items.keys())):
						if list(items.keys())[i] == use_thing:
							item_params = list(items.get(list(items.keys())[i]))
					eval(f'self.{item_params[0]} += {item_params[1]}')


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

player = Player("Имя игрока")
player.save_to_file("player_data.json")
loaded_player = Player.load_from_file("player_data.json")
import random as rand
import time
from prothesis._databases.items_database import all_weapons
from prothesis._databases.items_database import items
from prothesis.model.weapon_class import Weapon
from prothesis.model.players.player_info import PlayerInfo
from prothesis.view.player_view import PlayerView
class NPC():

    def __init__(self, name, aggressive = False, products = [], money = 0, health = 100, weapons = [all_weapons['кулак']], dialogue = {}, texture=None):
        self.name = name
        self.health = health
        self.weapons = weapons
        self.money = money
        self.products = products
        self.aggressive = aggressive
        self.dmgtype = 'кровотечение'
        self.dialogue = dialogue
        self.player_view = None
        self.player_info = None
        self.texture = texture

	
    def meeting(self, player_view: PlayerView, player_info: PlayerInfo):
        self.player_view = player_view
        self.player_info = player_info
        self.player_view.send_response_to_player(f'[ВСТРЕЧА] - кажется это {self.name}')
        if self.texture != None:
            self.player_view.send_photo(self.texture)
        choice = None
        while choice != '1':
            choice = self.player_view.get_request_from_player('Что собираешься делать?', ['уйти', 'торговаться', 'говорить', 'напасть'])
            if choice == '1':
                self.leave()
            elif choice == '2':
                self.trade(player_info)
            elif choice == '3':
                if self.dialogue == {}:
                    self.player_view.send_response_to_player(f'Похоже {self.name} не в настроении говорить')
                else:
                    choice1 = self.player_view.get_request_from_player('Выберете фразу:', list(self.dialogue.keys()))
                    self.player_view.send_response_to_player(f'{self.name}: "{self.dialogue.get(list(self.dialogue.keys())[int(choice1) - 1])}"')
            elif choice == '4':
                self.fight()
                choice = '1'

    def fight(self):
        
        enemy_weapon = self.weapons[0]  
        player_weapon = self.player_info.weapons[0]
        turn = True
        health = self.health
        period_dmg = 3
        period_dmg_counter = 0
        block = 1
        change_weapon = int(self.player_view.get_request_from_player('желаете сменить оружее?', [self.player_info.weapons[i].name for i in range(len(self.player_info.weapons))]))
        player_weapon = self.player_info.weapons[change_weapon - 1]
        self.player_view.send_response_to_player('--------БОЙ--------')
        time.sleep(1)
        self.player_view.send_response_to_player(f'{self.name} готовит {enemy_weapon.name} для атаки...')
        while health > 0:
            if turn:
                choice = []
                choice1 = self.player_view.get_request_from_player(
                        f'\nЧто собираешься делать?(выбери первое действие)',
                        [f'атака({player_weapon.name})', 'блок(50%)', 'лечение'],
                        test=False
                    )
                choice2 = self.player_view.get_request_from_player(
                        f'\nЧто собираешься делать?(выбери второе действие)',
                        [f'атака({player_weapon.name})', 'блок(50%)', 'лечение'],
                        test=False
                    )
                choice.append(choice1)
                choice.append(choice2)
                if len(choice) == 2:
                    for i in range(2):
                        if choice[i] == '1':
                            damage = [
                                int(player_weapon.damage * (0.5 + rand.random()) *
                                    block) for _ in range(player_weapon.attacks)
                            ]
                            health -= sum(damage)
                            self.player_view.send_response_to_player(f'нанесено {" + ".join(map(str, damage))}')
                            self.player_view.send_response_to_player(
                                f'{self.name} имеет {max(0, health)} здоровья\n'
                            )
                            time.sleep(1)
                            if self.dmgtype == player_weapon.damage_type and rand.random() > 0.6:
                                period_dmg_counter = 3
                            if self.dmgtype == player_weapon.damage_type and period_dmg_counter != 0:
                                health -= period_dmg
                                self.player_view.send_response_to_player(
                                    f'вы наложили статус: {player_weapon.damage_type}, периодический урон - 3\n осталось этапов - {period_dmg_counter}'
                                )
                                self.player_view.send_response_to_player(
                                    f'{self.name} имеет {max(0, health)} здоровья'
                                )
                                period_dmg_counter -= 1

                        if choice[i] == '2':
                            block = block * 0.5
                            self.player_view.send_response_to_player(
                                'вы подготовили блок на следующую атаку противника!\n'
                            )

                        if choice[i] == '3':
                            if self.player_info.inventory == [] or self.player_info.inventory[0] == []:
                                self.player_view.send_response_to_player(f'Ваш инвентарь пуст.')
                            else:
                                x = []
                                for i in self.player_info.inventory:
                                    x.append(f"{self.player_info.inventory.index(i) + 1}: {i.name} {i.type} {i.value}")
                                self.player_view.send_response_to_player(f'Ваш запас воздуха: {self.player_info.air}%')
                                self.player_view.send_response_to_player(f'Ваш инвентарь:')
                                choice = self.player_view.get_request_from_player('Cделайте выбор:', x)
                                y = x[int(choice)-1]
                                type = y.split(" ")[2]
                                value = y.split(" ")[3]
                                self.player_info.inventory.pop(int(y[0])-1)
                                if type == 'Air' or type == 'air' :
                                    self.player_info.air += int(value)
                                else:
                                    self.player_info.health += int(value)
                                self.player_view.send_response_to_player(f'Ваш запас воздуха: {self.player_info.air}%')
                                self.player_view.send_response_to_player(f'Ваше здоровье: {self.player_info.health}')                    
            else:
                time.sleep(1)
                self.player_view.send_response_to_player(f'\n{self.name} атакует!')
                time.sleep(1)
                damage = [
                    int(enemy_weapon.damage * (0.5 + rand.random()) * block)
                    for _ in range(enemy_weapon.attacks)
                ]
                self.player_view.send_response_to_player(f'нанесено {" + ".join(map(str, damage))} урона')
                self.player_info.health -= sum(damage)
                block = 1
                if self.player_info.health > 0:
                    self.player_view.send_response_to_player(f'ваше здоровье - {self.player_info.health}')
                else:
                    self.player_view.send_response_to_player('ваше здоровье - 0')
            turn = not turn
        else:
            time.sleep(1)
            mny = round(self.money * (0.5 + rand.random()), 2)
            self.player_view.send_response_to_player(f'{self.name}, погибает, вы получаете {mny}$')
            self.player_info.money += mny
            if len(self.products) != 0:
                self.player_view.send_response_to_player('также вы подбираете предметы что уцелели после вашей атаки')
                rnd_product = rand.choice(self.products)
                if rnd_product.cls == 'item':
                    self.player_info.inventory.append(rnd_product)
                else:
                    self.player_info.weapons.append(rnd_product)
            self.leave()
	
    def trade(self, player_info):
        products = self.products
        if products == []:
            self.player_view.send_response_to_player(f'Кажется {self.name} не в настроении торговать')
            return
        self.player_view.send_response_to_player(f'{self.name} показывает свои товары')
        self.player_view.send_response_to_player(f'ваш баланс {player_info.money}')
        product = None
        while len(self.products) != 0 and product != '':
            for index in range(len(products)):
                self.player_view.send_response_to_player(f'{products[index].name} - {products[index].price}k')
            variants = [self.products[index].name for index in range(len(self.products))]
            variants.append('конец торговли')
            product = self.player_view.get_request_from_player('Что желаете приобрести?', variants)
            print(product)
            if product == str(len(self.products) + 1):
                break
            elif products[int(product) - 1].price <= player_info.money:
                print("я тут")
                if products[int(product)-1].cls == 'item':
                    player_info.money -= products[int(product) - 1].price
                    player_info.inventory.append(products[int(product) - 1])
                    self.player_view.send_response_to_player(f'Вы купили {self.products.pop(int(product) - 1).name}')
                    self.player_view.send_response_to_player(f'Ваш баланс: {player_info.money}')
                    product = ''
                elif products[int(product)-1].cls == 'weapon':
                    player_info.money -= products[int(product) - 1].price
                    player_info.weapons.append(products[int(product) - 1])
                    self.player_view.send_response_to_player(f'Вы купили {self.products.pop(int(product) - 1).name}')
                    self.player_view.send_response_to_player(f'Ваш баланс: {player_info.money}')
                    product = ''
            else:
                self.player_view.send_response_to_player('недостаточно денег')
    
    def leave(self):
        self.player_view.send_response_to_player('Ты уходишь')



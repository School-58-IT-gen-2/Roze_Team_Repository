import random as rand
import time
from typing import Self
from prothesis._databases.items_database import all_weapons
from prothesis._databases.items_database import items
from prothesis.model.players.player_info import PlayerInfo
from prothesis.view.player_view import PlayerView

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
        self.player_view = PlayerView()
        self.player_info = PlayerInfo()

	
    def meeting(self, player_view, player_info):
        self.player_view = player_view
        self.player_info = player_info
        print(f'[ВСТРЕЧА] - кажется это {self.name}')
        choice = None
        while choice != '':
            choice = self.player_view.get_request_from_player('Что собираешься делать?', ['уйти', 'торговаться', 'говорить'])
            if choice == '1':
                print('Ты уходишь')
                break
            elif choice == '2':
                self.trade(player_info)
            elif choice == '3':
                if self.dialogue == {}:
                    print(f'Похоже {self.name} не в настроении говорить')
                else:
                    phrases = list(self.dialogue.keys()) #фразы которые можно сказать
                    for i in range(len(phrases)):
                        print(f'{i + 1} - "{phrases[i]}"') # номер фразы, фраза
                    choice = input('>>>')
                    print(f'{self.name}: "{self.dialogue.get(phrases[int(choice) - 1])}"')

    def fight(self):
        enemy_weapon = self.weapons
        player_weapon = self.player_info.weapons[0]
        turn = True
        health = self.health
        period_dmg = 3
        period_dmg_counter = 0
        block = 1
        change_weapon = int(self.player_view.get_request_from_player('желаете сменить оружее?', [self.player_info.weapons[i][0] for i in range(len(self.player_info.weapons))]))
        player_weapon = self.player_info.weapons[change_weapon - 1]
        self.player_view.send_response_to_player('--------БОЙ--------')
        time.sleep(1)
        self.player_view.send_response_to_player(f'{self.name} готовит {enemy_weapon[0]} для атаки...')
        while health > 0:
            if turn:
                choice = list(
                    self.player_view.get_request_from_player(
                        f'\nЧто собираешься делать?(выбери два действия)',
                        [f'атака({player_weapon[0]})', 'блок(50%)', 'лечение(бинты)'],
                        test=False
                    ))
                if len(choice) == 2:
                    for i in range(2):
                        if choice[i] == '1':
                            damage = [
                                int(player_weapon[1] * (0.5 + rand.random()) *
                                    block) for _ in range(player_weapon[2])
                            ]
                            health -= sum(damage)
                            self.player_view.send_response_to_player(f'нанесено {' + '.join(map(str, damage))}')
                            self.player_view.send_response_to_player(
                                f'{self.name} имеет {max(0, health)} здоровья\n'
                            )
                            time.sleep(1)
                            if self.dmgtype == player_weapon[
                                    4] and rand.random() > 0.6:
                                period_dmg_counter = 3
                            if self.dmgtype == player_weapon[
                                    4] and period_dmg_counter != 0:
                                health -= period_dmg
                                self.player_view.send_response_to_player(
                                    f'вы наложили статус: {player_weapon[4]}, периодический урон - 3\n осталось этапов - {period_dmg_counter}'
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
                            self.player_info.health = min(100, self.player_info.health + 25)
                            self.player_view.send_response_to_player(
                                f'вы успешно воостановили здоровье. ХП = {self.player_info.health}\n'
                            )
            else:
                time.sleep(1)
                self.player_view.send_response_to_player(f'\n{self.name} атакует!')
                time.sleep(1)
                damage = [
                    int(enemy_weapon[1] * (0.5 + rand.random()) * block)
                    for _ in range(enemy_weapon[2])
                ]
                self.player_view.send_response_to_player(f'нанесено {' + '.join(map(str, damage))} урона')
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
            self.player_view.send_response_to_player(f'{self.name}, погибает, вы получаете {mny}$ и ингалятор')
            self.player_info.money += mny
            self.player_info.inventory.append(items['ингалятор'])
	
    def trade(self, player_info):
        products = self.products
        if products == []:
            print(f'Кажется {self.name} не в настроении торговать')
            return
        print(f'{self.name} показывает свои товары')
        print(f'ваш баланс {player_info.money}')
        product = None
        while len(self.products) != 0 and product != '':
            for index in range(len(products)):
                print(f'{index + 1} {products[index][0]} - {products[index][-1]}$')
            product = input(' введите номер товара\n enter - конец торговли\n')
            if product == '':
                break
            elif int(product) > len(products)+1:
                print('такого предмета нет')
            elif products[int(product) - 1][-1] <= player_info.money:
                if products[int(product)-1][3] == 'item':
                    player_info.money -= products[int(product) - 1][-1]
                    player_info.inventory.append(products[int(product) - 1])
                    print(f'Вы купили {products.pop(int(product) - 1)[0]}')
                    print(f'Ваш баланс: {player_info.money}')
                    product = ''
                elif products[int(product)-1][3] == 'weapon':
                    player_info.money -= products[int(product) - 1][-1]
                    player_info.weapons.append(products[int(product) - 1])
                    print(f'Вы купили {products.pop(int(product) - 1)[0]}')
                    print(f'Ваш баланс: {player_info.money}')
                    product = ''
                else:
                    print('недостаточно денег')
            else:
                print('вы не прошли проверку от дурака')

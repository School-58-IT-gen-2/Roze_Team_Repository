import time
import random as rand

from prothesis._databases.items_database import all_weapons
from prothesis._databases.items_database import items
from prothesis.model.players.player_info import PlayerInfo
from prothesis.view.player_view import PlayerView
from prothesis.model.item_class import Item
from prothesis.model.weapon_class import Weapon


class Enemy():

    def __init__(self,
                 name,
                 dmgtype,
                 health,
                 weapons,
                 money,
                 loot,
                 aggressive=False):
        
        self.name = name
        self.dmgtype = dmgtype
        self.health = health
        self.weapons = weapons
        self.money = money
        self.loot = loot
        self.aggressive = aggressive
        self.player_view = PlayerView()
        self.player_info = PlayerInfo()

    def meeting(self, player_view, player_info):
        self.player_info = player_info
        self.player_view = player_view
        fght_or_frnd = self.player_view.get_request_from_player(f'перед вами {self.name}, что вы будете делать?',  ['переубеждение', 'сражение', 'побег'])
        if fght_or_frnd == '1':
            self.spare()
        elif fght_or_frnd == '2':
            self.fight()

        elif fght_or_frnd == '3':
            self.escape()

    def fight(self):

        enemy_weapon = self.weapons
        player_weapon = self.player_info.weapons[0]
        turn = True
        health = self.health
        period_dmg = 3
        period_dmg_counter = 0
        block = 1
        x = []
        for i in self.player_info.weapons:
            x.append(f"{self.player_info.weapons.index(i) + 1}: {i.name} {i.damage_type} {i.damage}")
        change_weapon = int(self.player_view.get_request_from_player('желаете сменить оружее?', x))
        player_weapon = self.player_info.weapons[change_weapon - 1]
        self.player_view.send_response_to_player('--------БОЙ--------')
        time.sleep(1)
        self.player_view.send_response_to_player(f'{self.name} готовит {enemy_weapon.name} для атаки...')
        while health > 0:
            if turn:
                choice = []
                choice1 = self.player_view.get_request_from_player(
                        f'\nЧто собираешься делать?(выбери первое действие)',
                        [f'атака({player_weapon.name})', 'блок(50%)', 'лечение(бинты)'],
                        test=False
                    )
                choice2 = self.player_view.get_request_from_player(
                        f'\nЧто собираешься делать?(выбери второе действие)',
                        [f'атака({player_weapon.name})', 'блок(50%)', 'лечение(бинты)'],
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
                            self.player_info.health = min(100, self.player_info.health + 25)
                            self.player_view.send_response_to_player(
                                f'вы успешно воостановили здоровье. ХП = {self.player_info.health}\n'
                            )
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
            self.player_view.send_response_to_player(f'{self.name}, погибает, вы получаете {mny}$ и ингалятор')
            self.player_info.money += mny
            self.player_info.inventory.append(Item(*[1, 'ингалятор', 'air', 'item', 25, 30]))

    def escape(self):
        if rand.randint(1, 2) > 0.5:
            self.player_view.send_response_to_player('Вы успешно сбежали')
        else:
            self.fight()
    
    def spare(self):
        if rand.randint(1, 2) == 1:
            mny = round(self.money * (0.5 + rand.random()), 2)
            self.player_view.send_response_to_player(f'поздравляю, вы успешно закорешились с {self.name}, он поделился с вами {mny}$')
            self.player_info.money += mny
            self.player_view.send_response_to_player(f'ваш баланс: {self.player_info.money}')
        else:
            self.fight()

from Player_class import Player
from items_database import items
from items_database import all_weapons
import time
import random as rand

#сохранение лута


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

    def meeting(self, km, player):
        fght_or_frnd = input(
            f'перед вами {self.name}, что вы будете делать?\n 1. переубеждение\n 2. сражение\n 3. побег\n'
        )
        if fght_or_frnd == '1':
            if rand.random() > 0.5:
                self.spare(player)
            else:
                self.fight(player, km)
        elif fght_or_frnd == '2':
            self.fight(player, km)

        elif fght_or_frnd == '3':
            if rand.random() > 0.5:
                self.run()
            else:
                self.fight(player, km)
        else:
            self.fight(player, km)

    def fight(self, player, km):
        global all_weapons
        enemy_weapon = self.weapons
        player_weapon = player.weapons[0]
        turn = True
        health = self.health
        period_dmg = 3
        period_dmg_counter = 0
        block = 1
        print(f'желаете сменить оружее?')
        for index in range(len(player.weapons)):
            print(f'{index + 1}. {player.weapons[index][0]}')
        change_weapon = int(input())
        player_weapon = player.weapons[change_weapon - 1]
        print('--------БОЙ--------')
        time.sleep(1)
        print(f'{self.name} готовит {enemy_weapon[0]} для атаки...')
        while health > 0:
            if turn:
                choice = list(
                    input(
                        f'\nЧто собираешься делать?(выбери два действия) \n атака({player_weapon[0]}) - a\n блок(50%) - b\n лечение(бинты) - h\n'
                    ))
                if len(choice) == 2:
                    for i in range(2):
                        if choice[i] == 'a':
                            damage = [
                                int(player_weapon[1] * (0.5 + rand.random()) *
                                    block) for _ in range(player_weapon[2])
                            ]
                            health -= sum(damage)
                            print(f'нанесено {' + '.join(map(str, damage))}')
                            print(
                                f'{self.name} имеет {max(0, health)} здоровья\n'
                            )
                            time.sleep(1)
                            if self.dmgtype == player_weapon[
                                    4] and rand.random() > 0.6:
                                period_dmg_counter = 3
                            if self.dmgtype == player_weapon[
                                    4] and period_dmg_counter != 0:
                                health -= period_dmg
                                print(
                                    f'вы наложили статус: {player_weapon[4]}, периодический урон - 3\n осталось этапов - {period_dmg_counter}'
                                )
                                print(
                                    f'{self.name} имеет {max(0, health)} здоровья'
                                )
                                period_dmg_counter -= 1

                        if choice[i] == 'b':
                            block = block * 0.5
                            print(
                                'вы подготовили блок на следующую атаку противника!\n'
                            )

                        if choice[i] == 'h':
                            player.health = min(100, player.health + 25)
                            print(
                                f'вы успешно воостановили здоровье. ХП = {player.health}\n'
                            )
                else:
                    print('нужно сделать два действия за ход')
            else:
                time.sleep(1)
                print(f'\n{self.name} атакует!')
                time.sleep(1)
                damage = [
                    int(enemy_weapon[1] * (0.5 + rand.random()) * block)
                    for _ in range(enemy_weapon[2])
                ]
                print(f'нанесено {' + '.join(map(str, damage))} урона')
                player.health -= sum(damage)
                block = 1
                if player.health > 0:
                    print('ваше здоровье -', player.health)
                else:
                    print('ваше здоровье -', 0)
                    player.death(km)
            turn = not turn
        else:
            time.sleep(1)
            mny = round(self.money * (0.5 + rand.random()), 2)
            print(self.name, f'погибает, вы получаете {mny}$ и ингалятор')
            player.money += mny
            player.inventory.append(items['ингалятор'])

    def spare(self, player):
        mny = round(self.money * (0.5 + rand.random()), 2)
        print(
            f'поздравляю, вы успешно закорешились с {self.name}, он поделился с вами {mny}$'
        )
        player.money += mny
        print(f'ваш баланс: {player.money}')

    def run(self):
        print('вы успешно сбежали')


#Toster = Enemy('хлебоподжариватель', 'сбои', 100, all_weapons['кулак'], 5, 'loot')
#Toster.meeting()

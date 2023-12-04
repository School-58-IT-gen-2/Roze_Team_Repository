import time
import random as rand

from main import player_controller


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

        self.player_controller = player_controller

    def meeting(self, km, player):
        fght_or_frnd = player_controller.__player_view.get_request_from_player(f'перед вами {self.name}, что вы будете делать?',  ['переубеждение', 'сражение', 'побег'])
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
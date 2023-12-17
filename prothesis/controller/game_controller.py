import random as rand
import sys
import json

from prothesis.model.players.player_info import PlayerInfo
from prothesis.model.stages.stage_info import StageInfo
from prothesis.view.player_view import PlayerView
from prothesis._databases.creatures_database import enemies_for_stages
from prothesis._databases.creatures_database import npcs_for_stages


class GameController():

    def __init__(self, player_info: PlayerInfo, stage_info: StageInfo, player_view: PlayerView):
        self.__player_info = player_info
        self.__stage_info = stage_info
        self.player_view = player_view

    def act(self):
        choice = self.player_view.get_request_from_player('выбор действия:', ['идти', 'использовать предмет', 'сохранить прогресс'])
        if choice == '1':  # enter - идти
            self.step()
        elif choice == '2':
            self.show_inventory()
            self.act()
        elif choice == '3':
            self.save_to_file('save_test.json')
            self.act()

    def step(self):
        self.__player_info.km += 1
        self.__player_info.air -= rand.randint(1, 5)
        if self.__player_info.air <= 0:
            self.player_view.send_response_to_player('"Вы судорожно глотаете остатки воздуха..."')
        elif self.__player_info.air < 15:
            self.player_view.send_response_to_player('"!Критически мало воздуха, срочно воспользуйтесь ингалятором"')
        elif self.__player_info.air < 40:
            self.player_view.send_response_to_player('"!Мало воздуха, воспользуйтесь ингалятором"')
        eval(f'self.{self.__stage_info.seed[self.__player_info.km]}()') #происходит то, что на текущей позиции в сиде
        self.act()

    def show_inventory(self):
        self.player_view.send_response_to_player(f'Ваш запас воздуха: {self.__player_info.air}%')
    
    def save_to_file(self, filename):
        data = self.__player_info.get_data()
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
        self.__player_info.set_info(data)

    def void(self):
        self.player_view.way_report(self.__player_info.km, 'ПУСТО', '"кажется здесь пусто"')
        
    def npc(self):
        self.player_view.way_report(self.__player_info.km, 'ВСТРЕЧА', '"кажется кто-то здесь"')
        sage = npcs_for_stages[self.__stage_info.stage_num][0]
        sage.meeting(self.player_view, self.__player_info)

    def trader(self):
        self.player_view.way_report(self.__player_info.km, 'ВСТРЕЧА', '"кажется кто-то здесь"')
        trader = npcs_for_stages[self.__stage_info.stage_num][1]
        trader.meeting(self.player_view, self.__player_info)

    def trader2(self):
        self.player_view.way_report(self.__player_info.km, 'ВСТРЕЧА', '"кажется кто-то здесь"')
        trader2 = npcs_for_stages[self.__stage_info.stage_num][2]
        trader2.meeting(self.player_view, self.__player_info)

    def enemy(self):
        self.player_view.way_report(self.__player_info.km, 'НАПАДЕНИЕ', '"кажется на вас напали!"')
        enemy = rand.choice(enemies_for_stages[self.__stage_info.stage_num])
        enemy.meeting(self.player_view, self.__player_info)

    def event(self):
        self.player_view.way_report(self.__player_info.km, 'СОБЫТИЕ', 'текст события')

    def ending(self):
        self.player_view.way_report(self.__player_info.km, 'КОНЕЦ', '...')

    def start(self):
        self.player_view.way_report(self.__player_info.km, 'НАЧАЛО', self.__stage_info.stage_prologue)

    def death(self):
        self.player_view.way_report(self.__player_info.km, 'СМЕРТЬ', 'В глазах темнеет... Кажется это конец....')
        sys.exit("Вы умерли")

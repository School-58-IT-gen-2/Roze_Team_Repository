import random as rand
import json

from prothesis.model.players.player_info import PlayerInfo
from prothesis.model.stages.stage_info import StageInfo
from prothesis.view.player_view import PlayerView


class GameController():

    def __init__(self, player_info: PlayerInfo, stage_info: StageInfo, player_view: PlayerView):
        self.__player_info = player_info
        self.__stage_info = stage_info
        self.__player_view = player_view
        print(123)

    def act(self):
        choice = self.__player_view.get_request_from_player('выбор действия:', ['идти', 'использовать предмет', 'сохранить прогресс'])
        if choice == '1':  # enter - идти
            self.step()

    def step(self):
        self.__player_info.km += 1
        self.__player_info.air -= rand.randint(1, 8)
        if self.__player_info.air <= 0:
            self.__player_view.send_response_to_player('"Вы судорожно глотаете остатки воздуха..."')
        elif self.__player_info.air < 15:
            self.__player_view.send_response_to_player('"!Критически мало воздуха, срочно воспользуйтесь ингалятором"')
        elif self.__player_info.air < 40:
            self.__player_view.send_response_to_player('"!Мало воздуха, воспользуйтесь ингалятором"')
        eval(f'self.{self.__stage_info.seed[self.__player_info.km]}()') #происходит то, что на текущей позиции в сиде
        self.act()
    
    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump('True', file)

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            data = bool(json.load(file))
        self.__player_info.save = data

    def void(self):
        self.__player_view.way_report(self.__player_info.km, 'ПУСТО', '"кажется здесь пусто"')
        
    def npc(self):
        self.__player_view.way_report(self.__player_info.km, 'ВСТРЕЧА', '"кажется кто-то здесь"')

    def enemy(self):
        self.__player_view.way_report(self.__player_info.km, 'НАПАДЕНИЕ', '"кажется на вас напали!"')

    def event(self):
        self.__player_view.way_report(self.__player_info.km, 'СОБЫТИЕ', 'текст события')

    def ending(self):
        self.__player_view.way_report(self.__player_info.km, 'КОНЕЦ', '...')


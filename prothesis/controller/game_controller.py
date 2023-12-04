import random as rand

from prothesis.model.players.player_info import PlayerInfo
from prothesis.model.stages.stage_info import StageInfo
from prothesis.view.player_view import PlayerView


class GameController():

    def __init__(self, player_info: PlayerInfo, stage_info: StageInfo, player_view: PlayerView):
        self.__player_info = player_info
        self.__stage_info = stage_info
        self.__player_view = player_view
        self.act()

    def act(self):
        choice = input('\nвыбор действия (enter - идти, u - использовать предмет, s - сохранить прогресс)>>> ')
        if choice == '':  # enter - идти
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


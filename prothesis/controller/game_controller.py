import random as rand

from prothesis.model.players.player_info import PlayerInfo
from prothesis.model.stages.stage_info import StageInfo


class GameController():

    def __init__(self, player_info: PlayerInfo, stage_info: StageInfo):
        self.__player_info = player_info
        self.__stage_info = stage_info
        print(f'{self.__stage_info.stage_prologue}\n60km [НАЧАЛО]'
              )  #начальное сообщение
        self.act()

    def act(self):
        choice = input(
            '\nвыбор действия (enter - идти, u - использовать предмет, s - сохранить прогресс)>>> '
        )
        if choice == '':  # enter - идти
            self.void()

    def void(self):
        print(
            f'{60 - self.__player_info.km}km [ПУСТО] - "кажется здесь пусто"')

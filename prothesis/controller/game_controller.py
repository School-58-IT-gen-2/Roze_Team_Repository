import random as rand

from prothesis.model.games.game_info import GameInfo
from prothesis.model.players.player_info import PlayerInfo


class GameController():

    def __init__(self, player_info: PlayerInfo, game_info: GameInfo):
        self.__player_info = player_info
        self.__game_info = game_info
        print('''"вы просыпаетесь посреди пустоты. 
песок, металлические обломки, все это вы 
уже видели однажды. вы чувствуете как горячий воздух наполняет ваше горло...
горло? вы осматриваете себя и замечаете странные трубки в вашей груди и шее.
дотронувшись до лица вы понимаетечто на лице респиратор. кажется вы теперь 
киборг... надо добраться до ближайшего населенного пункта как можно скорее, 
вы чувствуете что ваш кислород на исходе. путешествие начинается."
\n60km [НАЧАЛО]''')  #начальное сообщение
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

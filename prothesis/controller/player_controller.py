import random as rand

from model.players.player_info import PlayerInfo


class PlayerController():

    def __init__(self, player_info:PlayerInfo):
        self.__player_info = player_info
        print(f'"вы просыпаетесь посреди пустоты. песок, металлические обломки, все это вы уже видели однажды. вы чувствуете как горячий воздух наполняет ваше горло... горло? вы осматриваете себя и замечаете странные трубки в вашей груди и шее. дотронувшись до лица вы понимаетечто на лице респиратор. кажется вы теперь киборг... надо добраться до ближайшего населенного пункта как можно скорее, вы чувствуете что ваш кислород на исходе. путешествие начинается."\n60km [НАЧАЛО]')  #начальное сообщение

        self.seed = ['void'] * 60  #генерация карты (сначала заполняем все 60 мест пустыми местами)
        self.km = 0
        self.enemies_count = 4
        self.events_count = 4
        for i in range(1, self.enemies_count + 1):
            self.seed[i * rand.randint(1, 60//self.enemies_count - 1)] = 'enemy' #равномерно, рандомно добавляем позиции с врагами
        for i in range(1, self.events_count + 1):
            self.seed[i * rand.randint(1, 60//self.events_count - 1)] = 'event' #равномерно, рандомно добавляем позиции с событиями
        self.seed[1] = 'npc'
        self.seed[-1] = 'ending'
        self.act()

    def act(self):
        choice = input('\nвыбор действия (enter - идти, u - использовать предмет, s - сохранить прогресс)>>> ')
        if choice == '': # enter - идти
            self.void()
    
    def void(self):
        print(f'{60 - self.km}km [ПУСТО] - "кажется здесь пусто"')

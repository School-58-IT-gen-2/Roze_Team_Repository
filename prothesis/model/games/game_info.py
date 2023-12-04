import random as rand


class GameInfo():

    def __init__(self):
        self.seed = [
            'void'
        ] * 60  #генерация карты (сначала заполняем все 60 мест пустыми местами)
        self.enemies_count = 4
        self.events_count = 4
        for i in range(1, self.enemies_count + 1):
            self.seed[i * rand.randint(
                1, 60 // self.enemies_count - 1
            )] = 'enemy'  #равномерно, рандомно добавляем позиции с врагами
        for i in range(1, self.events_count + 1):
            self.seed[i * rand.randint(
                1, 60 // self.events_count - 1
            )] = 'event'  #равномерно, рандомно добавляем позиции с событиями
        self.seed[1] = 'npc'
        self.seed[-1] = 'ending'

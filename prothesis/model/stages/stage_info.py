import random as rand


class StageInfo():

    def __init__(self, stage_prologue, stage_num=1):
        self.stage_num = stage_num  #номер стадии
        self.stage_prologue = stage_prologue
        self.enemies_count = 5  #кол-во врагов на стадии
        self.events_count = 3  #кол-во событий на стадии

        self.seed = ['void'] * 61  #генерация карты (сначала заполняем все 60 мест пустыми местами)
        for i in range(1, self.enemies_count + 1):
            self.seed[i * rand.randint(1, 60 // self.enemies_count - 1)] = 'enemy'  #равномерно, рандомно добавляем позиции с врагами
        for i in range(1, self.events_count + 1):
            self.seed[i * rand.randint(1, 60 // self.events_count - 1)] = 'event'  #равномерно, рандомно добавляем позиции с событиями
        self.seed[1] = 'start'
        self.seed[2] = 'npc'
        self.seed[20] = 'trader'
        self.seed[40] = 'trader2'
        self.seed[-1] = 'ending'

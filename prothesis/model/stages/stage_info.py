import random as rand
import sqlite3
from prothesis.model.postegress.adapter import AdapterDB
import copy




class StageInfo():

    def __init__(self, stage_prologue, stage_num=1, custom_seed=False):
        self.id = 1
        self.stage_num = stage_num  #номер стадии
        self.stage_prologue = stage_prologue
        self.enemies_count = 5  #кол-во врагов на стадии
        self.events_count = 3  #кол-во событий на стадии
        self.npc_count = 2
        self.sql_adapter = AdapterDB()
        if not custom_seed:
            self.seed = ['void'] * 61  #генерация карты (сначала заполняем все 60 мест пустыми местами)
            for i in range(1, self.enemies_count + 1):
                self.seed[i * rand.randint(1, 60 // self.enemies_count - 1)] = 'enemy'  #равномерно, рандомно добавляем позиции с врагами
            for i in range(1, self.events_count + 1):
                self.seed[i * rand.randint(1, 60 // self.events_count - 1)] = 'event'  #равномерно, рандомно добавляем позиции с событиями
            for i in range(1, self.npc_count):
                self.seed[i * rand.randint(1, 60 // self.npc_count - 1)] = 'npc'
            self.seed[1] = 'start'
            self.seed[2] = 'npc'
            self.seed[20] = 'trader'
            self.seed[40] = 'trader'
            self.seed[-1] = 'ending'
        else:
            self.seed = ['void'] * 61  #генерация карты (сначала заполняем все 60 мест пустыми местами)
            self.seed[1] = 'start'
            self.seed[3] = 'enemy'
            self.seed[4] = 'event'
            self.seed[5] = 'trader'
            self.seed[7] = 'npc'
    def load_seed(self):
        data = self.sql_adapter.get_by_player_id('Seed','place_in_seed',self.id)
        for i in range(len(data)):
            data[i] = data[i][0]
        place = data
        data = self.sql_adapter.get_by_player_id('Seed','text_place_in_seed',self.id)
        for i in range(len(data)):
            data[i] = data[i][0]
        text = data
        seed = []
        for i in range(len(place)):
            seed.append(0)
        for i in range(len(place)):
            seed[place[i]] = text[i]
        self.seed = seed
    def new_seed(self):
        seed = copy.copy(self.seed)
        if self.sql_adapter.get_by_player_id('Seed','place_in_seed',self.id) != []:
            self.sql_adapter.delete_by_player_id('Seed', self.id)
        for i in seed:
            self.sql_adapter.insert('Seed', {'place_in_seed': f'{seed.index(i)}', 'player_id':f'{self.id}', 'text_place_in_seed': f'{i}'})
            seed[seed.index(i)] = 0
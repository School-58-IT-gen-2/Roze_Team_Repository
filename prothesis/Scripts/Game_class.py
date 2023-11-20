from creatures_database import sage
from creatures_database import events_for_stages
from creatures_database import enemies_for_stages
import random as rand

class Stage():

    def __init__(self, stage_num, stage_prologue, player):
        self.stage_num = stage_num #номер стадии
        self.stage_prologue = stage_prologue
        self.enemies_count = 5 #кол-во врагов на стадии
        self.events_count = 3 #кол-во событий на стадии
        self.km = 0
        self.player = player
        
        print(f'"{self.stage_prologue}"\n 60km [НАЧАЛО]')  #начальное сообщение

        self.seed = ['void'] * 60  #генерация карты (сначала заполняем все 60 мест пустыми местами)
        for i in range(1, self.enemies_count + 1):
            self.seed[i * rand.randint(1, 60//self.enemies_count - 1)] = 'enemy' #равномерно, рандомно добавляем позиции с врагами
        for i in range(1, self.events_count + 1):
            self.seed[i * rand.randint(1, 60//self.events_count - 1)] = 'event' #равномерно, рандомно добавляем позиции с событиями
        self.seed[1] = 'npc'
        self.seed[-1] = 'ending'
        self.__cycle()

    def __cycle(self):
        choice = input('\nвыбор действия>>> ')
        if choice == '': # enter - идти
            self.step()

    def step(self):
        self.km += 1
        self.player.air -= rand.randint(1, 8)
        if self.player.air <= 0:
            print('"Вы судорожно глотаете остатки воздуха..."')
            self.player.death(self.km)
        elif self.player.air < 15:
            print('"!Критически мало воздуха, срочно воспользуйтесь ингалятором"')
        elif self.player.air < 40:
            print('"!Мало воздуха, воспользуйтесь ингалятором"')
        eval(f'self.{self.seed[self.km]}(self.player)') #происходит то, что на текущей позиции в сиде
        self.__cycle()

    def void(self, player):
        print(f'{60 - self.km}km [ПУСТО] - "кажется здесь пусто"')
    
    def enemy(self, player):
        print(f'{60 - self.km}km [НАПАДЕНИЕ] - "кажется здесь враг"')
        enemy = rand.choice(enemies_for_stages[self.stage_num])
        enemy.meeting()
    
    def event(self, player):
        print(f'{60 - self.km}km [СОБЫТИЕ] - ', end='')
        event = events_for_stages[self.stage_num][0]
        event.execute(player)
        
    def npc(self, player):
        sage.meeting()
    
    def ending(self, player):
        print('')

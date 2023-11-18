from NPC_class import sage

class Stage():

    def __init__(self, stage_num, stage_prologue):
        self.stage_num = stage_num
        self.stage_prologue = stage_prologue
        print(f'50km [НАЧАЛО] - "{self.stage_prologue}"')  #начальное сообщение
        self.km = -1
        self.seed = ['void'] * 50  #генерация карты (сначала заполняем все 50 мест пустыми местами)
        self.seed[5] = 'enemy'
        self.seed[10] = 'npc'
        self.__cycle()

    def __cycle(self):
        choice = input('выбор действия>>> ')
        if choice == '':
            self.step()

    def step(self):
        self.km += 1
        eval(f'self.{self.seed[self.km]}()')
        self.__cycle()

    def void(self):
        print(f'{50 - self.km}km [ПУСТО] - "кажется здесь пусто"')
    
    def enemy(self):
        print(f'{50 - self.km}km [НАПАДЕНИЕ] - "кажется здесь враг"')
        
    def npc(self):
        sage.meeting()

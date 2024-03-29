import sqlite3
from prothesis.view.player_view import PlayerView
from prothesis.model.postegress.adapter import AdapterDB

class PlayerInfo():
    def __init__(self):
        self.air = 99
        self.health = 100
        self.inventory = [['ингалятор', 'air', 25, 30]]
        self.money = 50
        self.protez = 100
        self.weapons = [['микроволновая п-ушка', 15, 1, 300, 'сбои'],['ПМ', 10, 4, 600, 'повреждение']]
        self.save = True #для проверки сейвов
        self.km = 0
        self.user = 1827810009
        self.sql_adapter = AdapterDB()


    def create_table(self):#неведомая хрень
        self.c.execute('''CREATE TABLE IF NOT EXISTS player_info
                         (air INTEGER, health INTEGER, inventory TEXT, money INTEGER, protez INTEGER, weapons TEXT, save INTEGER, km INTEGER)''')
        self.conn.commit()

    def new_sql(self, user_id):
        if self.sql_adapter.get_by_id('Player_info', user_id) == []:
            self.sql_adapter.insert('Player_info', {'id':user_id, 'air':'DEFAULT', 'health':'DEFAULT', 'inventory':'DEFAULT', 'money':'DEFAULT', 'protez':'DEFAULT', 'weapons':'DEFAULT', 'save':'DEFAULT', 'km':'DEFAULT'})

    def load_sql(self):
        print(self.sql_adapter.get_by_id('Player_info', id=self.user)[0][8])
        self.air = self.sql_adapter.get_by_id('Player_info', id=self.user)[0][8]

    def save_sql(self, user_id):
        self.sql_adapter.update('Player_info', f'air = {self.air}', user_id)

    def get_data(self):
        data = vars(self) #vars преобразует все атрибуты класса в один словарь
        return data 

    def set_info(self, data):
        for key in list(data.keys()):
            exec(f'self.{key} = data[key]')

    def set_money(self, count, player_view: PlayerView):
        symbol = '+' if count > 0 else '-'
        self.money = max(self.money + count, 0)
        player_view.send_response_to_player(
            f'{symbol} {count}k (ваш баланс: {str(self.money)} кредитов)')
    
    def get_money(self, count=None):
        return self.money if count is None else self.money >= count
        #если на вход ничего не дали, то возвращаем все деньги
        #если дали, то возвращаем больше\равны ли они указанного числа

    def get_air(self, count=None):
        return self.air if count is None else self.air >= count
        #если на вход ничего не дали, то возвращаем весь воздух
        #если дали, то возвращаем больше\равны ли они указанного числа

    def get_health(self, count=None):
        return self.health if count is None else self.health >= count
        #если на вход ничего не дали, то возвращаем все хп
        #если дали, то возвращаем больше\равны ли они указанного числа

    def get_protez(self, count=None):
        return self.protez if count is None else self.protez >= count
        #если на вход ничего не дали, то возвращаем весь протез
        #если дали, то возвращаем больше\равны ли они указанного числа

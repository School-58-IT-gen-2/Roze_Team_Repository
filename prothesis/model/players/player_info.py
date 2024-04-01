import sqlite3
from prothesis.view.player_view import PlayerView
from prothesis.model.postegress.adapter import AdapterDB


class PlayerInfo():
    def __init__(self):
        self.id = 1827810009
        self.health = 100
        self.money = 50
        self.protez = 0
        self.save = True #для проверки сейвов
        self.km = 0
        self.air = 100
        self.inventory = [2,3,4] #[['ингалятор', 'air', 25, 30]]
        self.weapons = [1,5]#[['микроволновая п-ушка', 15, 1, 300, 'сбои'],['ПМ', 10, 4, 600, 'повреждение']]
        self.sql_adapter = AdapterDB()

    def create_table(self):#неведомая хрень
        self.c.execute('''CREATE TABLE IF NOT EXISTS player_info
                         (air INTEGER, health INTEGER, inventory TEXT, money INTEGER, protez INTEGER, weapons TEXT, save INTEGER, km INTEGER)''')
        self.conn.commit()

    def new_sql(self, user_id):
        if self.sql_adapter.get_by_id('Player_info', user_id) == []:
            self.sql_adapter.insert('Player_info', {'id':user_id, 'air':'DEFAULT', 'health':'DEFAULT', 'money':'DEFAULT', 'protez':'DEFAULT', 'save':'DEFAULT', 'km':'DEFAULT'})

    def load_sql(self):
        x = 0
        for i in list(vars(self).keys()):
           x += 1
           if x < 8:
               exec(f"self.{i} = self.sql_adapter.get_by_id('Player_info', id=self.id)[0][{x-1}]")
        data = self.sql_adapter.get_by_player_id('Player_inventory','id',self.id)
        for i in range(len(data)):
            data[i] = data[i][0]
        self.inventory = data
        data = self.sql_adapter.get_by_player_id('Player_weapons','weapon_id',self.id)
        for i in range(len(data)):
            data[i] = data[i][0]
        self.weapons = data
    def save_sql(self):
     #self.sql_adapter.update('Player_info', f'air = {self.air}', user_id)
        par = vars(self)
        x = 0
        for i in list(vars(self).keys()):
           x +=1
           if x < 8:
               print(f"self.sql_adapter.update('Player_info', '{i} = {par[i]}', {self.id})")
               exec(f"self.sql_adapter.update('Player_info', '{i} = {par[i]}', {self.id})")
        exec(f"self.sql_adapter.delete_by_player_id('Player_inventory',{self.id})")
        exec(f"self.sql_adapter.delete_by_player_id('Player_weapons',{self.id})")
        for i in self.inventory:
            val = {'player_id' : f'{self.id}','item_id':f'{i}'}
            exec(f"self.sql_adapter.insert('Player_inventory',{val})")
        for i in self.weapons:
            val = {'player_id' : f'{self.id}','weapon_id':f'{i}'}
            exec(f"self.sql_adapter.insert('Player_weapons',{val})")


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

class PlayerInfo():
    def __init__(self):
        self.air = 100
        self.health = 100
        self.inventory = [['ингалятор', 'air', 25, 30]]
        self.money = 50
        self.protez = 100
        self.weapons = [['микроволновая п-ушка', 15, 1, 300, 'сбои'],['ПМ', 10, 4, 600, 'повреждение']]
        self.save = True #для проверки сейвов
        self.km = 0

    def get_data(self):
        data = vars(self) #vars преобразует все атрибуты класса в один словарь
        return data 
    
    def set_info(self, data):
        print(data.keys())
        for key in list(data.keys()):
            exec(f'self.{key} = data[key]')

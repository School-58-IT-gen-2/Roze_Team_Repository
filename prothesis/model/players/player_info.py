class PlayerInfo():

    def __init__(self):
        self.air = 100
        self.health = 100
        self.inventory = [['ингалятор', 'air', 25, 30]]
        self.money = 50
        self.protez = 100
        self.weapons = [['микроволновая п-ушка', 15, 1, 300, 'сбои'],['ПМ', 10, 4, 600, 'повреждение']]
        self.km = 0

    def get_inventory(self):
        return self.inventory

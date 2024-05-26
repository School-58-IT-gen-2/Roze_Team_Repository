class Weapon:
    def __init__(self, id, name, damage=0, attacks=1, cls='weapon', damage_type='кровотечение', price=0):
        self.id = id
        self.name = name
        self.damage = damage
        self.attacks = attacks
        self.cls = cls
        self.damage_type = damage_type
        self.price = price
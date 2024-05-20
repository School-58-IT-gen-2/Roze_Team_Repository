class Weapon:
    def __init__(self, id, name, damage=0, attacks=1, weapon_class='weapons', damage_type='кровотечение', price=0):
        self.id = id
        self.name = name
        self.damage = damage
        self.attacks = attacks
        self.weapon_class = weapon_class
        self.damage_type = damage_type
        self.price = price
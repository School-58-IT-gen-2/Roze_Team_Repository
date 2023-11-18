import random
from main import Player
class Event:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def execute(self):
        pass

    def __str__(self):
        return f"{self.name}: {self.description}"


class Event1(Event):
    def __init__(self):
        name = "Золото на дороге (не) валяется."
        description = "Вы нашли золотую детальку! Но она неного потрепана, вы не хотите её использовать и решаете продать.. Первый попавшийся робот выпукает ее за.."
        super().__init__(name, description)

    def execute(self):
        gold_price = random.randint(50,100)
        self.money += gold_price
        print( gold_price, "Бролларов! Чтож, деньги тут ещё никому не мешали..")

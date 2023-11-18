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
        
class Event2(Event):
    def __init__(self, name, description, option1, option2):
        name='Запретный плод.'
        description='К вам подходит робо-змея и предлагает купить Яблоко за 25 Бролларов, вы бы предпочли...'
        super().__init__(name, description)
        self.option1 = option1
        self.option2 = option2

    def execute(self):
        print(self.name)
        print(self.description)
        print(f"Согласиться! Кто не рискует тот не пьет детское шампанское. {self.option1}")
        print(f"Отказаться. Змей с яблоком звучит крайне опасно. {self.option2}")

        choice = input("Введите номер выбранного варианта (1 или 2): ")

        if choice == "1":
            print(f"Вы решились на сделку.: {self.option1}")
            print('А вы рисковый бро! За смелость змей вознаградил тебя мини-инголятором в виде яблока.')
            self.air += 15
        elif choice == "2":
            print(f"Вы ,пожалуй, откажетесь...: {self.option2}")
            print('Безопасность важнее риска, вы уходите, змей исчезает.')

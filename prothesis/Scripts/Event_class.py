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
            self.air += 15 #нужно добавить мини-инголятор в инвентарь
            self.money -= 25
        elif choice == "2":
            print(f"Вы ,пожалуй, откажетесь...: {self.option2}")
            print('Безопасность важнее риска, вы уходите, змей исчезает.')
            
class Event3(Event):
    def __init__(self, name, description, option1, option2):
        name = "Не беспокойтесь, это не только в Америке."
        description = "Вы увидели существо, выглядешее точь в точь как вы! Решитесь ли вы к нему подойти или убежите? "
        super().__init__(name, description)
        self.option1 = option1
        self.option2 = option2

    def execute(self):
        print(self.name)
        print(self.description)
        print(f"Подойти, вдруг это мой разлученный брат-близнец!. {self.option1}")
        print(f"КОНЕЧНО БЕЖАТЬ, ВЫ ЧЕ. {self.option2}")

        choice = input("Введите номер выбранного варианта (1 или 2): ")

        if choice == "1":
            print(f"Вы набрались смелости изучить существо.: {self.option1}")
            print('Вы решили не послушать умных людей из интернета и не зря! Существо обладало парочкой недостающих вашему протезу деталей и любезно поделилось.')
            self.protez += 20
        elif choice == "2":
            print(f"Вы ,пожалуй, откажетесь...: {self.option2}")
            print('А мне в ютуб шортс сказали избегать таких.. Вы попытались убежать, но существо догнало вас и от первого же удара вы вырубились. Как только вы пришли в сознание, рядом никого не было') 
            self.health -= 35

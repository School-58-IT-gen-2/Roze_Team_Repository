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

    def execute(self, Player):
        gold_price = random.randint(50,100)
        Player.money += gold_price
        print( gold_price, "Бролларов! Чтож, деньги тут ещё никому не мешали..")
        
class Event2(Event):
    def __init__(self, name, description, option1, option2):
        name='Запретный плод.'
        description='К вам подходит робо-змея и предлагает купить Яблоко за 25 Бролларов, вы бы предпочли...'
        super().__init__(name, description)
        self.option1 = option1
        self.option2 = option2

    def execute(self, Player):
        print(self.name)
        print(self.description)
        print(f"Согласиться! Кто не рискует тот не пьет детское шампанское. {self.option1}")
        print(f"Отказаться. Змей с яблоком звучит крайне опасно. {self.option2}")

        choice = input("Введите номер выбранного варианта (1 или 2): ")

        if choice == "1":
            print(f"Вы решились на сделку.: {self.option1}")
            print('А вы рисковый бро! За смелость змей вознаградил тебя мини-инголятором в виде яблока.')
            Player.air += 15 #нужно добавить мини-инголятор в инвентарь
            Player.money -= 25
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

    def execute(self, Player):
        print(self.name)
        print(self.description)
        print(f"Подойти, вдруг это мой разлученный брат-близнец!. {self.option1}")
        print(f"КОНЕЧНО БЕЖАТЬ, ВЫ ЧЕ. {self.option2}")

        choice = input("Введите номер выбранного варианта (1 или 2): ")

        if choice == "1":
            print(f"Вы набрались смелости изучить существо.: {self.option1}")
            print('Вы решили не послушать умных людей из интернета и не зря! Существо обладало парочкой недостающих вашему протезу деталей и любезно поделилось.')
            Player.protez += 20
        elif choice == "2":
            print(f"Вы ,пожалуй, откажетесь...: {self.option2}")
            print('А мне в ютуб шортс сказали избегать таких.. Вы попытались убежать, но существо догнало вас и от первого же удара вы вырубились. Как только вы пришли в сознание, рядом никого не было') 
            Player.health -= 35
            
class Event4(Event):
    def __init__(self):
        name = "Закулисье"
        description ="Упс.. похоже вас угораздило провалиться в текстурки.. к вам кто-то подходит, похоже, это холодно-голодные разрабы, они хотят кушать."
        super().__init__(name, description)

    def execute(self, Player):
        print("Разрабы этой игры нацелились на вас как на еду, но увидив у вас в кармане карточку нашли более рациональное решение.")
        print("- Поддержите наш проект, тогда мы поддержим вас. Донаты всегда будут тепло приняты тут 2202203666459724")
        print("Разрабы поверили вам на слово о поддержке проекта и щедро отсыпали плюшек.")
        Player.air += 7
	    Player.health += 7
	    Player.money += 7
	    Player.protez += 7

class Event5(Event):
    def __init__(self, name, description, option1, option2):
        name='Шифр.'
        description='Вы увидели новую, никем не тронутую аптечку, но.. на ней замок? Над ним странная надпись: Под деревом четыре льва, один ушёл, осталось... Вы думаете ответ... '
        super().__init__(name, description)
        self.option1 = option1
        self.option2 = option2

    def execute(self, Player):
        print(self.name)
        print(self.description)
        print(f"Два! Главное, что в рифму. {self.option1}")
        print(f"Три, это же самая простая детская загадка... {self.option2}")

        choice = input("Введите номер выбранного варианта (1 или 2): ")

        if choice == "1":
            print(f"Вы ввели в замок 'Два': {self.option1}")
            print('Ваш внутренний ребенок, кончено, порадовался, но мы живем не вмире глупых иллюзий. От замка вас ударило током')
            Player.health -= 15 
        elif choice == "2":
            print(f"Вы ввели в замок 'Три': {self.option2}")
            print('За простую загадку вы получили приятный бонус, поздравляю!')
            Player.health += 15
		
class Event6(Event):
    def __init__(self):
        name='Приятного аппетита'
        description='Вы бродите уже так долго.. вы очень хотите кушать.. стоп. Что это? Вы встретили  добрую вафельницу! Она не против накормить вас, только вот сколько это вафля уже лежит внутри..?'
        super().__init__(name, description)

    def execute(self, Player):
        print(self.name)
        print(self.description)

        choice = random.randint(1,2)

        if choice == "1":
            print("Она свежая! Вы вкусно покушали и готовы продолжать путь.")
            Player.health += 15 
        elif choice == "2":
            print("Она явно старше вас.. но чувство голода сильнее. Вы съедаете её.. кажется, вам не хорошо.")
            Player.health -=10

# -- часть Ильи --
import random as r
class PinkList(list):
	def __init__(self, *args):
			super().__init__(args)
			self.digit_words = ['нуль', 'адын', 'дьва', 'тьри', 'читыри', 'пят', 'шест', 'сем', 'восем', 'девить']
			self.__replace()

	def __replace(self):
			for i in range(len(self)):
				if isinstance(self[i], str):
							for j in range(10):
									self[i] = self[i].replace(str(j), self.digit_words[j])

	def __str__(self):
		return '--||--'.join(map(str, self))

	def append(self, arg):
		self.insert(0, arg)
		self.insert(len(self), arg)
		self.insert(r.randint(0, len(self) - 1), arg)
		
	def pop(self, arg):
		index = r.randint(0, len(self) - 1)
		deleted = self[index]
		del self[index]
		return deleted

	def remove(self, arg):
		ind = [i for i in range(len(self)) if self[i] == arg]
		for i in reversed(ind):
				del self[i]
	def randomize(self, arg):
		r.shuffle(self)
		if arg <= len(self) and arg >= 0:
			for i in range(arg):
				self.pop(0)
		else:
			return('Index out of range')
		

pink_list = PinkList('мне 6 лет', 'я лох', 2, 3, 4, 2)
print(pink_list)
pink_list.append('бот')
print(pink_list)
pink_list.remove(2)
print(pink_list)
pink_list.randomize(8)
print(pink_list)

# -- часть Веты --

# Это заглушка класса dict
class RedDict(dict):
    # подсказка - у класса dict есть метод __init__(self)
    # подсказка - у класса dict есть метод __init__(self, sequence)
    # подсказка - у класса dict есть метод __init__(self, **kwargs)
    def some_method(self):
        pass

# -- Часть Кого-то --

# Это заглушка класса set
class RedSet(set):
    # подсказка - у класса set есть метод __init__(self, items)
    def some_method(self):
        pass


# Это вызов конструктора списка с помощью кортежа.
# То есть на вход при создании экземпляра передается кортеж.
red_list = RedList((1, 2, 3))
# Вывод в консоли должен получится [1, 2, 3], ведь мы ничего не меняли в заглушке класса... пока что=)
print(red_list)
# Это вызов конструктора множества с помощью списка.
# То есть на вход при создании экземпляра передается список.
red_set = RedSet(['1', "q", "wow", '1'])

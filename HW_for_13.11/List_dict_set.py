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
		

pink_list = PinkList('мне 6 лет', 'pink_team', 2, 3, 4, 2)
print(pink_list)
pink_list.append('бот')
print(pink_list)
pink_list.remove(2)
print(pink_list)
pink_list.randomize(8)
print(pink_list)

# -- часть Веты --

class PinkDict(dict):
	def __init__(self, *kwargs):
		super().__init__(kwargs)
		self.digit_words = ['нуль', 'адын', 'дьва', 'тьри', 'читыри', 'пят', 'шест', 'сем', 'восем', 'девить']
		self.__replace()
	
	def __replace(self):
			for i in range(1, len(self)+1):
				if i % 2 == 0:
					key_list = list(self.keys())
					self[key_list[i-1]] = self.digit_words[i]

	def __str__(self):
		print('Вы используете кастомный словарь!!')
		key_items = list(self.items())
		for i in range(len(key_items)):
			print(i+1, '.', key_items[i])
		return('')
	
	def get(self, key):
		if key in self.keys():
			return self[key]
		else:
			return('такого ключа нет, дурачок')

	def pink_values(self):
		return(tuple(list(self.values())))
	
	def pink_keys(self):
		glued_str = []
		for i in self.values():
			glued_str.append(str(i))
		return(''.join(glued_str))
	
	def pink_copy(self):
		new_self = self
		for i in new_self.keys():
			if isinstance(i, str):
				new_self[i] = None
		return new_self

	def true_form_of_dict(self, k):
		for key, value in self.items():
			for j in range(2, k):
				self[key*j] = value*j
			break
		return self


pink = PinkDict([1, 'a'], [2, 'b'], [3, 'c'], ['four', 'd'])
print(pink)
print(pink.get(1))
print(pink.get(8))
print(pink.pink_values())
print(pink.pink_keys())
pink_cop = pink.pink_copy()
print(pink_cop)
pink_try = pink.true_form_of_dict(4)
print(pink_try)
# -- Часть Маши --

# Это заглушка класса set
class RedSet(set):
    # подсказка - у класса set есть метод __init__(self, items)
    def some_method(self):
        pass

# Последний кто будет коммитить, удалите эту часть когда она перестанет быть нужна

# Это вызов конструктора списка с помощью кортежа.
# То есть на вход при создании экземпляра передается кортеж.
red_list = PinkList((1, 2, 3))
# Вывод в консоли должен получится [1, 2, 3], ведь мы ничего не меняли в заглушке класса... пока что=)
print(red_list)
# Это вызов конструктора множества с помощью списка.
# То есть на вход при создании экземпляра передается список.
red_set = RedSet(['1', "q", "wow", '1'])

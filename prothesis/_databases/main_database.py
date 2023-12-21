'''from NPC_class import NPC
from Event_class import Event1
from Event_class import Event2
from Event_class import Event3
from Event_class import Event4
from Event_class import Event5
from Event_class import Event6
#БАЗА ДАННЫХ ДЛЯ СОБЫТИЙ
events_for_stages = {1:[Event1(), Event2('','','',''), Event3('','','',''), Event4(), Event5('','','',''), Event6()]}


'''
from prothesis.model.places.event_class import Common_event
from prothesis.model.places.event_class import Set_act
from prothesis.model.places.event_class import Text_act
from prothesis.model.places.event_class import Choice_act
from prothesis.model.places.event_class import Random_choice_act
from prothesis.model.places.npc_class import NPC
from prothesis.model.places.enemy_class import Enemy
from prothesis._databases.items_database import all_weapons


#БАЗА ДАННЫХ ДЛЯ НПС
Sage = NPC(name='Мудрец', dialogue={'Привет':'День добрый', 'кто ты?':'меня зовут мудрец, хотя местные называют меня сумашедшим', 'где я?':'добро пожаловать'})
Trader = NPC(name='Торговец', products = [['кинжал пораженный коррозией', 7, 4, 'weapon', 'кровотечение', 100], ['магнитный крюк', 10, 2, 'weapon', 'сбои', 100], ['бинты','health', 25, 'item', 20], ['ингалятор', 'air', 25, 'item', 30]], dialogue={'кто ты?':'Я просто старый торгаш, живущий прекрастной жизнью странника', 'как ты относишься к машинам?':'Машины... они давно стали как люди. Если Главную систему обтянут кожей, я не отличу ее от моей тещи! ха-ха... в любом случае, этот конфликт не моего маленького ума дело.'} )
Trader2 = NPC(name='Торговец', products = [['кинжал пораженный коррозией', 7, 4, 'weapon', 'кровотечение', 100], ['магнитный крюк', 10, 2, 'weapon', 'сбои', 100], ['бинты','health', 25, 'item', 20], ['ингалятор', 'air', 25, 'item', 30]], dialogue={'кто ты?':'Я просто старый торгаш, живущий прекрастной жизнью странника', 'как ты относишься к машинам?':'Машины... они давно стали как люди. Если Главную систему обтянут кожей, я не отличу ее от моей тещи! ха-ха... в любом случае, этот конфликт не моего маленького ума дело.'} )

npcs_for_stages = {1:[Sage, Trader, Trader2]}






#БАЗА ДАННЫХ ДЛЯ ВРАГОВ
Toster = Enemy('хлебоподжариватель', 'сбои', 100, all_weapons['кулак'], 5, 'loot')
Archives = Enemy('компьютер из библиотеки', 'сбои', 50, all_weapons['кулак'], 10, 'loot')
Bandit = Enemy('бандит', 'кровотечение', 100, all_weapons['кинжал пораженный коррозией'], 15, 'loot')
Wanderer = Enemy('бродяга','кровотечение', 100, all_weapons['кинжал пораженный коррозией'], 5, 'loot')

enemies_for_stages = {1:[Toster, Archives, Bandit, Wanderer]}






#БАЗА ДАННЫХ ДЛЯ СОБЫТИЙ
Snake_event = Common_event('Запретный плод.', 'Вы встречаете механическую змею', 
                           [
                               Text_act('К вам подходит робо-змея и предлагает купить Яблоко за 25 Бролларов'),
                               Choice_act('Вы бы предпочли...', 
                                          {
                                              'Отказаться': Text_act('Безопасность важнее риска, вы уходите, змей исчезает.'),
                                              'Согласиться!': Set_act({'air':25}, 'А вы рисковый бро! За смелость змей вознаградил тебя мини-инголятором в виде яблока.')
                                          })
                           ])

Wafle_event = Common_event('Приятного аппетита.', 'Вы бродите уже так долго.. вы очень хотите кушать.. стоп. Что это?', 
                           [
                                Text_act('Вы встретили  добрую вафельницу!'),
                                Random_choice_act('Она не против накормить вас, только вот сколько это вафля уже лежит внутри..?', 
                                                  {
                                                    Set_act({'health':20}, 'Она свежая! Вы вкусно покушали и готовы продолжать путь.'):0.7,
                                                    Set_act({'health':-20}, 'Она явно старше вас.. но чувство голода сильнее. Вы съедаете её.. кажется, вам не хорошо.'):0.3
                                                    })
                            ])

events_for_stages = {1:[Snake_event]}
from NPC_class import NPC
from Enemy_class import Enemy
from Event_class import Event1
from Event_class import Event2
from Event_class import Event3
import items_database
#БАЗА ДАННЫХ ДЛЯ СОБЫТИЙ
events_for_stages = {1:[Event1(), Event2('','','',''), Event3('','','','')]}



#БАЗА ДАННЫХ ДЛЯ НПС
sage = NPC(name='Мудрец')


#БАЗА ДАННЫХ ДЛЯ ВРАГОВ
Toster = Enemy('хлебоподжариватель', 'сбои', 100, items_database.all_weapons['кулак'], 5, 'loot')
enemies_for_stages = {1:[Toster]}


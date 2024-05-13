#id Макар: 1827810009
#id Виолетта: 1309198139
#id Даня: 5548785472

#бот PyZone: 6712575033:AAFi3-Juz0w3dlOSBNU4AAZDtYxwOAqrRTA
#бот NoAir: 6068101345:AAGr0hpElzAEBwfoc7-yoUhd-QRD9Sd8vr4

from prothesis.view.player_view import PlayerView
from prothesis.controller.game_controller import GameController
from prothesis.model.stages.stage_info import StageInfo
from prothesis.model.players.player_info import PlayerInfo
from prothesis.view.player_console_view import PlayerConsoleView
from prothesis.view.player_tg_view import PlayerTGView
from prothesis.model.postegress.adaptercsv import AdapterCSV
from prothesis.model.item_class import Item

import datetime as DT  

new_player_info = PlayerInfo()

player_view = PlayerTGView()#PlayerTGView(id=1827810009)

new_game_info = StageInfo(stage_prologue='''"вы просыпаетесь посреди пустоты. 
песок, металлические обломки, все это вы уже видели однажды. 
вы чувствуете как горячий воздух наполняет ваше горло...горло? 
вы осматриваете себя и замечаете странные трубки в вашей груди и шее. 
дотронувшись до лица вы понимаетечто на лице респиратор. 
кажется вы теперь киборг... 
надо добраться до ближайшего населенного пункта как можно скорее, 
вы чувствуете что ваш кислород на исходе. путешествие начинается."''',
custom_seed=False)

new_player_info.id  = player_view.chat_id
new_game_info.id = player_view.chat_id

if new_player_info.sql_adapter.get_by_id('Users', id=player_view.chat_id) == []:
    new_player_info.sql_adapter.insert('Users', {'id': player_view.chat_id, 'user_nickname': player_view.message_info.chat.username, 'chat_id': player_view.message_info.chat.id, 'created': int(player_view.message_info.date.timestamp()), 'updated': int(player_view.message_info.date.timestamp())}) 
new_player_info.new_sql(user_id=player_view.chat_id)


game_controller = GameController(new_player_info, new_game_info, player_view)
choice = game_controller.player_view.get_request_from_player('Добро пожаловать!', ['Загрузить игру', 'Новая игра'])
if choice == '2':
    player_view.send_response_to_player('Подождите, идёт генерация карты...')
    new_game_info.new_seed()
else:
    new_player_info.load_sql()
    new_game_info.load_seed()

print(new_player_info.inventory)

player_view.send_response_to_player('Добро пожаловать в игру! Выберите действие:')
game_controller.act()
    


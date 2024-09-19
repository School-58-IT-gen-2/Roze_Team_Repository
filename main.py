from dotenv import load_dotenv

load_dotenv()

from prothesis.controller.game_controller import GameController
from prothesis.model.stages.stage_info import StageInfo
from prothesis.model.players.player_info import PlayerInfo
from prothesis.view.player_tg_view import PlayerTGView, Thread
from prothesis.view.global_tg_view import GlobalTGView




global_view = GlobalTGView() #класс для принятия запросов от всех игроков
current_players = [] #список всех игроков, вошедших в игру



def start_game():
    '''Набор операций для запуска игры для игрока'''

    #Классы отвечающие за связь с тг ботом, информацию о игроке и информацию о текущей стадии игры
    new_player_view = PlayerTGView(global_view, chat_id=global_view.last_chat_id, message_info=global_view.last_message_info)
    new_player_info = PlayerInfo()
    new_game_info = StageInfo(stage_prologue='''"вы просыпаетесь посреди пустоты. 
песок, металлические обломки, все это вы уже видели однажды. 
вы чувствуете как горячий воздух наполняет ваше горло...горло? 
вы осматриваете себя и замечаете странные трубки в вашей груди и шее. 
дотронувшись до лица вы понимаетечто на лице респиратор. 
кажется вы теперь киборг... 
надо добраться до ближайшего населенного пункта как можно скорее, 
вы чувствуете что ваш кислород на исходе. путешествие начинается."''',
custom_seed=False)
    
    #запись id игрока
    new_player_info.id  = new_player_view.chat_id
    new_game_info.id = new_player_view.chat_id

    #формирование GameController из всего этого
    game_controller = GameController(new_player_info, new_game_info, new_player_view)

    #добавление игрока в базу данных, если его там нет
    if new_player_info.sql_adapter.get_by_id('Users', id=new_player_view.chat_id) == []:
        new_player_info.sql_adapter.insert('Users', {'id': new_player_view.chat_id, 'user_nickname': new_player_view.message_info.chat.username, 'chat_id': new_player_view.message_info.chat.id, 'created': int(new_player_view.message_info.date.timestamp()), 'updated': int(new_player_view.message_info.date.timestamp())}) 
    new_player_info.new_sql(user_id=new_player_view.chat_id)

    game_controller.player_view.send_response_to_player('Добро пожаловать!')

    #загрузка сохранения или создание новой игры по желанию игрока
    while True:
        choice = game_controller.player_view.get_request_from_player(text='Выберите опцию', variants=['Загрузить игру', 'Новая игра'])
        if choice == '2':
            new_player_view.send_response_to_player('Подождите, идёт генерация карты...')
            new_game_info.new_seed()
            break
        else:
            if new_player_info.sql_adapter.get_by_player_id('Seed', 'id', id=new_player_info.id) != []:
                new_player_info.load_sql()
                new_game_info.load_seed()
                break
            else:
                game_controller.player_view.send_response_to_player('На данный момент у вас нет сохранений')
    
    #запуск игры
    new_player_view.send_response_to_player('Добро пожаловать в игру! Выберите действие:')
    game_controller.act()


#вечный цикл ожидания новых игроков
while True:

    id = global_view.waiting_for_new_player(current_players)
    if id not in current_players:
        current_players.append(id)
        Thread(target=start_game).start()

'''def waiting_for_new_players():
    threadings = []
    threading = Thread(target=global_view.waiting_for_new_player())
    threadings.append(threading)
    threadings[-1].start()

    while True:
        if not threadings[-1].is_alive():
            Thread(target=start_game).start()
            print('Ожидание других игроков...')
            threading = Thread(target=global_view.waiting_for_new_player())
            threadings.append(threading)
            threadings[-1].start()


Thread(target=waiting_for_new_players()).start()
'''
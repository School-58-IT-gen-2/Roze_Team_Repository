from prothesis.controller.game_controller import GameController
from prothesis.model.stages.stage_info import StageInfo
from prothesis.model.players.player_info import PlayerInfo
from prothesis.view.player_console_view import PlayerConsoleView

new_player_info = PlayerInfo()

player_view = PlayerConsoleView()

nem_game_info = StageInfo(stage_prologue='''"вы просыпаетесь посреди пустоты. 
песок, металлические обломки, все это вы уже видели однажды. 
вы чувствуете как горячий воздух наполняет ваше горло...горло? 
вы осматриваете себя и замечаете странные трубки в вашей груди и шее. 
дотронувшись до лица вы понимаетечто на лице респиратор. 
кажется вы теперь киборг... 
надо добраться до ближайшего населенного пункта как можно скорее, 
вы чувствуете что ваш кислород на исходе. путешествие начинается."''')

player_controller = GameController(new_player_info, nem_game_info, player_view)
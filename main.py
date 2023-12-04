from prothesis.controller.game_controller import GameController
from prothesis.model.games.game_info import GameInfo
from prothesis.model.players.player_info import PlayerInfo

print('start')


def condition():
    return True


new_player_info = PlayerInfo()
nem_game_info = GameInfo()
player_controller = GameController(new_player_info, nem_game_info)

while condition():
    player_controller.act()

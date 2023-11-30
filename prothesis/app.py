from controller.player_controller import PlayerController
from model.players.player_info import PlayerInfo


def condition():
    return True

new_player_info = PlayerInfo()
player_controller = PlayerController(new_player_info)

while condition():
    player_controller.act()
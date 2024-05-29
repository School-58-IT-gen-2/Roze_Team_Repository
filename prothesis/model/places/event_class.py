import random
import time

from prothesis.view.player_view import PlayerView
from prothesis.view.player_console_view import PlayerConsoleView
from prothesis.model.players.player_info import PlayerInfo

class Event:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.player_view = PlayerView()
        self.player_info = PlayerInfo()

    def execute(self, player_view, player_info):
        self.player_view = player_view
        self.player_info = player_info

    def __str__(self):
        return f"{self.name}: {self.description}"
    
class Act:
    def __init__(self, description=''):
        self.description = description
        self.player_view = PlayerView()
        self.player_info = PlayerInfo()
    
    def execute(self, player_view, player_info):
        self.player_view = player_view
        self.player_info = player_info

class Text_act(Act):
    def __init__(self, description=''):
        super().__init__(description)
    
    def execute(self, player_view, player_info):
        super().execute(player_view, player_info)
        self.player_view.send_response_to_player(self.description)

class Photo_act(Act):
    def __init__(self, description='', photo=None):
        super().__init__(description)
        self.photo = photo
    
    def execute(self, player_view, player_info):
        super().execute(player_view, player_info)
        self.player_view.send_response_to_player(self.description)
        if self.photo != None:
            self.player_view.send_photo(self.photo)

class Set_act(Act):
    def __init__(self, parameters, description=''):
        super().__init__(description)
        self.parameters = parameters
    
    def execute(self, player_view, player_info):
        super().execute(player_view, player_info)
        self.player_view.send_response_to_player(self.description)
        for key in self.parameters.keys():
            exec(f'self.player_info.{key} += {self.parameters[key]}')

class Choice_act(Act):
    def __init__(self, description='', variants={}):
        super().__init__(description)
        self.variants = variants
    
    def execute(self, player_view, player_info):
        super().execute(player_view, player_info)
        choice = self.player_view.get_request_from_player(self.description, list(self.variants.keys()))
        time.sleep(1)
        self.variants[list(self.variants.keys())[int(choice) - 1]].execute(self.player_view, self.player_info)

class Random_choice_act(Act):
    def __init__(self, description='', variants={}):
        super().__init__(description)
        self.variants = variants
    
    def execute(self, player_view, player_info):
        super().execute(player_view, player_info)
        self.player_view.send_response_to_player(self.description)
        time.sleep(1)
        variants_pos = list(self.variants.values())
        new_variants = {}
        for index in range(len(variants_pos)):
            variants_pos[index] = variants_pos[index] if index == 0 else variants_pos[index] + variants_pos[index - 1]
            new_variants[variants_pos[index]] = list(self.variants.keys())[index]
        random_f = random.random()
        for pos in variants_pos:
            if pos >= random_f:
                new_variants[pos].execute(self.player_view, self.player_info)
                break

class Common_event(Event):
    def __init__(self, name, description, acts):
        super().__init__(name, description)
        self.acts = acts
    
    def execute(self, player_view, player_info):
        super().execute(player_view, player_info)
        self.player_view.send_response_to_player(self.description)
        for act in self.acts:
            time.sleep(1)
            act.execute(self.player_view, self.player_info)

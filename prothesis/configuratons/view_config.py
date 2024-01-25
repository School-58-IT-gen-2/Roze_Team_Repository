import json


class ViewConfig:
    def __init__(self):
        with open("prothesis/configs/view_config.json", "r", encoding="utf-8") as file:
            config = json.load(file)
        if not config:
            raise Exception("Config is empty, you maggot")

        self.view_type = config["view_type"]
        self.__allowed_answers_poll = config["allowed_answers_poll"]

    def get_view_type(self):
        return self.view_type

    def get_allowed_answers_poll(self):
        return self.__allowed_answers_poll
import json


class NetConfig:
    def __init__(self):
        with open("prothesis/configs/net_config.json", "r", encoding="utf-8") as file:
            config = json.load(file)
        if not config:
            raise Exception("Config is empty, you fool!")
        if config["token"]:
            self.__token = config["token"]
        else:
            raise Exception("Token is empty, you fool!")

    def get_token(self):
        return self.__token
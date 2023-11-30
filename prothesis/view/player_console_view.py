from player_view import PlayerView

class PlayerConsoleView(PlayerView):
    def __init__(self, locale="RU"):
        super().__init__(locale)

    def send_response_to_player(self, response):
        print(response)

    def __send_request_from_player_to_controller(self, request):
        return request

    def get_request_from_player(self):
        request = input()
        response = self.__send_request_from_player_to_controller(request)
        return response
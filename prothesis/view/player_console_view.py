from prothesis.view.player_view import PlayerView

class PlayerConsoleView(PlayerView):
    def __init__(self, locale="RU"):
        super().__init__(locale)

    def send_response_to_player(self, response):
        print(response)

    def __send_request_from_player_to_controller(self, request):
        return request

    def get_request_from_player(self, text='', variants=None, test=True):
        var_count = len(variants)
        request = None
        while request not in list(map(str, range(1, var_count + 1))):
            for i in range(var_count):
                print(f'{i + 1} - {variants[i]}', end=' ')
            request = input(text)
            if not test: break
        response = self.__send_request_from_player_to_controller(request)
        return response
    
    def way_report(self, km, place, text):
        print(f'{61 - km}km [{place}] - {text}')

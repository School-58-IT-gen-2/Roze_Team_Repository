#from telegram import Update

#from telegram import ForceReply, Update
#from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
#id Макар: 1827810009
#id Виолетта: 1309198139

#бот PyZone: 6712575033:AAFi3-Juz0w3dlOSBNU4AAZDtYxwOAqrRTA
#бот NoAir: 6068101345:AAGr0hpElzAEBwfoc7-yoUhd-QRD9Sd8vr4

from prothesis.view.player_view import PlayerView
from prothesis.controller.game_controller import GameController
from prothesis.model.stages.stage_info import StageInfo
from prothesis.model.players.player_info import PlayerInfo
from prothesis.view.player_console_view import PlayerConsoleView
from prothesis.view.player_tg_view import PlayerTGView

new_player_info = PlayerInfo()

player_view = PlayerTGView(id=1827810009)

new_game_info = StageInfo(stage_prologue='''"вы просыпаетесь посреди пустоты. 
песок, металлические обломки, все это вы уже видели однажды. 
вы чувствуете как горячий воздух наполняет ваше горло...горло? 
вы осматриваете себя и замечаете странные трубки в вашей груди и шее. 
дотронувшись до лица вы понимаетечто на лице респиратор. 
кажется вы теперь киборг... 
надо добраться до ближайшего населенного пункта как можно скорее, 
вы чувствуете что ваш кислород на исходе. путешествие начинается."''')


print(player_view.chat_id)
game_controller = GameController(new_player_info, new_game_info, player_view)
choice = game_controller.player_view.get_request_from_player('Добро пожаловать!', ['Загрузить игру', 'Новая игра'])
if choice == '1':
    game_controller.load_from_file('save_test.json')

'''
def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    choice = player_controller.__player_view.get_request_from_player('Добро пожаловать!', ['Загрузить игру', 'Новая игра'])
    if choice == '1':
        player_controller.load_from_file()
    elif choice == '2':
        player_controller.save_to_file()
    return update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    return update.message.reply_text("Help!")


def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    return update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6712575033:AAFi3-Juz0w3dlOSBNU4AAZDtYxwOAqrRTA").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)'''


game_controller.act()

class PlayerTGView(PlayerView):
    def __switch_locale(self, locale):
        pass
    def __init__(self, locale="RU"):
        self.__switch_locale(locale)

    def send_response_to_player(self, response):
        pass

    def get_request_from_player(self):
        pass
    
    def way_report(self, km, place, text):
        print(f'{60 - km}km [{place}] - {text}')

#if __name__ == "__main__":
    #main()

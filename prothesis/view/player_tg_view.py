from telegram import Update

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from player_view import PlayerView

def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    print("AAA")
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
    application.run_polling(allowed_updates=Update.ALL_TYPES)












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


if __name__ == "__main__":
    main()

from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from telegram.ext import CallbackContext
from typing import List

button_names = ["ннн", "777"]

def create_buttons(update: Update, context: CallbackContext, button_names: List[str]):
                custom_keyboard = [button_names]
                reply_markup = ReplyKeyboardMarkup(custom_keyboard)
                update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)

def start(update: Update, context: CallbackContext):
                create_buttons(update, context, button_names)

def button_click(update: Update, context: CallbackContext):
                text = update.message.text
                if text in button_names:
                                update.message.reply_text(f"Вы выбрали {text}")
                else:
                                update.message.reply_text("Пожалуйста, выберите опцию из предложенных кнопок.")

updater = Updater("6068101345:AAGr0hpElzAEBwfoc7-yoUhd-QRD9Sd8vr4", use_context=True)  # Замените "YOUR_BOT_TOKEN" на реальный токен вашего бота
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, button_click))

updater.start_polling()


class PlayerTGView(PlayerView):
    def __init__(self, locale="RU"):
        self.__switch_locale(locale)

    def send_response_to_player(update, context, self, response):
        update.message.reply_text(response)

    def get_request_from_player(update, context, self, button_func, button_names: List[str]):
        def create_buttons(update: Update, context: CallbackContext, button_names: List[str]):
            custom_keyboard = [button_names]
            reply_markup = ReplyKeyboardMarkup(custom_keyboard)
            update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)
        def button_click(update: Update, context: CallbackContext, button_func):
            text = update.message.text
            keys = button_func.keys()
            if text in keys:
                for i in range(len(keys)):
                    if keys[i] == text:
                        eval(button_func[keys[i]])
            else:
                update.message.reply_text("Пожалуйста, выберите опцию из предложенных кнопок.")
    


if __name__ == "__main__":
    main()

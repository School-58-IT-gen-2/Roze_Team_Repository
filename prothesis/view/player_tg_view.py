from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from telegram.ext import CallbackContext
from typing import List


def start(update: Update, context: CallbackContext):
                create_buttons(update, context, button_names)


updater = Updater("6068101345:AAGr0hpElzAEBwfoc7-yoUhd-QRD9Sd8vr4", use_context=True)  # Замените "YOUR_BOT_TOKEN" на реальный токен вашего бота
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, button_click))

updater.start_polling()



def send_response_to_player(update, context, response):
    update.message.reply_text(response)

def get_request_from_player(update, context, button_func, button_func: dict):
    custom_keyboard = [[*button_func.keys()]]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)
    button_click(update, context, button_func: dict)

def button_click(update: Update, context: CallbackContext, button_func: dict):
    text = update.message.text
    keys = button_func.keys()
    if text in keys:
        for i in range(len(keys)):
            if keys[i] == text:
                eval(button_func[keys[i]])
    else:
        update.message.reply_text("Пожалуйста, выберите опцию из предложенных кнопок.")


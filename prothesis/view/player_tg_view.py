from telegram import Bot

from prothesis.view.player_view import PlayerView
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from telegram.ext import CallbackContext
from typing import List
from dotenv import load_dotenv
import os


#ПРИМЕР МИШИ
load_dotenv()
tg_token = os.getenv('token')

bot = Bot(token=tg_token)


class PlayerTGView(PlayerView):
    def __init__(self, locale="RU", id=None):
        super().__init__(locale)
        self.update_id = None
        self.message_info = None
        print('Telegram bot launched, waiting for connection')
        if id == None:
            self.chat_id = None
            while True:
                chat_id, text = self.get_request_from_player(variants=['/start'], get_id=True, create_buttons=False)
                if text == '/start':
                    self.chat_id = chat_id
                    print(f'Telegram new connection: {chat_id}')
                    break
        else:
            self.chat_id = id
        

    def send_response_to_player(self, response):
        bot.send_message(self.chat_id, response)

    def create_buttons(self, text='', buttons=[]):
        custom_keyboard = [[btn] for btn in buttons]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        bot.send_message(self.chat_id, text=text, reply_markup=reply_markup)

    def get_request_from_player(self, text: str = None, variants: list = ['Да', 'Нет'], get_id=False, create_buttons=True, test=True):
        if text is not None and not create_buttons:
            bot.send_message(self.chat_id, text)
        elif create_buttons:
            self.create_buttons(text, variants)
        
        while True:
            updates = bot.get_updates(offset=self.update_id, timeout=10000)
            for update in updates:
                if update.message is not None and update.message.text is not None:
                    self.update_id = update.update_id + 1
                    message = update.message.text
                    if message in variants:
                        if get_id:
                            self.message_info = update.message
                            return update.message.chat_id, message
                        return str(variants.index(message) + 1)
    
    def send_photo(self, image, text=''):
        im = open(image, 'rb')
        bot.send_photo(chat_id=self.chat_id, photo=im)
    
    
    def way_report(self, km, place, text):
        bot.send_message(self.chat_id, f'{61 - km}km [{place}] - {text}')
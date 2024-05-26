from telegram import Bot
from threading import Thread

from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from telegram.ext import CallbackContext
from typing import List

token = "6712575033:AAFi3-Juz0w3dlOSBNU4AAZDtYxwOAqrRTA"
bot = Bot(token=token)

class GlobalTGView():
    def __init__(self):
        self.update_id = None
        self.last_chat_id = None
        self.last_message_info = None
        self.last_message = {'':0} #ключ - текст последнего сообщения, значение - айди автора последнего сообщения
        Thread(target=self.get_updates).start()
        print('\033[0;34mTelegram bot launched, waiting for connection\033[0;37m')

    def get_request(self, variants: list = ['Да', 'Нет'], get_id=False, chat_id=None, current_players=[]):
        while True:
            if list(self.last_message.keys())[0] in variants:
                text = list(self.last_message.keys())[0]
                player_id = list(self.last_message.values())[0]
                if get_id:
                    if player_id not in current_players:
                        self.last_chat_id = player_id
                        print(f'\033[0;34mTelegram new connection: {player_id}\033[0;37m')
                        return player_id
                elif player_id == chat_id:
                    return str(variants.index(text) + 1)

    def get_updates(self):
        while True:
            updates = bot.get_updates(offset=self.update_id, timeout=10000)
            for update in updates:
                if update.message is not None and update.message.text is not None:
                    self.update_id = update.update_id + 1
                    self.last_message = {update.message.text:update.message.chat_id}
                    self.last_message_info = update.message
                    print('\033[0;32m' + str(self.last_message) + '\033[0;37m')
                    '''
                    if message == '/start':
                            self.last_chat_id = update.message.chat_id
                            print(f'Telegram new connection: {self.last_chat_id}')
                            return
                    elif update.message.chat_id == chat_id and message in variants:
                        return str(variants.index(message) + 1)
                    '''
    
    def waiting_for_new_player(self, current_players):
        return self.get_request(variants=['/start'], get_id=True, current_players=current_players)
        
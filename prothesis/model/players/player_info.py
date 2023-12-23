import sqlite3
from prothesis.view.player_view import PlayerView

class PlayerInfo():
    def __init__(self):
        self.conn = sqlite3.connect('player_data.db')  
        self.c = self.conn.cursor()
        self.create_table()  


    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS player_info
                         (air INTEGER, health INTEGER, inventory TEXT, money INTEGER, protez INTEGER, weapons TEXT, save INTEGER, km INTEGER)''')
        self.conn.commit()

    def get_data(self):
        self.c.execute("SELECT * FROM player_info")
        data = self.c.fetchone()
        return dict(zip(('air', 'health', 'inventory', 'money', 'protez', 'weapons', 'save', 'km'), data))

    def set_info(self, data):
        placeholders = ', '.join('?' * len(data))
        columns = ', '.join(data.keys())
        values = tuple(data.values())
        self.c.execute(f"REPLACE INTO player_info ({columns}) VALUES ({placeholders})", values)
        self.conn.commit()

    def set_money(self, count, player_view: PlayerView):
        symbol = '+' if count > 0 else '-'
        self.money = max(self.money + count, 0)
        player_view.send_response_to_player(
            f'{symbol} {count}k (ваш баланс: {str(self.money)} кредитов)')
        self.set_info({'money': self.money})

    def __del__(self):
        self.conn.close() 

import psycopg2


class AdapterDB:
    def __init__(self) -> None:
        self.conn = self.__get_connect()

    def __get_connect(self):
        """подключение к нашей базе"""
        try:
            conn = psycopg2.connect(
                """
				host=rc1d-9cjee2y71olglqhg.mdb.yandexcloud.net
				port=6432
				dbname=sch58_db
				user=Admin
				password=atdhfkm2024
				target_session_attrs=read-write
			"""
            )
            return conn
        except:
            print("connection error")

    def get_table(self, table_name: str):
        """посылаем запрос на подключение к конкретной таблице"""
        request = f'SELECT * FROM "Roze_Galactic_Empire"."{table_name}"'
        cursor = self.conn.cursor()
        cursor.execute(request)
        data = cursor.fetchall()
        return data

    def get_all(self, table_name: str, param: str):
        request = f'SELECT {param} FROM "Roze_Galactic_Empire"."{table_name}"'
        cursor = self.conn.cursor()
        cursor.execute(request)
        data = cursor.fetchall()
        return data

    def get_by_name(self, table_name: str, param: str, name: str):
        request = f'SELECT {param} FROM "Roze_Galactic_Empire"."{table_name}" WHERE name = \'{name}\''
        cursor = self.conn.cursor()
        cursor.execute(request)
        data = cursor.fetchall()
        return data[0]
    
adapter_db = AdapterDB()
print(adapter_db.get_by_name('NPC', 'product', 'Мудрец'))


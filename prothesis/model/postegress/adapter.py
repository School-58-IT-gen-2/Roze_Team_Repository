import psycopg2


class AdapterDB:
    def __init__(self) -> None:
        self.conn = self.__get_connect()
        self.random = 0

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
        except Exception as error:

            print(f"SQL connection error: {error}")

    def __sql_format(self, value):
        if value == None: return 'Null'
        if type(value) == str and value not in ['DEFAULT']: return f"'{value}'"
        return str(value)

    def get_all(self, table_name: str):
        """посылаем запрос на подключение к конкретной таблице"""
        request = f'SELECT * FROM "Roze_Team"."{table_name}"'
        cursor = self.conn.cursor()
        cursor.execute(request)
        data = cursor.fetchall()
        return data

    def get_by_id(self, table_name: str, id: int):
        request = f'SELECT * FROM "Roze_Team"."{table_name}" WHERE id = {id}'
        cursor = self.conn.cursor()
        cursor.execute(request)
        data = cursor.fetchall()
        return data
    def get_by_player_id(self, table_name: str,key:str, id: int):
        request = f'SELECT {key} FROM "Roze_Team"."{table_name}" WHERE player_id = {id}'
        cursor = self.conn.cursor()
        cursor.execute(request)
        data = cursor.fetchall()
        return data
    def delete_by_id(self, table_name: str, id: int):
        request_select = f'SELECT * FROM "Roze_Team"."{table_name}"'
        request = f'DELETE FROM "Roze_Team"."{table_name}" WHERE id = {id}'
        cursor = self.conn.cursor()
        cursor.execute(request)
        cursor.execute(request_select)
        self.conn.commit()
        data = cursor.fetchall()
        return data
    def delete_by_player_id(self, table_name: str, id: int):
        request_select = f'SELECT * FROM "Roze_Team"."{table_name}"'
        request = f'DELETE FROM "Roze_Team"."{table_name}" WHERE player_id = {id}'
        cursor = self.conn.cursor()
        cursor.execute(request)
        cursor.execute(request_select)
        self.conn.commit()
        data = cursor.fetchall()
        return data
    
    def update(self, table, request, id):
        request_select = f'SELECT * FROM "Roze_Team"."{table}"'
        request = f'UPDATE "Roze_Team"."{table}" SET {request} WHERE id={id}'
        cursor = self.conn.cursor()
        cursor.execute(request)
        cursor.execute(request_select)
        self.conn.commit()
        data = cursor.fetchall()
        return data

    def insert(self, table, values):
        print( f'INSERT INTO "Roze_Team"."{table}" ({", ".join([i for i in values.keys()])}) VALUES ({", ".join([self.__sql_format(i) for i in values.values()])})')
        request = f'INSERT INTO "Roze_Team"."{table}" ({", ".join([i for i in values.keys()])}) VALUES ({", ".join([self.__sql_format(i) for i in values.values()])})'
        request_select = f'SELECT * FROM "Roze_Team"."{table}" '
        cursor = self.conn.cursor()
        cursor.execute(request)
        cursor.execute(request_select)
        self.conn.commit()
        data = cursor.fetchall()
        return data

    def get_by_any(self,select):
        request = select
        cursor = self.conn.cursor()
        cursor.execute(request)
        self.conn.commit()
        data = cursor.fetchall()
        return data
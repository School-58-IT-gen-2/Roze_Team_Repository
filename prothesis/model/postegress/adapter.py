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
        except:
            print("connection error")

    def get_all(self, table_name: str):
        """посылаем запрос на подключение к конкретной таблице"""
        request = f'SELECT * FROM "Roze_Galactic_Empire"."{table_name}"'
        cursor = self.conn.cursor()
        cursor.execute(request)
        data = cursor.fetchall()
        return data

    def get_by_id(self, table_name: str, id: int):
        request = f'SELECT * FROM "Roze_Galactic_Empire"."{table_name}" WHERE id = {id}'
        cursor = self.conn.cursor()
        cursor.execute(request)
        data = cursor.fetchall()
        return data
    def delete_by_id(self, table_name: str, id: int):
        request_select = f'SELECT * FROM "Roze_Galactic_Empire"."{table_name}"'
        request = f'DELETE FROM "Roze_Galactic_Empire"."{table_name}" WHERE id = {id}'
        cursor = self.conn.cursor()
        cursor.execute(request)
        cursor.execute(request_select)
        self.conn.commit()
        data = cursor.fetchall()
        return data
    
    def update(self, table, request, id):
        request_select = f'SELECT * FROM "Roze_Galactic_Empire"."{table}"'
        request = f'UPDATE "Roze_Galactic_Empire"."{table}" SET {request} WHERE id={id}'
        cursor = self.conn.cursor()
        cursor.execute(request)
        cursor.execute(request_select)
        self.conn.commit()
        data = cursor.fetchall()
        return data

    def insert(self, table, values):
        
        print( f'INSERT INTO "Roze_Galactic_Empire"."{table}" ({", ".join([i for i in values.keys()])}) VALUES ({", ".join([str(i) for i in values.values()])})')
        request = f'INSERT INTO "Roze_Galactic_Empire"."{table}" ({", ".join([i for i in values.keys()])}) VALUES ({", ".join([str(i) for i in values.values()])})'
        request_select = f'SELECT * FROM "Roze_Galactic_Empire"."{table}" '
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
    
#a = AdapterDB()
#a.delete_by_id("Items",7)
#a.insert("Items",{'name' : "'помидор'",'id' : 'DEFAULT','type' : "'health'", 'value' : '12','class' : "'items'", 'price': '112'  })
#print(a.get_by_any('SELECT "star type","name" FROM "Roze_Galactic_Empire"."Systems" WHERE "Allegiance" = \'Empire\' and lower("name") = "name"  LIMIT 100'))
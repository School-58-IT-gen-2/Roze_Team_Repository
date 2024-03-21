from prothesis.model.postegress.adapter import AdapterDB
import psycopg2
import csv
class AdapterCSV:
    def __init__(self) -> None:
        self.conn = self.__get_connect()
        self.adapter = AdapterDB()
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

    def __sql_format(self, value):
        if value == None: return 'Null'
        if type(value) == str: return f"'{value}'"
        return str(value)

    def insert(self, table, values, unic=False):
        print( f'INSERT INTO "Roze_Galactic_Empire"."{table}" ({", ".join([i for i in values.keys()])}) VALUES ({", ".join([self.__sql_format(i) for i in values.values()])})')
        if unic == False: request = f'INSERT INTO "Roze_Galactic_Empire"."{table}" ({", ".join([i for i in values.keys()])}) VALUES ({", ".join([self.__sql_format(i) for i in values.values()])})'
        else: request = f'INSERT INTO "Roze_Galactic_Empire"."{table}" ({", ".join([i for i in values.keys()])}) VALUES ({", ".join([self.__sql_format(i) for i in values.values()])})'
            #if self.adapter.get_by_id('Users', values['id']) == []: 
        request_select = f'SELECT * FROM "Roze_Galactic_Empire"."{table}" '
        cursor = self.conn.cursor()
        cursor.execute(request)
        cursor.execute(request_select)
        self.conn.commit()
        data = cursor.fetchall()
        return data
    
    def insert_all(self,file):
        x = file.split(".")
        x = x[0]
        with open(file, 'r', encoding= 'UTF-8') as f:
            data = csv.DictReader(f, delimiter=',')
            for row in data:
                for i in row.keys():
                    if not row[i].isdigit():
                        row[i] = f"'{row[i]}'"
                a.insert(x,row)


#a = AdapterCSV()
#a.insert_all("NPC.csv")

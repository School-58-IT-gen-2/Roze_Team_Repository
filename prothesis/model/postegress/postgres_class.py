import psycopg2
import os
from dotenv import load_dotenv
''' 
любые запросы хорошо чекать на ошибки, поскольку полеты данных - вещь непредсказуемая. 
Если данные не летят/не изменяются, это не всегда очевидно. 
А проверка на подключение поможет искать ошибки миллион лет, когда их на самом деле нет, вы просто до базы достучаться не можете 
    '''
    # подключение к нашей базе
load_dotenv()
sql_conect_data = os.getenv('sql_conect_data')
sql_conect_data = sql_conect_data.split(',')

try:
    conn = psycopg2.connect(
        f"""
			host={sql_conect_data[0]}
			port={sql_conect_data[1]}
			dbname={sql_conect_data[2]}
			user={sql_conect_data[3]}
			password={sql_conect_data[4]}
			target_session_attrs={sql_conect_data[5]}
	"""
    )
except:
    print("connection error postgres")

# посылаем запрос на подключение к конкретной таблице
request = 'SELECT * FROM "Roze_Galactic_Empire"."NPS"' 

# уснанавливаем связь с базой для выполнения запросов
cursor = conn.cursor()                                 
       
# выполняем запрос
cursor.execute(request) 

# табличку после запроса
data = cursor.fetchall()

print(data)

request_update = 'UPDATE "Roze_Galactic_Empire"."Planets" SET "Name"=\'Earth\', "System"=2, "Population"=10000000, "Position"=3, "Type"=2 WHERE id=2'

# выполняем запрос
cursor.execute(request_update)
cursor.execute(request)

# сохраняем изменения обновленной таблички
conn.commit()

data = cursor.fetchall()


print(data)

request_insert = 'INSERT INTO "Galactic Empire"."Planets" ("Name", id, "System", "Population", "Position", "Type") VALUES (\'Mityas_planet\', DEFAULT, 2, 1, 4, 2)'

# выполняем запрос
cursor.execute(request_insert)

cursor.execute(request)



data = cursor.fetchall()


print(data)

planet_name = input("Введите название планеты, на которой произойдет рагнарек ")



request_update = f'UPDATE "Galactic Empire"."Planets" SET "Name"=\'{planet_name}\', "System"=2, "Population"= 1, "Position"=3, "Type"=2 WHERE "Name"= \'{planet_name}\' '


cursor.execute(request_update)
cursor.execute(request)

conn.commit()

data = cursor.fetchall()


print(data)
class Postgres():
    def __init__(self):
        pass

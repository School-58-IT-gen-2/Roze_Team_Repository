import psycopg2

''' 
любые запросы хорошо чекать на ошибки, поскольку полеты данных - вещь непредсказуемая. 
Если данные не летят/не изменяются, это не всегда очевидно. 
А проверка на подключение поможет искать ошибки миллион лет, когда их на самом деле нет, вы просто до базы достучаться не можете 
    '''
try:
    # подключение к нашей базе
    conn = psycopg2.connect("""
        host=rc1d-9cjee2y71olglqhg.mdb.yandexcloud.net
        port=6432
        sslmode=verify-full
        dbname=sch58_db
        user=Admin
        password=atdhfkm2024
        target_session_attrs=read-write
    """)
except:
    print('connection error')

# посылаем запрос на подключение к конкретной таблице
request = 'SELECT * FROM "Galactic Empire"."Planets"'

# уснанавливаем связь с базой для выполнения запросов
cursor = conn.cursor()

# выполняем запрос
cursor.execute(request)

# табличку после запроса
data = cursor.fetchall()

print(data)

request_update = 'UPDATE "Galactic Empire"."Planets" SET "Name"=\'Earth\', "System"=2, "Population"=10000000, "Position"=3, "Type"=2 WHERE id=2'

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
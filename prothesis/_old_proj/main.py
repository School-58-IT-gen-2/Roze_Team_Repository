from Player_class import Player
from Game_class import Stage
import main_database

choice = input('Добро пожаловать в игру!\nenter - новая игра\nl - загрузить игру\n')
player = Player('тип')
if choice == 'l':
    stage = Stage(1, 'вы просыпаетесь посреди пустоты. песок, металлические обломки, все это вы уже видели однажды. вы чувствуете как горячий воздух наполняет ваше горло... горло? вы осматриваете себя и замечаете странные трубки в вашей груди и шее. дотронувшись до лица вы понимаетечто на лице респиратор. кажется вы теперь киборг... надо добраться до ближайшего населенного пункта как можно скорее, вы чувствуете что ваш кислород на исходе. путешествие начинается. ', player.load_from_file("player_data.json"))

    
elif choice == '':
    stage = Stage(1, 'вы просыпаетесь посреди пустоты. песок, металлические обломки, все это вы уже видели однажды. вы чувствуете как горячий воздух наполняет ваше горло... горло? вы осматриваете себя и замечаете странные трубки в вашей груди и шее. дотронувшись до лица вы понимаетечто на лице респиратор. кажется вы теперь киборг... надо добраться до ближайшего населенного пункта как можно скорее, вы чувствуете что ваш кислород на исходе. путешествие начинается. ', player)
else:
    print('вы не прошли проверку от дурака')
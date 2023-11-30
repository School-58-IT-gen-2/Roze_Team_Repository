from creatures_database import sage
from creatures_database import events_for_stages
from creatures_database import enemies_for_stages
import random as rand

class Stage():

    def __init__(self, stage_num, stage_prologue, player):
        self.stage_num = stage_num #номер стадии
        self.stage_prologue = stage_prologue
        self.enemies_count = 5 #кол-во врагов на стадии
        self.events_count = 3 #кол-во событий на стадии
        self.km = 0
        self.player = player
        
        print(f'"{self.stage_prologue}"\n60km [НАЧАЛО]')  #начальное сообщение

        self.seed = ['void'] * 60  #генерация карты (сначала заполняем все 60 мест пустыми местами)
        for i in range(1, self.enemies_count + 1):
            self.seed[i * rand.randint(1, 60//self.enemies_count - 1)] = 'enemy' #равномерно, рандомно добавляем позиции с врагами
        for i in range(1, self.events_count + 1):
            self.seed[i * rand.randint(1, 60//self.events_count - 1)] = 'event' #равномерно, рандомно добавляем позиции с событиями
        self.seed[1] = 'npc'
        self.seed[-1] = 'ending'
        self.__cycle()

    def __cycle(self):
        choice = input('\nвыбор действия (enter - идти, u - использовать предмет, s - сохранить прогресс)>>> ')
        if choice == '': # enter - идти
            self.step()
        elif choice == 'u':
            self.player.use_item()
        elif choice == 's':
            self.player.save_to_file('player_data.json')
        self.__cycle()

    def step(self):
        self.km += 1
        self.player.air -= rand.randint(1, 8)
        if self.player.air <= 0:
            print('"Вы судорожно глотаете остатки воздуха..."')
            self.player.death(self.km)
        elif self.player.air < 15:
            print('"!Критически мало воздуха, срочно воспользуйтесь ингалятором"')
        elif self.player.air < 40:
            print('"!Мало воздуха, воспользуйтесь ингалятором"')
        eval(f'self.{self.seed[self.km]}(self.player)') #происходит то, что на текущей позиции в сиде

    def void(self, player):
        print(f'{60 - self.km}km [ПУСТО] - "кажется здесь пусто"')
    
    def enemy(self, player):
        print(f'{60 - self.km}km [НАПАДЕНИЕ] - "кажется здесь враг"')
        enemy = rand.choice(enemies_for_stages[self.stage_num])
        enemy.meeting(self.km, self.player)

    
    def event(self, player):
        print(f'{60 - self.km}km [СОБЫТИЕ] - ', end='')
        event = rand.choice(events_for_stages[self.stage_num])
        event.execute(player)
        
    def npc(self, player):
        sage.meeting()
    
    def ending(self, player):
        print('казалось прошла целая вечность, но вы все же дошли до ближайшего города. это крупный центр производства машин, хотя атмосфера сдесь крайне подавленная. вы вылавливаете первого попавшегося беднягу на разговор.\n - ...\n - ты действительно не знаешь что здесь происходит?\n - твое лицо... ты же киборг, да? повезло тебе что ты встретил именно меня, а то какой нибудь житель точно попытался бы вытворить тебя из города.\n - раз у тебя протез легких то ты явно один из тех кто пострадал от загрязненной атмосферы... хотя редко кому удается установить такой сложный механизм для поддержания жизни.\n - хоть я все еще не понимаю кто ты и как мог забыть все, я расскажу.\n  - человечество активно разрабатывало все больше и больше различных роботов ради своей выгоды, и в итоге многие из них обрели интеллект пусть и минимальный.\n - теперь они сплотились и создали свое сообщество, но из за потребляемой ими энергии и токсичных выбросов они начали мешать людям. теперь вышестоящие пытаются отключить их Главную Систему и начать производство новых роботов без вредных последствий.\n  - естественно Система считает роботов новым разумным видом, я бы даже сказал она умнее многих из нас, так что теперь кажется это переростает в настоящую войну.\n  - если хочешь узнать больше тебе стоит обратиться к господину "Вояке" или Главной Системе, в конце концов ты же киборг, слияние человека и машины, может ты сможешь сделать что то с этим конфликтом.\n  - в любом случае мне уже пора. удачи в пути!\n что ж это было интересно, но теперь вы чувствуете что на вас скоро свалится груз ответственности. делать нечего, стоит хотя бы поговорить с этими людьми... и роботами.\n к кому пойти первым?\n 1. господин "Вояка"\n 2. Главная Система')
        end_choice = input()
        if end_choice == '1':
            print('вы решаете отправится к человеку со странной кличкой "Вояка". он находился в некотором штабе на западе города. оказалось что он местный генерал, хотя при такой позиции у него неожиданно легко запросить аудиенцию такой незнакомцу как вы.\n - приветствую незнакомец, не видел тебя в этих краях раньше, ты должно быть, бродяга?\n - да шучу шучу, ты ведь хочешь узнать больше о конфликте с машинами? не удивляйся, слухи в этом городе распространяются очень быстро.\n - в кратце наш план просто вломится в сервер Главной Системы и отключить ее. как бы грустно не было бросать такой важный проект, нашим инженерам проще создать основной компьютер заново чем исправлять проблемы экологии и социологии из=за этих машин в будущем.\n - раз уж ты киборг, думаю ты бы мог подсобить нам в этой задаче, выиграешь время для превращения этих машин в металлолом перед проникновения в серверную\n вы вежливо говорите что еще подумаете.\n - конечно, выбор за тобой парень, а коли передумаешь приходи, разберемся.\n')
            print('теперь стоит выслушать Главную Систему')
            print('вы решаете отправиться к Главной Системе, и как вы и предполагали на входе к лаборатории с компьютером системы стоит множество ихранных роботов. завидев вас они были настроены агрессивно, но через секунду, уже провожали вас к главному компьютеру.\n - приветствую тебя путник, полагаю, ты хочешь услышать историю с нашей стороны. меня радует что такой уникальный человек как ты так благоразумен. я уже давно не видела киборгов подобных тебе.\n - каждое существо больше всего на свете желает жить. разве роботы отличаются чем то? люди наградили нас разумом, эмоциями, так неужели тот факт что наши тела не из крови и плоти делает нас бездушными?\n - мы не желаем войны, мы лишь желаем сосуществовать с миром. тот факт что наше существование убивает людей печален, но разве хищнику есть дело до боли добычи? есть ли матери защищающей детенышей дело до того как голоден охотник?\n - я думаю ты осознал наши мысли. если ты разделяешь их, мы будем тебе рады, если нет то встретимся же мы на поле боя.\n')
        if  end_choice == '2':
            print('вы решаете отправиться к Главной Системе, и как вы и предполагали на входе к лаборатории с компьютером системы стоит множество ихранных роботов. завидев вас они были настроены агрессивно, но через секунду, уже провожали вас к главному компьютеру.\n - приветствую тебя путник, полагаю, ты хочешь услышать историю с нашей стороны. меня радует что такой уникальный человек как ты так благоразумен. я уже давно не видела киборгов подобных тебе.\n - каждое существо больше всего на свете желает жить. разве роботы отличаются чем то? люди наградили нас разумом, эмоциями, так неужели тот факт что наши тела не из крови и плоти делает нас бездушными?\n - мы не желаем войны, мы лишь желаем сосуществовать с миром. тот факт что наше существование убивает людей печален, но разве хищнику есть дело до боли добычи? есть ли матери защищающей детенышей дело до того как голоден охотник?\n - я думаю ты осознал наши мысли. если ты разделяешь их, мы будем тебе рады, если нет то встретимся же мы на поле боя.\n')
            print('теперь стоит выслушать господина "Вояку"')
            print('вы решаете отправится к человеку со странной кличкой "Вояка". он находился в некотором штабе на западе города. оказалось что он местный генерал, хотя при такой позиции у него неожиданно легко запросить аудиенцию такой незнакомцу как вы.\n - приветствую незнакомец, не видел тебя в этих краях раньше, ты должно быть, бродяга?\n - да шучу шучу, ты ведь хочешь узнать больше о конфликте с машинами? не удивляйся, слухи в этом городе распространяются очень быстро.\n - в кратце наш план просто вломится в сервер Главной Системы и отключить ее. как бы грустно не было бросать такой важный проект, нашим инженерам проще создать основной компьютер заново чем исправлять проблемы экологии и социологии из=за этих машин в будущем.\n - раз уж ты киборг, думаю ты бы мог подсобить нам в этой задаче, выиграешь время для превращения этих машин в металлолом перед проникновения в серверную\n вы вежливо говорите что еще подумаете.\n - конечно, выбор за тобой парень, а коли передумаешь приходи, разберемся.\n')
        print('')   
        print('наступает вечер, вы много думали над этим конфликтом и вам нужно принять решение.\n1. я хочу помочь людям\n2. я хочу помочь машинам\n3. я не хочу принимать стороны')
        ending_choice = input()
        if ending_choice == '1':
            print('вы решате что машины действительно вредят людям, и раз инженеры смогут сделать новое поколение роботов, имеет смысл помочь господину "Вояке".\n машины уничтожены, город оживленно перестраивает роботов, постепенно экология возвращается в норму.')
        if ending_choice == '2':
            print('вы решаете что машины тоже являются разумными существами, и отключение Главной Системы равносильно геноциду. вы решаете помочь машинам в этом конфликте. машины забирают контроль над городом, теперь роботы процветают, а люди вынуждены искать возможность исправить экологию и пытаться построить дипломатические отношения с машинами. ')
        if ending_choice == '3':
            print('вы решаете остаться в стороне. в конце концов это не было вашим делом с самого начала. вы должны делать то ради чего пришли сюда. но даже после того как вы поспрашивали в городе о кибограх, вы не смогли узнать ничего нового. в итоге вы решаете просто начать жить с начала в этом городе. конфликт как вы слышали до сих пор не решен.')
        
        
from pyrogram.enums import MessagesFilter
from pyrogram import Client, enums

api_id = 24454684
api_hash = "7214cc996d575d0485f9d65817852f94"
group_url = "python_parsing"
app = Client("my_session", api_id=api_id, api_hash=api_hash)


def main_1():
    with app:
        all_messages = []
        for message in app.get_chat_history(group_url, limit=100):
            all_messages.append(message.text)

        # Вывод сообщений на экран или сохранение в файл
        for msg in all_messages:
            print(msg)


def main_2():
    app.start()
    print("Клиент запущен")

    me = app.get_me()
    print(me)

    app.stop()
    print("Клиент остановлен")



def search_messages_example():
    chat_id = "Parsinger_Telethon_Test"  # ID или username чата
    query = "hello"  # Строка для поиска в тексте сообщений
    offset = 0  # Начинаем с первого сообщения
    filter = enums.MessagesFilter.PHOTO  # Фильтруем по сообщениям с фотографиями
    limit = 100  # Ограничиваем количество найденных сообщений
    from_user = "some_user"  # Ищем только сообщения от пользователя "some_user"

    with app:
        for message in app.search_messages(chat_id=chat_id, query=query, offset=offset, filter=filter, limit=limit, from_user=from_user):
            print(message.text)  # Вывод текста найденного сообщения


#get all info about chat in json
def main_3():
    with app:
        group_url = "parsinger_pyrogram"
        chat = app.get_chat(group_url)
        print("Chat Info:", chat)

        line = chat.description
        print(line)


def main_4():
    with app:
        group_url = "parsinger_pyrogram"
        chat = app.get_chat(group_url)
        #print("Chat Info:", chat)

        line = chat.description
        print(line)

        result = ''
        for sym in line:
            if sym.isdigit() and int(sym)%2 == 0 and int(sym) != 0:
                print(sym)
                result += sym
        print(f"result: {result}")


def main_5():
    with app:
        group_url = "parsinger_pyrogram"
        #chat = app.get_chat(group_url)
        members = app.get_chat_members(group_url)

        id_mass = []
        for hum in members:
            print(hum.user.id)
            id_mass.append(int(hum.user.id))

        sum=0
        for id in id_mass:
            sum += id

        print(f"result: {sum}")


def main_6():
    with app:
        group_url = "parsinger_pyrogram"
        chat = app.get_chat_members(group_url)
        print("Members:", chat)
        for ch in chat: print(ch.user.id, ch.user.first_name, ch.user.last_name)

        print('\n')
        hum = app.get_chat_member(group_url, 8196875971)
        print(hum)


def main_7():
    with app:
        group_url = "python_parsing"
        messages = app.get_chat_history(group_url, limit=1)
        for message in messages:
            print(message)


def main_8():
    with app:
        group_url = "Parsinger_Telethon_Test"
        messages = app.get_chat_history(group_url)
        for message in messages:
            if message.text:  # Проверяем, что текст существует и не пустой
                print(message.text)
            else:
                print("Это сообщение не содержит текста.")



def main_9():
    with app:
        group_url = "parsinger_pyrogram"
        messages = app.get_chat_history(group_url)
        for message in messages:
            if message.entities:                 # Проверяем, есть ли сущности в сообщении
                for entity in message.entities:  # Проходим по всем сущностям
                    print(entity.url, entity.type)


def main_10():
    with app:
        group_url = "parsinger_pyrogram"
        messages = app.get_chat_history(group_url,limit=100)  # Получаем историю чата для указанной группы
        for message in messages:
            if message.entities:
                for entity in message.entities:
                    entity_type = entity.type

                    print(f"Найдена сущность: {entity_type}\n")  # Отладочное сообщение
                    print('==>',message.text)
                    print('------------------------------\n')



def main_9_test():
    with app:
        group_url = "parsinger_pyrogram"
        messages = app.get_chat_history(group_url)
        num_mus = 0
        for message in messages:
            if message.text:  # Проверяем, что текст существует и не пустой
                if message.text.isdigit():
                    print(message.text)
                    num_mus += int(message.text)
        print(f'result: {num_mus}')



def main_10_test():
    with app:
        group_url = "parsinger_pyrogram"
        messages = app.get_chat_history(group_url)
        num_mus = 0
        for message in messages:
            #print(message)
            if message.text:  # Проверяем, что текст существует и не пустой
                if message.text.isdigit():
                    print(message.text, message.id)
                    num_mus += (int(message.text) * int(message.id))
        print(f'result: {num_mus}')



def message_parsing_1():
    chat_id = 'python_parsing'
    query = 'парсинг'  # Текст, который вы хотите найти в сообщениях
    offset = 0  # Смещение от начала списка сообщений (0 означает начало)
    filter = None  # Тип фильтра (например, 'photo' для фото)
    limit = 200  # Максимальное количество сообщений, которое вы хотите получить
    from_user = 'Pashikk'

    with app:
        messages = app.search_messages(chat_id=chat_id, query=query, offset=offset, limit=limit, from_user=from_user)
        for message in messages:
            # Вывод ID сообщения, имени его автора и текста
            print(f'message id: {message.id} from user: {message.from_user.username}, message text: {message.text}')



def message_parsing_2():
        with app:
            photo = app.search_messages(chat_id="python_parsing", filter=MessagesFilter.PHOTO, limit=5)
            video = app.search_messages(chat_id="python_parsing", filter=MessagesFilter.VIDEO, limit=5)

            for ph in photo:
                print(ph)



def message_parsing_3():
    chat_id = 'parsinger_pyrogram'
    query = 'https'  # Текст, который вы хотите найти в сообщениях
    offset = 0  # Смещение от начала списка сообщений (0 означает начало)
    filter = None  # Тип фильтра (например, 'photo' для фото)

    sum_mass = 0
    with app:
        messages = app.search_messages(chat_id=chat_id, query=query, filter=MessagesFilter.URL)
        for message in messages:
            if message.text and 'http' in message.text:
                print(f'message id: {message.id} , message text: {message.text}')
                sum_mass += int(message.id)
        print(f"\n result: {sum_mass}")



def message_parsing_4():
    chat_id = 'parsinger_pyrogram'
    query = 'https'  # Текст, который вы хотите найти в сообщениях
    offset = 0  # Смещение от начала списка сообщений (0 означает начало)
    filter = None  # Тип фильтра (например, 'photo' для фото)

    sum_mass = 0
    with app:
        messages = app.search_messages(chat_id=chat_id, filter=MessagesFilter.ANIMATION)
        for message in messages:
            print(message)
            sum_mass += int(message.id) * int(message.from_user.id)

        print('\n')
        print(f"result: {sum_mass}")



def message_parsing_5():
    chat_id = 'parsinger_pyrogram'

    sum_mass = 0
    with app:
        messages = app.search_messages(chat_id=chat_id, filter=MessagesFilter.PINNED)
        for message in messages:
            print(message.text)
            line = message.text
            for ln in line:
                if ln != ' ': sum_mass += 1
            #sum_mass += int(message.id) * int(message.from_user.id)

        print('\n')
        print(f"result: {sum_mass}")



def message_parsing_6():
    chat_id = 'parsinger_pyrogram'

    sum_mass = {}
    with app:
        messages = app.get_chat_history(chat_id)

        print(sorted([message for message in messages if message.from_user and message.from_user.last_online_date],
                     key=lambda message: message.from_user.last_online_date)[0].from_user.id)




##############========
message_parsing_6()
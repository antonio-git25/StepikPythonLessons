from pyrogram.enums import MessagesFilter
from pyrogram import Client, enums
from tqdm import tqdm
import os

api_id = 24454684
api_hash = "7214cc996d575d0485f9d65817852f94"
group_url = "python_parsing"
app = Client("my_session", api_id=api_id, api_hash=api_hash)

def calculate_directory_size(path):
    """
    Подсчитывает размер всех файлов в директории.
    :param path: Путь к директории, размер файлов которой нужно подсчитать.
    :return: Общий размер файлов в байтах.
    """
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size


def progress(current, total, progress_bar):
    # Обновляем прогресс-бар
    progress_bar.update(current - progress_bar.n)


def main_photo():
    with app:
        for message in app.get_chat_history(group_url):
            # Проверяем, содержит ли сообщение изображение
            if message.new_chat_photo:
                # Скачиваем изображение
                app.download_media(message.new_chat_photo, file_name=f"anime/{message.from_user.id}_{message.id}.jpg")


def main():
    with app:
        for message in app.get_chat_history(group_url):
            if message.media:
                file_name = f"media/{message.id}"
                file_size = None

                # Определение расширения файла и размера в зависимости от типа медиа
                if message.audio:
                    file_name += ".mp3"
                    file_size = message.audio.file_size
                elif message.document:
                    file_name += f".{message.document.mime_type.split('/')[-1]}"
                    file_size = message.document.file_size
                elif message.voice:
                    file_name += ".ogg"
                    file_size = message.voice.file_size
                elif message.sticker:
                    file_name += ".webp"
                    file_size = message.sticker.file_size
                elif message.animation:
                    file_name += ".mp4"
                    file_size = message.animation.file_size

                # Создание прогресс-бара для каждого файла
                # Если размер файла определен, создаем прогресс-бар и начинаем загрузку
                if file_size:
                    with tqdm(total=file_size, unit='B', unit_scale=True, desc="Скачивание") as progress_bar:
                        app.download_media(message, file_name=file_name, progress=progress, progress_args=(progress_bar,))


#result 194911917 is wrong
def get_size_photo():
    with app:
        for message in app.get_chat_history(group_url):
            if message.photo:
                #app.download_media(message.photo, file_name=f"photo/{message.from_user.id}_{message.id}.jpg")
                app.download_media(message.photo, file_name=f"photo_2/{message.id}_{message.from_user.id}.jpg")

        full_path = "C:/Users/Antonio/PycharmProjects/PythonStepikAPI/Pyrogram/photo_2"
        result = calculate_directory_size(full_path)
        print(f"result: {result}")


def get_sixe():
    full_path = "C:/Users/Antonio/PycharmProjects/PythonStepikAPI/Pyrogram/photo"
    result = calculate_directory_size(full_path)
    print(f"result: {result}")


##############========
get_sixe()
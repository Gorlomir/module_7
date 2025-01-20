import os
import time


def process_directory(directory):
    ignore_directories = ['.venv', '__pycache__', 'build', 'dist', '*.egg-info', '.git'] # Список директорий, которые надо игнорировать

    for root, dirs, files in os.walk(directory):

        dirs[:] = [d for d in dirs if not any(d.startswith(ignore) for ignore in ignore_directories)] #удаление

        for file in files:
            filepath = os.path.join(root, file)
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)

            print(
                f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: '
                f'{formatted_time}, Родительская директория: {parent_dir}')

directory = "."
process_directory(directory)
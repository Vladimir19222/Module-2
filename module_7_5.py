import os
import time

parent_dir = os.path.dirname(os.getcwd())
directory = '../games'  # '..\module2'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory, file)
        mtime = os.path.getmtime(filepath)
        named_tuple = time.localtime(mtime)
        formatted_time = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        filesize = os.path.getsize(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize}, байт, Время изменения: {formatted_time}',
             f'Родительская директория: {parent_dir}')

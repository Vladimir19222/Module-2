from datetime import datetime
from threading import Thread
import time


def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(word_count):
            f.write('Какое-то слово № ' + str(i + 1) + '\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')

time_start = datetime.now()
thread1 = Thread(target=write_words, args=(10, 'example5.txt'),)
thread2 = Thread(target=write_words, args=(30, 'example6.txt'),)
thread3 = Thread(target=write_words, args=(200, 'example7.txt'),)
thread4 = Thread(target=write_words, args=(100, 'example8.txt'),)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')

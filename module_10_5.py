import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start = datetime.datetime.now()
for x in filenames:
    read_info(x)
end = datetime.datetime.now()
print(end - start, '(линейный)')

# Многопроцессный вызов
if __name__ == '__main__':
    start = datetime.datetime.now()
    n = len(filenames)
    with multiprocessing.Pool(processes=n) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start, '(многопроцессный)')

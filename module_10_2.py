from threading import Thread
import time


class Knight(Thread):
    number_of_enemy = 100
    number_of_days = 0

    def __init__(self, name, power):
        super().__init__()
        self.power = power
        self.name = name

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.number_of_enemy > 0:
            self.number_of_enemy -= self.power
            if self.number_of_enemy < self.power:
                self.number_of_enemy = 0
            self.number_of_days += 1
            print(f'{self.name} сражается {self.number_of_days} день(дня)..., осталось {self.number_of_enemy} воинов.\n')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {self.number_of_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились')

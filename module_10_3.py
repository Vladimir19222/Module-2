import threading
from threading import Thread, Lock
from random import randint
import time


class Bank:
    balance = int()
    lock = Lock()

    def __init__(self):
        super().__init__()

    def deposit(self):
        a = randint(50, 500)
        self.balance += a
        print(f'Пополнение:{a}. Баланс: {self.balance}\n')
        time.sleep(0.01)

    def take(self):
        b = randint(50, 500)
        print(f'Запрос на {b}')
        if b <= self.balance:
            self.balance -= b
            print(f'Снятие:{b}. Баланс: {self.balance}\n')
        else:
            self.lock.acquire()
            try:
                print('Запрос отклонён, недостаточно средств\n')
            finally:
                self.lock.release()
        time.sleep(0.01)


bk = Bank()

for i in range(100):
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

print(f'Итоговый баланс: {bk.balance}')

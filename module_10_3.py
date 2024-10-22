import time
from threading import Thread, Lock
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            num_append = randint(50, 500)
            self.balance += num_append
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {num_append}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            num_lower = randint(50, 500)
            print(f'Запрос на {num_lower}')
            if num_lower <= self.balance:
                self.balance -= num_lower
                print(f'Снятие: {num_lower}. Баланс: {self.balance}')
            elif num_lower > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
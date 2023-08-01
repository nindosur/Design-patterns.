    # 1
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print(f'Объект создан, {s}')
b = Singleton()
print(f'Объект создан, {b}')

    # 2
from decimal import *

text = {"total": 9.61, "items": ["Омлет", "Чай"]}
# text - имеет формат json
# формирует строку в вормат UNICODE

class Factory(object):
    def build_sequence(self):           # для работы со всеми типами данных
        return []

    def build_number(self, string):     # для работы с числами
        return Decimal(string)

class Loader(object):
    def load(string, factory):
        sequence = factory.build_sequence()
        for substring in string.split(','):
            item = factory.build_number(substring)
            sequence.append(item)
        return sequence

f = Factory()
result = Loader.load('1.23, 4.56', f)
print(result)

    # 3
class Logger:
    __instance = None

    def __new__(cls, log_type):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.log_type = log_type
        return cls.__instance

    def log(self, message):
        if self.log_type == 'file':
            with open("log.txt", 'a') as log_file:
                log_file.write(message + '\n')
        elif self.log_type == 'screen':
                print(message)
        else:
            raise ValueError("Ошибка!!!")

class NumberProcessor:

    def __init__(self, logger):
        self.numbers = []
        self.logger = logger

    def process_numbers(self, file_path):
        with open(file_path, "w") as file:
            file.write("Числа:\n")
            while True:
                num = input("Введите число, для выхода напишите 'Q': ")
                if num.upper() == "Q":
                    break
                try:
                    num = int(num)
                    self.numbers.append(num)
                    file.write(str(num) + "\n")
                except ValueError:
                    print("Неверный ввод!!!")
                    self.logger.log("Пользователь при вводе цифр, ввел некорректное значение.")

            max_num = max(self.numbers)
            min_num = min(self.numbers)
            file.write(f"Максимальное число: {max_num}\n")
            file.write(f"Минимальное число: {min_num}\n")

            self.logger.log(f"Все числа: {self.numbers}")
            self.logger.log(f"Максимальное число: {max_num}")
            self.logger.log(f"Минимальное число: {min_num}")

            print("Все числа:", self.numbers)
            print("Максимальное число:", max_num)
            print("Минимальное число:", min_num)


logger = Logger('file')
logger_screen = Logger('screen')
processor = NumberProcessor(logger)
processor.process_numbers("output.txt")


import os
import sys


def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "По указанному значению совпадений не найдено"
    return "\n".join(result)


def transfer_data(source: str, dest: str, num_row: int, mode: int):
    """
    Функция для переноса указанной строки из одного файла
    в другой
    source: str - имя исходного файла
    dest: str - имя файла куда переносим
    num_row: int - номер переносимой строки
    """
    f = open(source, 'r')
    i = 1
    text = ""
    if os.path.isfile(dest):
        w = open(dest, 'a')
    else:
        w = open(dest, 'w')
    for line in f:
        if i == num_row:
            w.write(line)
        elif mode == 2:
            text += line
        i += 1
    if mode == 2:
        w2 = open(source, 'w')
        w2.write(text)


INFO_STRING = """
Выберите ркжим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
5 - выход из программы
"""

file = "text.txt"
loop = True

if file not in os.listdir():
    print("указанное имя файла отсутсвует")
    sys.exit()


while loop:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))
    elif mode == 2:
        name = input("Введите Ваше имя: ")
        phone = input("Введите Ваш телефон: ")
        add_new_user(name, phone, file)
    elif mode == 3:
        data = input("Введите значение: ")
        print(search_user(file, data))
    elif mode == 4:
        # Тут нужно вызвать функцию с аргументами
        source = input("Введите путь до исходного файла: ")
        dist = input("Введите путь файла для переноса: ")
        row_num = int(input("Введите номер строки: "))
        mode = int(input("Введите модель поведения (1 - копирование, 2 - перенос): "))
        transfer_data(source, dist, row_num, mode)
    elif mode == 5:
        loop = False

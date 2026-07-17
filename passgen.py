#RU: Автором программы является Gibstep; профиль автора на GitHub находится по адресу https://github.com/Gibstep. Программа распространяется по лицензии GNU GPL v3.0.
#EN: The program is authored by Gibsteb; the author’s GitHub profile is at https://github.com/Gibstep . The program is distributed under the GNU GPL v3.0 license.

#Импорт библиотек
import random as rd
import string as stng
import secrets

#переменные
wrk = True #пока значение true код выполняется
chars = stng.ascii_letters + stng.digits + stng.punctuation #все символы - латиница, цифры и спецсимволы
cyrillic = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" #кириллица

#основной код:
while wrk:
    #выбор типа пароля
    selct0 = input('''
    Здравстуйте, какой тип пароля вы хотите сгенерировать?
    1) Пин-код
    2) Буквенный (латиница)
    3) Буквенный (кириллица)
    4) Надежный (латиница, цифры и спецсимволы)
    5) завершить работу программы
    Ввод: ''')
    #генерация и выбор длинны
    if selct0 == "1":
        #выбор длинны
        selct1 = input('''
        Выберите длинну пароля:
        1) 6 символов 
        2) 7 символов
        3) 8 символов
        Ввод: ''')
        #генерация
        if selct1 == "1":
             passwd = ''.join(str(rd.randint(0, 9)) for _ in range(6))
             print(passwd)
        if selct1 == "2":
             passwd = ''.join(str(rd.randint(0, 9)) for _ in range(7))
             print(passwd)
        if selct1 == "3":
             passwd = ''.join(str(rd.randint(0, 9)) for _ in range(8))
             print(passwd)
    if selct0 == "2":
        #выбор длинны
        selct1 = input('''
        Выберите длинну пароля:
        1) 6 символов 
        2) 7 символов
        3) 8 символов
        Ввод: ''')
        #генерация
        if selct1 == "1":
             passwd = ''.join(secrets.choice(stng.ascii_letters) for _ in range(6))
             print(passwd)
        if selct1 == "2":
             passwd = ''.join(secrets.choice(stng.ascii_letters) for _ in range(7))
             print(passwd)
        if selct1 == "3":
             passwd = ''.join(secrets.choice(stng.ascii_letters) for _ in range(8))
             print(passwd)
    if selct0 == "3":
        #выбор длинны
        selct1 = input('''
        Выберите длинну пароля:
        1) 6 символов 
        2) 7 символов
        3) 8 символов
        Ввод: ''')
        #генерация
        if selct1 == "1":
             passwd = ''.join(secrets.choice(cyrillic) for _ in range(6))
             print(passwd)
        if selct1 == "2":
             passwd = ''.join(secrets.choice(cyrillic) for _ in range(7))
             print(passwd)
        if selct1 == "3":
             passwd = ''.join(secrets.choice(cyrillic) for _ in range(8))
             print(passwd)
    if selct0 == "4":
        #выбор длинны
        selct1 = input('''
        Выберите длинну пароля:
        1) 6 символов 
        2) 7 символов
        3) 8 символов
        Ввод: ''')
        #генерация
        if selct1 == "1":
             passwd = ''.join(secrets.choice(chars) for _ in range(6))
             print(passwd)
        if selct1 == "2":
             passwd = ''.join(secrets.choice(chars) for _ in range(7))
             print(passwd)
        if selct1 == "3":
             passwd = ''.join(secrets.choice(chars) for _ in range(8))
             print(passwd)
    if selct0 == "5":
        wrk = False #завершение работы программы

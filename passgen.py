#RU: Автором программы является Virxxon; профиль автора на GitHub находится по адресу https://github.com/Virxxon . Программа распространяется по лицензии GNU GPL v3.0.
#EN: The program is authored by Virxxon; the author’s GitHub profile is at https://github.com/Virxxon . The program is distributed under the GNU GPL v3.0 license.

#Импорт библиотек
#Imports
import random as rd
import string as stng
import secrets

#переменные
#Variables
wrk = True #пока значение true код выполняется/The code runs while the value is true
chars = stng.ascii_letters + stng.digits + stng.punctuation #все символы - латиница, цифры и спецсимволы/Latin letters, digits, special symbols
cyrillic = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" #кириллица/Cyrillic

#основной код:
#Main:
while wrk:
    #выбор типа пароля
    #Select password type
    selct0 = input('''
    Hello! What type of password would you like to generate?

    1) PIN code
    2) Letters only (Latin)
    3) Letters only (Cyrillic)
    4) Strong password (Latin letters, numbers, and special characters)
    5) Exit the program

    Input (option number): ''')
    #генерация и выбор длинны
    #Generate and choose the length
    if selct0 == "1":
        #выбор длинны
        #Choose the length
        selct1 = input('''
        Choose the password length:

        1) 6 characters
        2) 7 characters
        3) 8 characters
        
        Input (option number): ''')
        #генерация
        #Generation
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
        #Choose the length
        selct1 = input('''
        Choose the password length:

        1) 6 characters
        2) 7 characters
        3) 8 characters
        
        Input (option number): ''')
        #генерация
        #Generation
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
        #Choose the length
        selct1 = input('''
        Choose the password length:

        1) 6 characters
        2) 7 characters
        3) 8 characters
        
        Input (option number): ''')
        #генерация
        #Generation
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
        #Choose the length
        selct1 = input('''
        Choose the password length:

        1) 6 characters
        2) 7 characters
        3) 8 characters
        
        Input (option number): ''')
        #генерация
        #Generation
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
        wrk = False #завершение работы программы/Exit the program

"""функции для генерации пароля и логина"""
import random


def generate_password():
    """generate password for 10 digits"""
    password = ""
    for i in range(10):
        password += str(random.randint(0, 9))
    return password


def generate_login():
    """generate login for 10 letters"""
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    login = "Andrey_05_"
    for i in range(10):
        login += random.choice(letters)
    login += "@ya.ru"
    return login

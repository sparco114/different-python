# -*- coding: utf-8 -*-
from random import randint

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):

    def __init__(self, input_data=None):
        self.input_data = input_data

    def __str__(self):
        return f'Я - Бог. Аргументы: {self.input_data}'


class DrunkError(Exception):
    def __init__(self, input_data=None):
        self.input_data = input_data

    def __str__(self):
        return f'Перепил. Аргументы: {self.input_data}'


class CarCrashError(Exception):
    def __init__(self, input_data=None):
        self.input_data = input_data

    def __str__(self):
        return f'Попал в аварию. Аргументы: {self.input_data}'


class GluttonyError(Exception):
    def __init__(self, input_data=None):
        self.input_data = input_data

    def __str__(self):
        return f'Объелся. Аргументы: {self.input_data}'


class DepressionError(Exception):
    def __init__(self, input_data=None):
        self.input_data = input_data

    def __str__(self):
        return f'Впал в депрессию. Аргументы: {self.input_data}'


class SuicideError(Exception):
    def __init__(self, input_data=None):
        self.input_data = input_data

    def __str__(self):
        return f'Совершил суицид. Аргументы: {self.input_data}'


def one_day():
    carma = 0
    cube = randint(1, 13)
    if 1 <= cube <= 7:
        carma = randint(1, 7)
    elif cube == 8:
        raise IamGodError(cube)
    elif cube == 9:
        raise DrunkError(cube)
    elif cube == 10:
        raise CarCrashError(cube)
    elif cube == 11:
        raise GluttonyError(cube)
    elif cube == 12:
        raise DepressionError(cube)
    elif cube == 13:
        raise SuicideError(cube)
    return carma


carm = 0
days = 0
while carm < ENLIGHTENMENT_CARMA_LEVEL:
    days += 1
    print(f'-------day {days}-------')
    try:
        res = one_day()
        print('+1')
        carm += res
    except Exception as exc:
        with open('err_days.txt', mode='a') as ff:
            ff.write(f'Day {days}: {exc}\n')
            print(f'ОШИБКА: {exc}')

print(carm)

# https://goo.gl/JnsDqu

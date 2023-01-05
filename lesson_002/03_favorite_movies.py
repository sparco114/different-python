#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

from pprint import pprint

first = my_favorite_movies[:10]
last = my_favorite_movies[-15:]
second = my_favorite_movies[12:25]
sec_from_end = my_favorite_movies[-22:-17]


print(f'{first}, {last}, {second}, {sec_from_end}')



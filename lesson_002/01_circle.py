#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

p = 3.1415926
s = p * radius ** 2
print('1 - Площадь круга: ', round(s, 4))

# Далее, пусть есть координаты точки
point = (23, 34)

x = point[0]
y = point[1]
d = (x ** 2 + y ** 2) ** .5
result = d < radius

# print(d, radius)
print('2 - Точка 1 внутри круга: ', result)

# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False

# Аналогично для другой точки
point_2 = (30, 30)

x2 = point_2[0]
y2 = point_2[1]

d2 = (x2 ** 2 + y2 ** 2) ** .5

result2 = d2 < radius
print('3 - Точка 2 внутри круга: ', result2)

# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.


# Пример вывода на консоль:
#
# 77777.7777
# False
# False


#final commit
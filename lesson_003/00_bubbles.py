# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(600, 300)
# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(center_position=point, radius=radius, width=2)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(poi, ste, rad, col):
    for _ in range(3):
        rad += ste
        sd.circle(center_position=poi, radius=rad, width=2, color=col)


step = 5
point = sd.get_point(600, 300)
radius = 50
bubble(poi=point, ste=step, rad=radius, col=[0, 0, 0])
#
# # Нарисовать 10 пузырьков в ряд
for x in range(100, 1000, 100):
    point = sd.get_point(x, 200)
    bubble(poi=point, ste=step, rad=radius, col=[200, 200, 100])



# def bub_line(x):
#     for _ in range(10):
#         pos = sd.get_point(x, 500)
#         sd.circle(center_position=pos)
#         x += 110
#
#
# rad = 80
# bub_line(x=rad)

# Нарисовать три ряда по 10 пузырьков
for y in range(100, 400, 100):
    for x in range(100, 1100, 100):
        point = sd.get_point(x, y)
        bubble(poi=point, ste=step, rad=radius, col=[200, 200, 100])

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for x in range(100):
    point = sd.random_point()
    color = sd.random_color()
    # step = sd.random_number(5, 10)
    step = random.randint(5, 10)

    bubble(poi=point, col=color, rad=50, ste=step)


sd.pause()



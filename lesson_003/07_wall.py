# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

for gorizont in range(50, 650, 50):
    sp = sd.get_point(0, gorizont)
    ep = sd.get_point(1200, gorizont)
    sd.line(sp, ep)

for x in range(50, 600, 100):
    ys = 0
    yf = 50
    for _ in range(0, 6, 1):
        start = sd.get_point(x, ys)
        end = sd.get_point(x, yf)
        sd.line(start, end)
        ys += 100
        yf += 100

for x in range(100, 600, 100):
    ys = 50
    yf = 100
    for _ in range(0, 6, 1):
        start = sd.get_point(x, ys)
        end = sd.get_point(x, yf)
        sd.line(start, end)
        ys += 100
        yf += 100

sd.pause()

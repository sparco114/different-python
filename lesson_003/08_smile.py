# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, col):
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=70, color=col, width=1)
    sd.ellipse(sd.get_point(x - 40, y + 25), (sd.get_point(x - 20, y + 35)), color=col, width=0)
    sd.ellipse(sd.get_point(x + 40, y + 25), (sd.get_point(x + 22, y + 35)), color=col, width=1)
    one = sd.get_point(x - 35, y - 30)
    two = sd.get_point(x - 20, y - 40)
    three = sd.get_point(x + 20, y - 40)
    four = sd.get_point(x + 35, y - 30)
    sd.lines([one, two, three, four], color=col, width=1, closed=False)


smile(100, 200, sd.COLOR_YELLOW)
smile(500, 300, sd.COLOR_RED)
smile(300, 400, sd.COLOR_GREEN)
smile(200, 500, sd.COLOR_DARK_ORANGE)


sd.pause()

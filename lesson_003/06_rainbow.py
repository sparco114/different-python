# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
sp = 50
epy = 350
step = 5

for col in rainbow_colors:
    start = sd.get_point(50, sp)
    end = sd.get_point(350, epy)
    sd.line(start_point=start, end_point=end, color=col, width=4)
    sp += step
    epy += step




# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


rad = 600
for col in rainbow_colors:
    point = sd.get_point(500, -150)
    sd.circle(center_position=point, color=col, width=20, radius=rad)
    rad += 20

sd.pause()

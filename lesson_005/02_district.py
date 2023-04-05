# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import district.soviet_street.house1.room1 as ss_h1_r1
import district.soviet_street.house1.room2 as ss_h1_r2
from district.soviet_street.house2 import room1 as ss_h2_r1
from district.soviet_street.house2 import room2 as ss_h2_r2
import district.central_street.house1.room1 as cs_h1_r1
import district.central_street.house1.room2 as cs_h1_r2
import district.central_street.house2.room1 as cs_h2_r1
import district.central_street.house2.room2 as cs_h2_r2

all_people = ss_h1_r1.folks + ss_h1_r2.folks + ss_h2_r1.folks + ss_h2_r2.folks + cs_h2_r1.folks + cs_h2_r2.folks + cs_h1_r1.folks + cs_h1_r2.folks

# print(len(all_people))


print(f"На районе живут: {', '.join(all_people)}")

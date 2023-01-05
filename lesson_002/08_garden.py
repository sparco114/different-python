#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint
# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
all = meadow_set | garden_set
print(all)

# выведите на консоль те, которые растут и там и там

gm = garden_set & meadow_set
print(gm)

# выведите на консоль те, которые растут в саду, но не растут на лугу
allgg = garden_set - meadow_set
print(f'GARDEN: {allgg}')

# выведите на консоль те, которые растут на лугу, но не растут в саду
allM = meadow_set - garden_set
print(f'MEADOW: {allM}')
#print(allM)



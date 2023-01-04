#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

mskX = sites['Moscow'][0]
lonX = sites['London'][0]
parX = sites['Paris'][0]
mskY = sites['Moscow'][1]
lonY = sites['London'][1]
parY = sites['Paris'][1]

msk_lon = ((mskX - lonX) ** 2 + (mskY - lonY) ** 2) ** 0.5
msk_par = ((mskX - parX) ** 2 + (mskY - parY) ** 2) ** 0.5

distances['MOSCOW'] = {}
distances['MOSCOW']['TO LONDON'] = msk_lon
distances['MOSCOW']['TO PARIS'] = msk_par

lon_par = ((lonX - parX) ** 2 + (lonY - parY) ** 2) ** .5

distances['LONDON'] = {}
distances['LONDON']['TO MOSCOW'] = msk_lon
distances['LONDON']['TO PARIS'] = lon_par

distances['PARIS'] = {}
distances['PARIS']['TO MOSCOW'] = msk_par
distances['PARIS']['TO LONDON'] = lon_par

pprint(distances)


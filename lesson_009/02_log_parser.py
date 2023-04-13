# -*- coding: utf-8 -*-
from pprint import pprint


# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class LogParser:

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def parse_day(self):
        st, fn = 1, 11
        self.parse_nok(st, fn)

    def parse_hour(self):
        st, fn = 1, 14
        self.parse_nok(st, fn)

    def parse_minutes(self):
        st, fn = 1, 17
        self.parse_nok(st, fn)

    def parse_nok(self, st, fn):
        with open(self.input_file, mode='r') as events:
            res = {}
            for line in events:
                if 'NOK' in line:
                    date = line[st:fn]
                    if date in res:
                        res[date] += 1
                    else:
                        res[date] = 1
        self.write_out(res)

    def write_out(self, res):
        with open(self.output_file, mode='w', encoding='utf-8') as file_out:
            for k, v in res.items():
                file_out.write(f'[{f"{k}:00-{int(k[-2:]) + 1}:00" if len(k) == 13 else k}] {v}\n')


pars = LogParser(input_file='events.txt', output_file='result.txt')

# pars.parse_day()
# pars.parse_hour()
pars.parse_minutes()


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

# -*- coding: utf-8 -*-
import time
import os
from threading import Thread


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#

class TradeStatistic(Thread):

    def __init__(self, file_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_path = file_path
        self.zero_volat = None
        self.no_zero_volat = []

    def run(self):
        self._files_scaner()

    def _files_scaner(self):
        with open(file=self.file_path, mode='r', encoding='utf-8') as ff:
            res = ff.readlines()
            prices = []
            for line in res[1:len(res)]:
                line = line.split(',')
                prices.append(float(line[2]))
            average_price = (max(prices) + min(prices)) / 2
            volatility = round((((max(prices) - min(prices)) / average_price) * 100), 2)
            if volatility == 0:
                self.zero_volat = line[0]
            else:
                self.no_zero_volat = (line[0], volatility)


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate


folder_name = './trades/'


@time_track
def main(folder):
    for dirpath, dirname, filenames in os.walk(folder):
        one_file = [TradeStatistic(file_path=os.path.join(dirpath, file)) for file in filenames]
        zero_volat_final = []
        no_zero_volat_final = []
        for file in one_file:
            file.start()
        for file in one_file:
            file.join()
        for file in one_file:
            if file.zero_volat is not None:
                zero_volat_final.append(file.zero_volat)
            else:
                no_zero_volat_final.append((file.no_zero_volat[0], file.no_zero_volat[1]))
        zero_volat_final.sort()
        no_zero_volat_final.sort(key=lambda x: x[1])
        print('Максимальная волатильность:')
        for i in range(1, 4):
            print(f'{no_zero_volat_final[-i][0]} - {no_zero_volat_final[-i][1]} %')
        print('Минимальная волатильность:')
        for i in range(3):
            print(f'{no_zero_volat_final[i][0]} - {no_zero_volat_final[i][1]} %')
        print('Нулевая волатильность:')
        print(str(zero_volat_final))


main(folder_name)

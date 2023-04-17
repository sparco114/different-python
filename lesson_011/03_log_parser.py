# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

def parse_nok():
    res = {}
    with open('events-.txt', mode='r') as events:
        prev_date = None
        for line in events:
            date = line[1:17]
            if 'NOK' in line:
                if date == prev_date:
                    res[date] += 1
                else:
                    if prev_date:
                        yield prev_date, res[prev_date]
                    res[date] = 1
                    prev_date = date
        if prev_date:
            yield prev_date, res[prev_date]
        else:
            raise StopIteration


grouped_events = parse_nok()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
    # with open('result.txt', mode='a') as ff:
    #     ff.write(f'{group_time} {event_count}\n')

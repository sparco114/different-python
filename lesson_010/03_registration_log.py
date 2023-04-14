# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

#
class NotNameError(Exception):

    def __init__(self, input_data):
        self.input_data = input_data

    def __str__(self):
        return f'Имя содержит не только буквы'


class NotEmailError(Exception):

    def __init__(self, input_data):
        self.input_data = input_data

    def __str__(self):
        return f'Неверно указан email'


def check_line(new_line):
    new_line = new_line[:-1].split(" ")
    if len(new_line) != 3:
        raise ValueError(f'Не все поля заполнены')
    else:
        if not new_line[0].isalpha():
            raise NotNameError(new_line)
        if not (('@' in new_line[1]) and ('.' in new_line[1])):
            raise NotEmailError(new_line)
        if not (10 <= int(new_line[2]) <= 99):
            raise ValueError(f'Некорректно указан возраст')


with open('registrations.txt', mode='r') as ff, open('reg_error.txt', mode='a', encoding='utf-8') as outf:
    err_count = 0
    for line in ff:
        try:
            check_line(line)
        except NotNameError as exc:
            outf.write(f'{exc} for {line}')
            err_count += 1
        except NotEmailError as exc:
            outf.write(f'{exc} for {line}')
            err_count += 1
        except ValueError as exc:
            outf.write(f'{exc} for {line}')
            err_count += 1
    outf.write(f'ERRORS: {err_count}')

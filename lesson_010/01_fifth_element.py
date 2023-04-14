# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

while True:
    try:
        input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
        leeloo = int(input_data[4])
        result = BRUCE_WILLIS / leeloo
        print(f"- Leeloo Dallas! Multi-pass № {result}!")
        break
    except ValueError as exc:
        print('невозможно преобразовать к числу')
    except IndexError as exc:
        print('выход за границы списка, нужно больше символов')
    except Exception as exc:
        print(f'другое: {exc}')


# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение

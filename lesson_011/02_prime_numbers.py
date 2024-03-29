# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, num):
        self.num = num
        self.prime_numbers = []

    def __iter__(self):
        return self

    def __next__(self):
        for numb in range(2, self.num + 1):
            for prime in self.prime_numbers:
                if numb % prime == 0:
                    break
            else:
                self.prime_numbers.append(numb)
                return numb
        raise StopIteration

    def __str__(self):
        return str(self.prime_numbers)


prime_number_iterator = PrimeNumbers(num=10)
for number in prime_number_iterator:
    print(number)

print(prime_number_iterator)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for nu in range(2, n + 1):
        for prime in prime_numbers:
            if nu % prime == 0:
                break
        else:
            prime_numbers.append(nu)
            yield nu
    return


for number in prime_numbers_generator(n=10):
    print(number)

print(list(prime_numbers_generator(10)))


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


def check(numberrr):
    str_nu = str(numberrr)
    len_nu = len(str_nu)
    a = str_nu[:(int(len_nu / 2))]
    b = ''.join(reversed(str_nu[int(-(len_nu / 2)):]))
    if len_nu % 2 == 0:
        if a == b:
            return True
    else:
        if str_nu[:(int((len_nu - 1) / 2))] == ''.join(reversed(str_nu[int(-(len_nu / 2)):])):
            return True
    return False


def prime_numbers_generator(n, func):
    prime_numbers = []
    for nu in range(2, n + 1):
        for prime in prime_numbers:
            if nu % prime == 0:
                break
        else:
            if func(nu):
                prime_numbers.append(nu)
                yield nu
    return


for number in prime_numbers_generator(n=2000, func=check):
    print(number)
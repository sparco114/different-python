# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers
#
#
# print(get_prime_numbers(100))


# -----------------------------------------------------------------------------


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


from random import randint

_num = None


def generate_num():
    global _num
    _num = str(randint(1000, 9999))
    # print(_num)


def check_num(asked_num):
    bulls = 0
    cows = 0
    for i in range(0, len(asked_num)):
        if asked_num[i] in _num:
            if asked_num[i] == _num[i]:
                bulls += 1
            else:
                cows += 1

    #     if str(_num)[i] == asked_num[i]:
    #         bulls += 1
    # for n in asked_num:
    #     if n in _num:
    #         if str(_num)[i] != asked_num[i]:
    #             cows += 1
    print("Количество быков - {}".format(bulls))
    print("Количество коров - {}".format(cows))
    return bulls == 4


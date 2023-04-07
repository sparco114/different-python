from random import randint

MAX_BUNCHES = 3
MAX_BUNCH_SIZE = 20

_holder = []


def put_stones():
    # global _holder = []
    for i in range(MAX_BUNCHES):
        _holder.append(randint(1, MAX_BUNCH_SIZE))


def take_from_bunch(pos, qty):
    if 1 <= pos < len(_holder) + 1:
        _holder[pos - 1] -= qty


def stones_position():
    return _holder


def gameover():
    return sum(_holder) == 0

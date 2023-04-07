from my_nim_engine import put_stones, take_from_bunch, stones_position, gameover
from termcolor import cprint, colored

put_stones()
user_num = 1
while True:
    col = 'blue' if user_num == 1 else 'yellow'
    print('Текущая позиция:')
    print(stones_position())
    cprint('Ход игрока {}'.format(user_num), color=col)
    pos = int(input(colored('Откуда берем?', col)))
    qty = int(input(colored('Сколько берем?', col)))
    take_from_bunch(pos=pos, qty=qty)
    if gameover():
        print('GAME OVER')
        break
    user_num = 2 if user_num == 1 else 1

cprint('Выиграл игрок {}'.format(user_num), color='red')
 
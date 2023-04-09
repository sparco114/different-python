# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from random import randint
from termcolor import cprint, colored


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return f"Я - {self.name}, сытость: {self.fullness}"

    def eat(self):
        if self.house.food >= 10:
            print(f'{self.name} поел')
            self.fullness += 30
            self.house.food -= 10
        else:
            self.fullness -= 10
            cprint(f'У {self.name} нет еды', 'yellow')

    def work(self):
        print(f'{self.name} cходил на работу')
        self.house.money += 150
        self.fullness -= 20

    def watching_tv(self):
        print(f'{self.name} смотрел МТВ')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print(f'{self.name} купил еды')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint(f'У {self.name} деньги кончились', 'yellow')

    def go_into_house(self, house):
        self.house = house
        self.fullness -= 10
        print(f'{self.name} заехал в дом')

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер от голода', 'red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food <= 20:
            self.shopping_cat_food()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watching_tv()

    def take_cat(self, cat):
        cat.house = self.house
        print(f'{self.name} взял кота в дом {self.house.house_name}')

    def shopping_cat_food(self):
        print(f'{self.name} купил коту еды')
        self.house.money -= 50
        self.house.cat_food += 50

    def cleaning(self):
        print(f'{self.name} прибрался в доме')
        self.fullness -= 20
        self.house.dirt += 100


class House:

    def __init__(self, house_name):
        self.food = 10
        self.money = 100
        self.house_name = house_name
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return f'В доме осталось еды: {self.food}, кошачьей еды: {self.cat_food}, денег: {self.money}'


class Cat:

    def __init__(self, cat_name):
        self.house = None
        self.cat_name = cat_name
        self.cat_fullness = 30

    def __str__(self):
        return f'Кот {self.cat_name}, в доме {self.house.house_name}. Сытость: {self.cat_fullness}'

    def sleep(self):
        print(f'Кот {self.cat_name} спит')
        self.cat_fullness -= 10

    def eat(self):
        if self.house.cat_food >= 10:
            print(f'Кот {self.cat_name} поел')
            self.cat_fullness += 20
            self.house.cat_food -= 10
        else:
            print('Нет кошачьей еды')
            self.cat_fullness -= 10

    def dirting(self):
        print(f'Кот {self.cat_name} дерет обои')
        self.cat_fullness -= 10
        self.house.dirt -= 5

    def act(self):
        if self.cat_fullness <= 0:
            cprint(f'Кот {self.cat_name} умер от голода', 'red')
            return
        dice = randint(1, 2)
        if self.cat_fullness <= 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        else:
            self.dirting()


beavis = Man('Бивис')
my_sweet_home = House('sweet_home')
beavis.go_into_house(my_sweet_home)
mark = Cat('Марк')
vaska = Cat('Васька')
murka = Cat('Мурка')

beavis.take_cat(mark)
beavis.take_cat(vaska)
beavis.take_cat(murka)

for day in range(1, 366):
    cprint(f'===================== DAY {day} =====================', 'blue')
    beavis.act()
    mark.act()
    vaska.act()
    murka.act()
    print('Итог дня:')
    print(beavis)
    print(mark)
    print(vaska)
    print(murka)
    print(my_sweet_home)


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

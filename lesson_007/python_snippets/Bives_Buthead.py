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
        self.house.money += 50
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
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watching_tv()


class House:

    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return f'В доме осталось еды: {self.food}, денег: {self.money}'


citizens = [
    Man('Бивис'),
    Man('Батхед'),
    # Man('Кенни'),
]

my_sweet_home = House()

for citisen in citizens:
    citisen.go_into_house(my_sweet_home)


for day in range(1, 365):
    cprint(f'===================== DAY {day} =====================', 'blue')
    for citisen in citizens:
        citisen.act()
    print('Итог дня:')
    for citisen in citizens:
        print(citisen)
    print(my_sweet_home)

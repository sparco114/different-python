from random import randint

from termcolor import cprint


class House:

    def __init__(self):
        self.money = 100
        self.food = 30
        self.dirt = 0

    def __str__(self):
        return f'В доме денег: {self.money}, еды: {self.food}, грязь: {self.dirt}'


class People:
    earn_money = 0
    ate_food = 0
    coats = 0

    def __init__(self, name, house):
        self.name = name
        self.fullness = 60
        self.happiness = 100
        self.house = house

    def __str__(self):
        return f'{self.name}, сытость: {self.fullness}, счастье:{self.happiness}'

    def eat(self):
        if self.house.food >= 30:
            print(f'{self.name} покушал')
            self.house.food -= 30
            self.fullness += 30
            People.ate_food += 30
        else:
            cprint(f'{self.name} нечего есть', color='yellow')
            self.fullness -= 10


class Husband(People):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness <= 0:
            cprint(f'{self.name} умер от голода', color='red')
            return
        if self.happiness <= 10:
            cprint(f'{self.name} умер от депрессии', color='red')
            return
        self.house.dirt += 2.5
        if self.fullness <= 30:
            self.eat()
        elif self.house.money <= 300:
            self.work()
        else:
            self.gaming()

    def work(self):
        print(f'{self.name} поработал')
        self.fullness -= 10
        self.house.money += 150
        People.earn_money += 150

    def gaming(self):
        print(f'{self.name} поиграл в WoT')
        self.fullness -= 10
        self.happiness += 20


class Wife(People):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness <= 0:
            cprint(f'{self.name} умер от голода', color='red')
            return
        if self.happiness <= 10:
            cprint(f'{self.name} умер от депрессии', color='red')
            return
        self.house.dirt += 2.5
        cube = randint(1, 3)
        if self.fullness <= 30:
            self.eat()
        elif self.house.food <= 60:
            self.shopping()
        elif self.happiness <= 30:
            self.buy_fur_coat()
        elif self.house.dirt >= 90:
            self.clean_house()
        elif cube == 1:
            self.buy_fur_coat()
        elif cube == 2:
            self.eat()
        elif cube == 3:
            self.shopping()

    def shopping(self):
        if self.house.money >= 70:
            print(f'{self.name} купила еды')
            self.house.food += 70
            self.house.money -= 70
            self.fullness -= 10
        else:
            print('Нет денег на еду')

    def buy_fur_coat(self):
        if self.house.money >= 350:
            print(f'{self.name} купила шубу')
            self.happiness += 60
            self.house.money -= 350
            self.fullness -= 10
            People.coats += 1
        else:
            print('Нет денег на шубу')

    def clean_house(self):
        print(f'{self.name} сделала уборку')
        self.house.dirt -= 100
        self.fullness -= 10
        self.happiness -= 10


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)

print(home)
print(serge)

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='cyan')
    serge.act()
    masha.act()
    cprint(serge, color='magenta')
    cprint(masha, color='magenta')
    cprint(home, color='magenta')

cprint(f'Заработано денег {People.earn_money}', color='black')
cprint(f'Съедено еды {People.ate_food}', color='black')
cprint(f'Куплено шуб {People.coats}', color='black')

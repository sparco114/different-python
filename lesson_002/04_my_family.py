#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.append('I')
my_family.extend(['fother', 'grandpa', 'jon'])
my_family.insert(0, 'mother')

print(my_family)

# список списков приблизителного роста членов вашей семьи
my_family_height = [['I', 172], ['fother', 178]]

my_family_height.append(['grandpa', 166])
my_family_height.insert(0, ['mother', 168])
my_family_height.extend([['jon', 179]])

# print(my_family_height)
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

print(f'Рост отца - {my_family_height[2][1]} см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print(f'Общий рост моей семьи - {(my_family_height[0][1]) + (my_family_height[1][1]) + (my_family_height)[2][1] + (my_family_height[3][1]) + (my_family_height[4][1])} см')

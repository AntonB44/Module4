'''Домашняя работа по уроку "Модули и пакеты"
Цель: закрепить навык создания и импортирования модулей,
а так же функций и переменных находящихся в них.'''

from fake_math import divide as fake_divide
from true_math import divide as true_divide
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
result5 = true_divide(0, 50)
print('Еще один пример:')
print(result5)

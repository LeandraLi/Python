# -------------------------------------------------------------------------------------------------
# Задача 30
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# ПРИМЕР:
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# a1 = int(input("Введите первый элемент прогресии: "))
# d = int(input("Введите разность: "))
# n = int(input("Введите кол-во эл-в: "))

# for i in range(a1, a1 + (n - 1)*d + 1, d):
#     print(i)


# -------------------------------------------------------------------------------------------------
# Задача 32
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# ПРИМЕР:
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

a = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = 7
max = 12

result = list(map(lambda x: x if min <= a[x] <= max else -1, range(len(a))))
result = list(filter(lambda x: x > -1, result))
print(result)

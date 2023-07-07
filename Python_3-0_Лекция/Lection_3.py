# Функция — это фрагмент программы, используемый многократно
# def function_name(x):
    # body line 1
    # ...
    # body line n
    # optional return

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ПРИМЕР
# Необходимо создать функцию sumNumbers(n), которая будет
# считать сумму всех элементов от 1 до n.

# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     # print(summa)
#     return summa

# # print(sumNumbers(5)) # 15

# # ИЛИ

# m = sumNumbers(5)
# print(m)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Модульность

# 1. function_file.py (Новый Python файл, в котором находятся функция f(x))
# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     return # выход из функции

# 2. working_file.py
# Чтобы начать взаимодействовать с функцией в файле function_file.py необходимо
# добавить эту возможность к себе в программный код. Сначала мы обращаемся к
# файлу(без расширения)
# С помощью import мы можем вызвать эту функцию в другом скрипте и дальше
# использовать её в новом файле. Можно сократить название функции в рабочем
# файле с помощью команды:
# Alias (псевдоним) — альтернативное имя, которое даётся функции при еt импорте из
# файла.
# import function_file
# print(function_file.f(1)) # Целое
# print(function_file.f(2.3)) # 23
# print(function_file.f(28)) # None

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# В Python можно перемножать строку на число.
# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Можно указать значение переменной count по умолчанию. Например, если
# значение явно не указано (нет второго аргумента), по умолчанию значение
# переменной count равно трем.
# def new_string(symbol, count=3):
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Возможность передачи неограниченного количества аргументов

# ● Можно указать любое количество значений аргумента функции.
# ● Перед аргументом надо поставить *.
# В примере ниже функция работает со строкой, поэтому при введении чисел
# программа выдаёт ошибку:

# def concatenatio(*params):
#     res = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1')) # a1
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Рекурсия — это функция, вызывающая сама себя.
# При описании рекурсии важно указать, когда функции надо остановиться и перестать вызывать саму себя. 
# По-другому говоря, необходимо указать базис рекурсии

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Быстрая сортировка
# def quicksort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quicksort(less) + [pivot] + quicksort(greater)

# print(quicksort([10, 5, 2, 3]))





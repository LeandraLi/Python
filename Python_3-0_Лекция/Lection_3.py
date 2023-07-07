# Функция — это фрагмент программы, используемый многократно
# def function_name(x):
    # body line 1
    # ...
    # body line n
    # optional return

# ПРИМЕР
# Необходимо создать функцию sumNumbers(n), которая будет
# считать сумму всех элементов от 1 до n.

def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)

n = int(input()) # 5
sumNumbers(n) # 15


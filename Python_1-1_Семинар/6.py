# Задача «Ход короля»
# Условие
# Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку. 
# Даны две различные клетки шахматной доски, определите, 
# может ли король попасть с первой клетки на вторую одним ходом. 
# Программа получает на вход четыре числа от 1 до 8 каждое, 
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
# Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую, 
# или NO в противном случае.
# Если хотя бы одно из введённых чисел не лежит в диапазоне от 1 до 8,
# то выведите строку "Ошибка ввода!"

ax = int(input("Введите 1-ое число от 1 до 8: "))
ay = int(input("Введите 2-ое число от 1 до 8: "))
bx = int(input("Введите 3-е число от 1 до 8: "))
by = int(input("Введите 4-ое число от 1 до 8: "))

if 1<=ax<=8 and 1<=ay<=8 and 1<=bx<=8 and 1<=by<=8:

    # if (ax == bx or bx == ax + 1 or bx == ax - 1) and (ay == by or ay == by - 1 or ay == by + 1):
    #     print('YES')
    # else:
    #     print('NO')

# Вариант 2:
    if abs(ax-bx)<=1 and abs(ay-by)<=1:
        print("YES")
    else:
        print("NO")
else:
 print("Ошибка ввода!")
# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

# Подсказка_Как бы из двух задач 2. Не меняем направление ломания. 
# #Надо просчитать кратность отломанных долек и посчитать площадь (3х2=6, то есть k не должно быть больше 6)

num = input('Введите шестизначный номер билета: ')
num1 = int(num[0]) + int(num[1]) + int(num[2])
num2 = int(num[3]) + int(num[4]) + int(num[5])
if num1 == num2:
    print('У вас счатливыйб билет!')
else:
    print('Вам не повезло, ваш билет не счастлив')

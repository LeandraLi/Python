from random import random


def write_info(info):
    with open("data.txt", "a", encoding = "utf-8") as file:
        file.write(info)

def find_info(char):
    with open("data.txt","r", encoding = "utf-8") as file:
        lst_sel = []
        lst = file.readlines() # по сути lst - это наши работники (элементы списка)
        count = 0
        for line in lst: # и запускаем цикл по этому списку
            if char in line: # если искомая характеристика есть в строке, то присваиваем ей номер по порядку
                count += 1
                print(f"{count}) {line.strip()}") # метод strip убирает лишнюю строку между строками при выводе данных
                lst_sel.append(line)
            return lst_sel

def view_all():
    with open("data.txt","r", encoding = "utf-8") as file:
        print(file.read())

def change_data(old_data, new_data): # перезапишем наш файлик с измененной строчкой
    with open("data.txt","r", encoding = "utf-8") as file:
        lst_old = file.readlines()
    with open("data.txt","w", encoding = "utf-8") as file:
        for line in lst_old:
            if old_data in line:
                file.write(new_data)
            else:
                file.write(line)

def delete_data(old_data): # только удаляем старую строчку, новой тут не будет
    with open("data.txt","r", encoding = "utf-8") as file:
        lst_old = file.readlines()
    with open("data.txt","w", encoding = "utf-8") as file:
        for line in lst_old:
            if old_data in line:
                continue
            else:
                file.write(line)

def sort_data(x):
    year = str(x.split(",")[1]).split(".")[2]
    month = str(x.split(",")[1]).split(".")[1]
    day = str(x.split(",")[1]).split(".")[0]
    return year, month, day

def sort(sort_num):
    with open("data.txt","r", encoding = "utf-8") as file:
        lst_old = file.readlines()
    if sort_num == 1:
        lst_old.sort(key = lambda x:x.split(",")[0])
    elif sort_num == 2:
        lst_old.sort(key = sort_data)
    elif sort_num == 3:
        lst_old.sort(key = lambda x:int(x.split(",")[2]))
    
    with open("data.txt","w", encoding = "utf-8") as file:
        file.writelines(lst_old)

import random

def randint(a, b):
    return random.randint(a, b)

def generate(num):
    names = ["Андрей","Дмитрий","Евгений","Иван","Константин","Максим","Никита","Олег","Павел","Роман",
            "Сергей","Тимофей","Ульяна","Кристина","Эдуард","Юлия","Яна","Виктория","Галина","Зинаида",]
    surnames = ["Иванов","Смирнов","Кузнецов","Попов","Васильев","Петров","Соколов","Михайлов","Новиков",
                "Федоров","Морозов","Волков","Алексеев","Лебедев","Семенов","Егоров","Павлов","Козлов",
                "Степанов","Николаев",]
    with open("data.txt","a", encoding = "utf-8") as file:
        for _ in range(num):
            fio = random.choice(names) + " " + random.choice(surnames)
            birth = f"{randint(1, 31)}.{randint(1, 12)}.{randint(1950, 2000)}"
            tele = random.randint(89000000000, 89990000000)
            line = f"{fio},{birth},{tele}\n"
            file.write(line)

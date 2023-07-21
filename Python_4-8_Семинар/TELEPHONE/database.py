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




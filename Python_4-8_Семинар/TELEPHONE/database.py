def write_info(info):
    with open("data.txt", "a", encoding = "utf-8") as file:
        file.write(info)

def find_info(char):
    with open("data.txt","r", encoding = "utf-8") as file:
        lst = file.readlines() # по сути lst - это наши работники (элементы списка)
        count = 0
        for line in lst: # и запускаем цикл по этому списку
            if char in line:
                count += 1
                print(f"{count}) {line.strip()}") # метод strip убирает лишнюю строку между строками при выводе данных



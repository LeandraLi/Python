from database import *
from view import *

def main():
    while True:
        num = input_number()
        if num == 1:
            info = input_info()
            write_info(info)
        elif num == 2:
            char = input_char()
            find_info(char)
        elif num == 3:
            char = input_char()
            lst_sel = find_info(char)
            sel_num = select_num()
            info = input_info()
            # теперь нужная строка для изменения хранится в следующем списке: lst_sel[sel_num-1]
        elif num == 4:
            char = input_char()
            find_info(char)
            sel_num = select_num()
        elif num == 5:
            char = input_char()
            find_info(char)
        elif num == 6:
            view_all()
        elif num == 7:
            print("Выход из программы") # сразу пишем сообщение, т.к. знаем сразу, что 5 - это выход
            pass
            break

main()


from database import *
from view import *

def main():
    while True:
        num = input_number()
        if num == 1:
            info = input_info()
            write_info(info)
            print("Успешно добавлено")
        elif num == 2:
            char = input_char()
            find_info(char)
            print("Успешно найдено")
        elif num == 3:
            char = input_char()
            lst_sel = find_info(char)
            sel_num = select_num()
            info = input_info()
            # теперь нужная строка для изменения хранится в следующем списке: lst_sel[sel_num-1]
            change_data(lst_sel[sel_num-1], info)
            print("Успешно изменено")
        elif num == 4:
            char = input_char()
            lst_sel = find_info(char)
            sel_num = select_num()
            delete_data(lst_sel[sel_num-1])
            print("Успешно удалено")
        elif num == 5:
            sort_num = select_sort()
            sort(sort_num)
            print("Успешно отсортировано")
        elif num == 6:
            view_all()
        elif num == 7:
            count = input_count()
            generate(count)
            print("Успешно сгенерировано")
        elif num == 8:
            print("Выход из программы") # сразу пишем сообщение, т.к. знаем сразу, что 5 - это выход
            pass
            break
main()


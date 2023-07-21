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
        elif num == 5:
            print("Выход из программы") # сразу пишем сообщение, т.к. знаем сразу, что 5 - это выход
            pass
            break

main()


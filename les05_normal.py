__author__ = 'Nina Vinokurova'

task='''\n# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py'''

#print(task)

import os
import sys
import les05_easy_def as easy

print('sys.argv = ', sys.argv)

if __name__ == '__main__':
    do = {
        "help": easy.print_help,
        "chdir": easy.change_dir,
        "dir_contents": easy.dir_contents,
        "rmdir": easy.del_dir,
        "mkdir": easy.make_dir,
        "ping": easy.ping
    }

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

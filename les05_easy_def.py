__author__ = 'Nina Vinokurova'

#функции для задания normal
import os
import shutil
import sys

# 1. Перейти в папку
def change_dir():
    if not dir_path:
        print("Необходимо указать имя директории вторым параметром")
    try:
        os.chdir(dir_path)
        print('Вы успешно перешли в директорию {}'.format(dir_path))
        print('Текущая директория:',os.getcwd())
    except FileExistsError:
        print('Что-то пошло не так... Попробуйте еще раз перейти в директорию {}'.format(dir_name))

# 2. Просмотреть содержимое текущей папки
def dir_contents():
    names = os.listdir(os.getcwd())
    for name in names:
        fullname = os.path.join(os.getcwd(), name) #полное имя
        if os.path.isdir(fullname): #путь с доступом ко всем папкам текущей директории
            print('папки директории:',fullname)
        if os.path.isfile(fullname): #путь с доступом ко всем файлам текущей директории
            print('файлы директории:',fullname)

# 3. Удалить папку
def del_dir():
    if not dirname:
        print("Необходимо указать имя директории вторым параметром")
    dir_path = os.path.join(os.getcwd(), dirname)
    try:
        os.rmdir(dir_path)
        print('Директория с наименованием ',dirname,' удалена')
    except FileExistsError:
        print('Что-то пошло не так... Директория с наименованием ',dirname,' не удалилась')

# 4. Создать папку
def make_dir():
    if not dirname:
        print("Необходимо указать имя директории вторым параметром")
    dir_path = os.path.join(os.getcwd(), dirname)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dirname))
    except FileExistsError:
        print('директория {} уже существует'.format(dirname))




#   cp <file_name> - создает копию указанного файла
def file_copy():
    filename=sys.argv
    str_filename=''.join(filename)
    print('Файл, из кот. запущен данный скрипт: ',str_filename)

    try:
        new_user_file=str_filename+'.copy'
        shutil.copy(str_filename,new_user_file,follow_symlinks=True)
        print('\nФайл {} был успешно создан'.format(new_user_file))
    except FileExistsError:
        print('Что-то пошло не так... Ошибки копирования')

        
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
def del_file():
    if not filename:
        print("Необходимо указать имя файла вторым параметром")
    file_path = os.path.join(os.getcwd(), filename)
    try:
        os.remove(file_path)
        print('Файл с наименованием ',filename,' удален')
    except FileExistsError:
        print('Что-то пошло не так... Файл с наименованием ',filename,' не удалился')

    

#   ls - отображение полного пути текущей директории
def show_path():
    print('Текущая директория:',os.getcwd())


def print_help():
    print("help - получение справки")
    print("chdir <dirname> - переход в папку с соотв. наименованием")
    print("dir_contents - просмотр содержимого текущей папки")
    print("rmdir <dirname> - удаление директории")
    print("mkdir <dirname> - создание директории")
    print("ping - тестовый ключ")
    
def ping():
    print("pong")


if __name__=='__main__':
    main()

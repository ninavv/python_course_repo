__author__ = 'Nina Vinokurova'

#функции для задания normal
import os

# 1. Перейти в папку
def change_dir():
    if not dir_path:
        print("Необходимо указать имя директории вторым параметром")
    try:
        os.chdir(dir_path)
        print('Вы успешно перешли в директорию {}'.format(dir_path))
        print(os.getcwd())
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


def print_help():
    print("help - получение справки")
    print("chdir <dirname> - переход в папку с соотв. наименованием")
    print("dir_contents - просмотр содержимого текущей папки")
    print("rmdir <dirname> - удаление директории")
    print("mkdir <dirname> - создание директории")
    print("ping - тестовый ключ")
    
def ping():
    print("pong")

  

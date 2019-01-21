__author__ = 'Nina Vinokurova'

task='''\n# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.\n'''
print(task)

import os
#import shutil

print(os.getcwd())

for i in range(1,10):
    dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
    try:
        os.mkdir(dir_path)
        print('Директория с наименованием dir_{} создана'.format(i))
    except FileExistsError:
        print('Директория с наименованием dir_{} уже существует'.format(i))


for i in range(1,10):
    dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
    try:
        os.rmdir(dir_path)
        #shutil.rmtree(os.getcwd(), 'dir{}'.format(i)) #shutil.rmtree() deletes a directory and all its contents(включая файл с ДЗ :) ).
        print('Директория с наименованием dir_{} удалена'.format(i))
    except FileRemoveError:
        print('Что-то пошло не так... Директория  с наименованием dir_{} не удалилась'.format(i))



task='''\n# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.\n'''
print(task)

import os
print('Текущая директория: ',os.getcwd())
print('\nПапки текущей директории: \n')
names = os.listdir(os.getcwd())
for name in names:
    fullname = os.path.join(os.getcwd(), name) #полное имя
    if os.path.isdir(fullname): #путь с доступом ко всем папкам текущей директории
        print(fullname)
    #if os.path.isfile(fullname): #путь с доступом ко всем файлам текущей директории
        #print(fullname)


task='''\n# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.\n'''
print(task)

import os
import shutil
import sys

#file_name=os.listdir(path=os.getcwd())
#str_file_name=''.join(file_name)
#print(str_file_name)

filename=sys.argv
str_filename=''.join(filename)
print('Файл, из кот. запущен данный скрипт: ',str_filename)

try:
    new_user_file=str_filename+'.copy'
    shutil.copy(str_filename,new_user_file,follow_symlinks=True)
    print('\nФайл {} был успешно создан'.format(new_user_file))
except FileExistsError:
    print('Что-то пошло не так... Ошибки копирования')

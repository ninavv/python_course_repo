__author__ = 'Nina Vinokurova'

task='''Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3'''

print(task)

def add_subtract(operation):
    pos_plus=operation.find('+')
    pos_minus=operation.find('-',1)

    if operation[pos_plus]=='+':
        #first_num=operation[:pos_plus]
        #second_num=operation[pos_plus+1:]
        #print(first_num,second_num)
        
        pos_del_first_num=operation.find('/')
        pos_del_second_num=operation.find('/',pos_plus)
        #print(pos_del_first_num,pos_del_second_num)
        
        first_top_digit=operation[:pos_del_first_num]
        first_bottom_digit=operation[pos_del_first_num+1:pos_plus]
        second_top_digit=operation[pos_plus+1:pos_del_second_num]
        second_bottom_digit=operation[pos_del_second_num+1:]
        #print(first_top_digit,first_bottom_digit,second_top_digit,second_bottom_digit)

        top=int(first_top_digit)*int(second_bottom_digit)+int(second_top_digit)*int(first_bottom_digit)
        bottom=int(first_bottom_digit)*int(second_bottom_digit)
        #print(top)
        #print(bottom)

        n=top//bottom #целая часть
        top_drob=top-n*bottom
        bottom_drob=bottom
        print(n, top_drob,'/',bottom_drob)

    
    elif operation[pos_minus]=='-':
        pos_del_first_num=operation.find('/')
        pos_del_second_num=operation.find('/',pos_minus)
        
        first_top_digit=operation[:pos_del_first_num]
        first_bottom_digit=operation[pos_del_first_num+1:pos_minus]
        second_top_digit=operation[pos_minus+1:pos_del_second_num]
        second_bottom_digit=operation[pos_del_second_num+1:]

        top=float(first_top_digit)*float(second_bottom_digit)-float(second_top_digit)*float(first_bottom_digit)
        bottom=float(first_bottom_digit)*float(second_bottom_digit)

        n=int(top//bottom) #целая часть
        top_drob=int(top-n*bottom)
        bottom_drob=int(bottom)
        print(n, top_drob,'/',bottom_drob)

    
add_subtract('5/6 + 4/7')
add_subtract('-2/3 - -2/1')


task='''Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"'''

print(task)
import os
path_workers=os.path.join('data','workers.py')
path_hours=os.path.join('data','hours_of.py')
w=open(path_workers,'r',encoding='UTF-8')
#print(w.readlines())
h=open(path_hours,'r',encoding='UTF-8')
#print(h.readlines())
for line in w:
    print(line.split())
    #print(line.split()[1],line.split()[2],line.split()[4])

for line in h:
    print(line.split())
    #print(line.split()[1],line.split()[2])


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


__author__ = 'Nina Vinokurova'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

print("ЗАДАЧА: введите произвольное целое число и я выведу самую большую цифру этого числа")
number=input("введите число: ")
max=0
i=0
while i in range(0,len(number)): #для решения с for: вместо while в этой строке можно указать for
    if int(number[i])>=max:
        max=int(number[i])
    i+=1
print("самая большая цифра вашего числа: ", max)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print("ЗАДАЧА: введите значения 2-ух переменных и я: поменяю эти переменные местами и выведу их на экран")
a=input("введите значение 1-ой переменной: ")
b=input("введите значение 2-ой переменной: ")
print("вы ввели: ", a+b)
c=b+a
print("я, как и обещал, выведу: ", c)


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
print("ЗАДАЧА: вычисляем корни квадратного уравнения вида ax^2+bx+c=0; коэффициенты уравнения вводятся пользователем")
a=float(input("введите коэффициент a: "))
b=float(input("введите коэффициент b: "))
c=float(input("введите коэффициент c: "))
print("ищу корни квадратного уравнения вида: ", a,"x^2 +",b,"x +",c,"=0")
D=b**2-4*a*c
if D>=0:
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    print("первый корень: ", x1)
    print("второй корень: ", x2)
else:
    print("уравнение не имеет корней")

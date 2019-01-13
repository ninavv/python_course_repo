__author__ = 'Nina Vinokurova'

task='''Задание-1:
Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
Первыми элементами ряда считать цифры 1 1'''

print(task)

def fibonacci(n,m):
    list_1=[1,1]
    list_2=[]
    sum=0
    for i in range(m):
        sum=list_1[i]+list_1[i+1]
        list_1.append(sum)
    #print(list_1)
    for z in range(n,m+1):
        list_2.append(list_1[z])
    print(list_2)
    
fibonacci(2,6)
fibonacci(4,10)



task='''Задача-2:
Напишите функцию, сортирующую принимаемый список по возрастанию.
Для сортировки используйте любой алгоритм (например пузырьковый).
Для решения данной задачи нельзя использовать встроенную функцию и метод sort()'''

print(task)

def sort_to_max(origin_list):
    
    new_list=[]
    while(len(origin_list))>0:
        min=origin_list[0]
        
        for i in range(len(origin_list)):
            if origin_list[i]<min:
                min=origin_list[i]
        #print(min)        
        origin_list.remove(min)
        new_list.append(min)
    print(new_list)

list_1=[2,10,-12,2.5,20,-11,4,4,0]
sort_to_max(list_1)



task='''Задача-3:
Напишите собственную реализацию стандартной функции filter.
Разумеется, внутри нельзя использовать саму функцию filter.'''

print(task)

def sort_to_min(origin_list):
    
    new_list=[]
    while(len(origin_list))>0:
        max=origin_list[0]
        
        for i in range(len(origin_list)):
            if origin_list[i]>=max:
                max=origin_list[i]
        #print(max)        
        origin_list.remove(max)
        new_list.append(max)
    print(new_list)

num_list = [2,10,-12,2.5,20,-11,4,4,0]
list(map(sort_to_min(num_list),num_list))

task='''Задача-4:
Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
Определить, будут ли они вершинами параллелограмма.'''

print(task)

import math
def parallelogram(x1,y1,x2,y2,x3,y3,x4,y4):
    a1=math.sqrt((x2-x1)**2+(y2-y1)**2)
    a2=math.sqrt((x3-x4)**2+(y3-y4)**2)
    a3=math.sqrt((x4-x1)**2+(y4-y1)**2)
    a4=math.sqrt((x3-x2)**2+(y3-y2)**2)
    if a1==a2 and a3==a4:
        return True
    else:
        return False
          
print(parallelogram(1,3,4,7,2,8,-1,4))
print(parallelogram(-2,1,1,-4,6,-3,3,2))
print(parallelogram(-2,-5,1,-4,9,-3,3,0))

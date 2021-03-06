__author__ = 'Nina Vinokurova'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print("ЗАДАЧА: дан список фруктов; нужно вывести фрукты в виде нумерованного списка, выровненного по правой стороне")
print("<<< ... форматирование с помощью .format")
fruits=['apple','banana','mango','orange','peach','pineapple']
i=1
for fruit in fruits:
    print("{}. {:>9}" .format(i,fruit))
    i+=1

#or using %
print("<<< ... или форматирование с помощью %")
fruits=['apple','banana','mango','orange','peach','pineapple']
i=1
for fruit in fruits:
    print("%d. %9s" %(i,fruit))
    i+=1

#or using string.rjust
print("<<< ... или форматирование с помощью string.rjust")
fruits=['apple','banana','mango','orange','peach','pineapple']
i=1
for fruit in fruits:
    print(str(i)+".", fruit.rjust(9))
    i+=1


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print("<<<")
print("ЗАДАЧА: даны 2 произвольных списка; удалите из первого списка элементы, присутствующие во втором списке")
list_1=["peach",1,2,3,0.5,"apple","mango",55,56,[22,23]]
list_2=[3,2,"peach",0.9,"apple","orange",55,57,[22,23]]
i=0
for list_1[i] in list_1:
    if list_1[i] in list_2:
        list_1.pop(i)
        i+=1
print(list_1)

#or using list.remove
'''print("ЗАДАЧА: даны 2 произвольных списка; удалите из первого списка элементы, присутствующие во втором списке")
list_1=["peach",1,2,3,0.5,"apple","mango",55,56,[22,23]]
list_2=[3,2,"peach",0.9,"apple","orange",55,57,[22,23]]
for el in list_1:
    if el in list_2:
        list_1.remove(el)
print(list_1)'''

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print("<<<")
print("ЗАДАЧА: дан список из целых чисел; следует получить новый список, в кот. выполнено условие: если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два")
list_1=[1,2,3,5,7,10,-10,-8,-3]
print("list_1 =", list_1)
list_2=[]
for el in list_1:
    if el % 2 == 0:
        el=el/4
    else:
        el=el*2
    list_2.append(el)
print("list_2 =", list_2)

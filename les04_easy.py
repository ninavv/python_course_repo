__author__ = 'Nina Vinokurova'

# Все задачи текущего блока решите с помощью генераторов списков!

task='''\nЗадание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]\n'''

print(task)
list_1=[1,2,4,0]
list_2=[i**2 for i in list_1]
print(list_2)

task='''\nЗадание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.\n'''

print(task)
list_1=["apple","peach","mango","grapevine"]
list_2=["banana","watermelon","apple","kiwi","mango"]
list_3=[el for el in list_1 if el in list_2]
print(list_3)

task='''\n Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4\n'''

print(task)
list_1=[1,2,3,5,7,10,0,-5,4]
list_2=[i for i in list_1 if i%3==0]
print(list_2)
list_3=[i for i in list_1 if i>0]
print(list_3)
list_4=[i for i in list_1 if i%4!=0]
print(list_4)

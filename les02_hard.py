ArithmeticError__author__ = 'Nina Vinokurova'

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
print("ЗАДАЧА: уравнение прямой вида y = kx + b задано в виде строки; определить координату y точки с заданной координатой x ")
equation = 'y = -12x + 11111140.2121'
x = 2.5
print("уравнение:", equation)

pos_x=equation.find("x")
pos_equal=equation.find("=")
k=equation[pos_equal+2:pos_x]
b=equation[pos_x+4:]
k=float(k)
b=float(b)
y=k*x+b
print(f"результат вычисления при х={x}:", y)


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

print("<<<")
print("ЗАДАЧА: Дата задана в виде строки формата 'dd.mm.yyyy'; проверить, корректно ли введена дата")

date_in=input("введите дату в формате dd.mm.yyyy: ")

'''from datetime import datetime as dt
try:
    dt.strptime(date_in, '%d.%m.%Y')
except ValueError:
    raise ValueError("дата введена в неправильном формате")'''

day_=int(date_in[0:2])
month_=int(date_in[3:5])
year_=int(date_in[6:])

while not (date_in.find(".")==2 and date_in.find(".",date_in.find(".")+1)==5 and len(date_in[6:])>=1 and len(date_in[6:])<=4):
    print("вы ввели дату в НЕВЕРНОМ формате")
    #break
    date_in=input("введите дату в формате dd.mm.yyyy: ")
else:
    print("формат ввода даты верный")


#проверка на корректность:

if month_ in range(1,13):
    print("месяц введен корректно")
else:
    print("месяц введен НЕКОРРЕКТНО")

if ((month_%2==0 and day_ in range(1,31)) or (month_%2!=0 and day_ in range(1,32))):
    print("день введен корректно")
else:
    print("день введен НЕКОРРЕКТНО")

if year_ in range(1,10000):
    print("год введен корректно")
else:
    print("год введен НЕКОРРЕКТНО")


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

#n-уровень
#m-этаж
#k-кол-во кв на уровне
#l-кол-во кв на этаже

print("<<<")
print("ЗАДАЧА: по номеру комнаты определить, на каком этаже она находится и какая она по счету слева на этом этаже")
room_num=int(input("введите номер комнаты: "))
level=0
floor_sum=0
room_sum=0
while room_num>room_sum:
    level+=1
    floor=level
    room=level*level
    print("на уровне номер ",level,"-",floor,"этажей и",room,"комнат")
    floor_sum+=floor
    room_sum+=room
    print("ИТОГО: ",floor_sum,"ЭТАЖЕЙ и",room_sum,"КОМНАТ")

first_floor_on_level=floor_sum-floor+1
first_room_on_level=room_sum-floor*floor+1
room_pos_on_level=room_num-first_room_on_level+1

if room_pos_on_level%level!=0:
    floor_num=first_floor_on_level+room_pos_on_level//level
    room_pos_from_left=room_pos_on_level%level
else:
    floor_num=(first_floor_on_level+room_pos_on_level//level)-1
    room_pos_from_left=level
print(f"эта комната находится на этаже №{floor_num}, она {room_pos_from_left}-я по счету слева")





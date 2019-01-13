__author__ = 'Nina Vinokurova'

task='''Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.'''

print(task)

def my_round(number, ndigits):
    
    pos_float=str(number).find(".") #1 int
    int_part=str(number)[:pos_float]  #2 str
    float_part=str(number)[pos_float+1:pos_float+ndigits+2]
    
    if ndigits==0:
        if int(str(number)[pos_float+1:pos_float+2])>=5:
            return(int(int_part)+1)
        else:
            return(int(int_part))  
    else:
        if int(float_part)%10>=5:
            float_part_1=int(str(number)[pos_float+1:pos_float+ndigits+1])+1
        else:
            float_part_1=int(str(number)[pos_float+1:pos_float+ndigits+1])
        return(int_part+"."+str(float_part_1))

print(my_round(10.42645,4))
print(my_round(10.67595,0))
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

task='''Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить'''

print(task)

def lucky_ticket(ticket_number):

    sum_1_3=0 #сумма цифр от 1 до 3
    sum_4_6=0 #сумма цифр от 4 до 6
    n=6 #шестизначный номер билета

    ticket_no_1_part=str(ticket_number)[:int(n/2)]
    ticket_no_2_part=str(ticket_number)[int(n/2):]
    
    for i in range(0,int(n/2)):
        sum_1_3+=int(ticket_no_1_part[i])
        sum_4_6+=int(ticket_no_2_part[i])
    #print(sum_1_3)
    #print(sum_4_6)
    
    if sum_1_3==sum_4_6:
        return True
    else:
        return False

print("билет 123006 счастливый? -")
print(lucky_ticket(123006))
print("билет 123210 счастливый? -")
print(lucky_ticket(123210))
print("билет 436751 счастливый? -")
print(lucky_ticket(436751))



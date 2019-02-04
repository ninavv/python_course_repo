import random
 
class Player:
    def __init__(self,name):
                    self.name=name
 
                    
class Card:
    def __init__(self,rows_num=3,cols_num=9,nums_in_row=5):
        self.rows_num=rows_num
        self.cols_num=cols_num
        self.nums_in_row=nums_in_row
    def fill_row(self):
        #choose_unique_row_values:   
        for i in range(1,self.cols_num+1):
            choose_num=set()
            j=0
            while len(choose_num)<self.nums_in_row:
                if j not in choose_num:
                    j=choose_num.add(random.randrange(1,self.cols_num+1))
        self.choose_num_list=list(choose_num)
        #print(choose_num_list)
 
        #print_row
        row1=[]
        for i in range(1,self.cols_num+1):
            if i in self.choose_num_list:
                row1.append(random.randrange(1,90+1))
            else:
                row1.append(" ")
        return row1
    def fill_card(self):
        self.card1=[]
        while len(set(self.card1))!=16:
            self.card1=self.fill_row()+self.fill_row()+self.fill_row()
        return self.card1
    def __iter__(self):
        return (el for el in self.card1)

class Barrel:
    def __init__(self,num=random.randint(1,90+1)):
        self.num=num


#rand_barrel=Barrel()
#print('выпал бочонок №:',rand_barrel.num)

              

player_1=Player("Computer")
print(player_1.name)
 
card_1=Card()
#print(card_1.fill_card())
random_card_1=card_1.fill_card()
#print(random_card)
'''print(random_card_1[:9])
print(random_card_1[9:18])
print(random_card_1[18:])'''
 
player_2=Player("User")
print(player_2.name)

card_2=Card()
random_card_2=card_2.fill_card()
#print(random_card)
'''print(random_card_2[:9])
print(random_card_2[9:18])
print(random_card_2[18:])'''
 
'''pip install pandas
import pandas as pd
df=pd.DataFrame(card_1)
print(df.head())'''
'''from tabulate import tabulate
table=[]
table.append_row([1,2])
table.append_row([3,4])
table.append_row([5,6])
print(tabulate(table))'''
 
#print(type(list(card_1)))

#answer=input("Зачеркнуть цифру? <Y/N>",)

'''if answer.upper()=="Y":
    if answer in list(card_2):
        ind=list(card_2).index(answer)
        list(card_2)[ind]="X"
        pass
    else:
        print("you loose")
        break
        
if answer.upper()=="N":
    if answer in list(card_2):
        print("you loose")
        break
    else:
        pass'''
compCard_list=list(random_card_1)
userCard_list=list(random_card_2)

while True:
    barrel=random.randrange(1,91)
    print()
    print("выпал бочонок №",barrel)

    print("---------------",player_1.name,"---------------")
    print(compCard_list[:9])
    print(compCard_list[9:18])
    print(compCard_list[18:])
    print("----------------------------------------")

    print("-----------------",player_2.name,"-----------------")
    print(userCard_list[:9])
    print(userCard_list[9:18])
    print(userCard_list[18:])
    print("----------------------------------------")

    if barrel in compCard_list:
        ind=compCard_list.index(barrel)
        compCard_list[ind]="-"
        
    answer=input("Зачеркнуть цифру? <Y/N>",)       
    if answer.upper()=="Y":
        if barrel in userCard_list:
            ind=userCard_list.index(barrel)
            print("Такая цифра содержится в карточке, зачеркнули")
            userCard_list[ind]="-"
        else:
            print("Такой цифры в карточке нет, Вы проиграли")
            break

    if answer.upper()=="N":
        if barrel in userCard_list:
            print("Такая цифра на карточке все же была, Вы проиграли")
            break

    end_list=[" "*27]
    if compCard_list==end_list:
        print("Победил игрок",player_1.name)
    if userCard_list==end_list:
        print("Победил игрок",player_2.name)


            
        


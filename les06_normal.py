__author__ = 'Nina Vinokurova'

task='''# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе\n'''
print(task)

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def get_name(self):
        return self.name + ' ' + self.surname
    def short_name(self):
        return self.surname+' '+self.name[0]+' '+self.father[0]
    def full_name(self):
        return self.name + ' ' + self.surname + ' ' + self.fathers_name
    
class Mother(Person):
    def __init__(self, name, surname, fathers_name):
        Person.__init__(self, name, surname)
        self.fathers_name=fathers_name
        
class Father(Person):
    def __init__(self, name, surname, fathers_name):
        Person.__init__(self, name, surname)
        self.fathers_name=fathers_name
        
class Student(Mother,Father):
    def __init__(self, name, surname, fathers_name, class_room, subject, mother, father):
        Person.__init__(self, name, surname)
        Mother.__init__(self, name, surname, fathers_name)
        Father.__init__(self, name, surname, fathers_name)
        self.fathers_name=fathers_name
        self.class_room=class_room
        self.subject=subject
        self.mother=mother
        self.father=father
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'],self._class_room['class_char'])
    def parents(self):
        return self.mother+', '+self.father

class Teacher(Person):
    def __init__(self, name, surname, subject):
        Person.__init__(self, name, surname)
        self.subject=subject

    
mother1=Mother('Анна','Иванова','Ильинична')
mother2=Mother('Елена','Петрова','Васильевна')
       
father1=Father('Александр','Иванов','Электронович')
father2=Father('Роман','Петров','Кузьмич')

student1=Student("Александр","Иванов","Александрович","5А","математика","Анна Иванова","Александр Иванов")
student2=Student("Александра","Иванова","Александровна","2А","русский","Анна Иванова","Александр Иванов")
student3=Student("Валентин","Петров","Романович","5А","математика","Елена Петрова","Роман Петров")
student4=Student("Валентина","Петрова","Романовна","1Б","русский","Елена Петрова","Роман Петров")
student5=Student("Евгений","Петров","Романовна","2В","английский","Елена Петрова","Роман Петров")
student6=Student("Евгения","Иванова","Александровна","5В","английский","Анна Иванова","Александр Иванов")
students=[student1,student2,student3,student4,student5,student6]

teacher1=Teacher("Алексей","Сидоров","математика")
teacher2=Teacher("Василиса","Сорокина","русский")
teacher3=Teacher("Джон","Смит","английский")
teachers=[teacher1,teacher2,teacher3]

# 1. Получить полный список всех классов школы
all_class_rooms=[]
for student in students:
    all_class_rooms.append(student.class_room)
print('перечень всех классов:',set(all_class_rooms))
print()

# 2. Получить список всех учеников в указанном классе (каждый ученик отображается в формате "Фамилия И.О.")
find_class_room="5А" #например, в классе 5А
print('перечень учеников в классе {}:'.format(find_class_room))
all_students=[]
for student in students:
    if student.class_room==find_class_room:
        all_students.append(student.short_name())
print('ученики:',all_students)
print()

# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
find_name="Александр"
find_surname="Иванов"
print('перечень предметов конкретного ученика {} {}:'.format(find_name,find_surname))
certain_subjects=[]
for student in students:
    if student.name==find_name and student.surname==find_surname:
        certain_subjects.append(student.class_room)
        certain_subjects.append(student.subject)
        for teacher in teachers:
            if student.subject==teacher.subject:
                certain_subjects.append(teacher.get_name())
print('класс, предмет, учитель:',certain_subjects)
print()

# 4. Узнать ФИО родителей указанного ученика
find_name="Александр"
find_surname="Иванов"
print('ФИ родителей конкретного ученика {} {}:'.format(find_name,find_surname))
certain_parents=[]
for student in students:
    if student.name==find_name and student.surname==find_surname:
        certain_parents.append(student.parents())
print('мать, отец:',certain_parents)
print()
# 5. Получить список всех Учителей, преподающих в указанном классе
find_class="5А"
print('список учителей, преподающих в классе {}:'.format(find_class))
certain_teachers=[]
for student in students:
    if student.class_room==find_class:
        for teacher in teachers:
            if student.subject==teacher.subject:
                certain_teachers.append(teacher.get_name())
print('учителя:',set(certain_teachers))


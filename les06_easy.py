__author__ = 'Nina Vinokurova'

task='''# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.\n'''
print(task)
import math
class Triangle:
    def __init__(self, side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def square(self):
        p=(self.side1+self.side2+self.side3)/2
        return math.sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))
    def height(self):
        p=(self.side1+self.side2+self.side3)/2
        return 2*math.sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))/self.side1
    def perimeter(self):
        return self.side1+self.side2+self.side3
        
class Triangle_Top:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def side(X,Y):
        return math.sqrt((X.x-Y.x)**2+(X.y-Y.y)**2)

A=Triangle_Top(-5,2)
B=Triangle_Top(7,-7)
C=Triangle_Top(5,7)
print('координаты первой вершины:({},{})'.format(A.x,A.y))
print('координаты второй вершины:({},{})'.format(B.x,B.y))
print('координаты третьей вершины:({},{})'.format(C.x,C.y))
sideAB=Triangle_Top.side(A,B)
sideBC=Triangle_Top.side(B,C)
sideAC=Triangle_Top.side(A,C)
print('длины сторон треугольника:{},{},{}\n'.format(sideAB,sideBC,sideAC))
Triangle1=Triangle(sideAB,sideBC,sideAC)
#print(Triangle1.side1,Triangle1.side2,Triangle1.side3)
print('площадь треугольника:',Triangle1.square())
print('одна из высот треугольника:',Triangle1.height())
print('периметр треугольника:',Triangle1.perimeter())



task='''# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.\n'''
print(task)
class Trapezium:
    def __init__(self, x1,y1,x2,y2,x3,y3,x4,y4):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.x3=x3
        self.y3=y3
        self.x4=x4
        self.y4=y4
        
    def side1(self):
        return math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        
    def side2(self):   
        return math.sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)
        
    def side3(self):     
        return math.sqrt((self.x4-self.x3)**2+(self.y4-self.y3)**2)
     
    def side4(self):    
        return math.sqrt((self.x1-self.x4)**2+(self.y1-self.y4)**2)
    
    def perimeter(self):
        return self.side1()+self.side2()+self.side3()+self.side4()
        
    def square(self):
        h=math.sqrt(self.side1()**2-(((self.side4()-self.side2())**2+self.side1()**2-self.side3()**2)/(2*(self.side4()-self.side2())))**2)
        return 1/2*(self.side2()+self.side4())*h
        
    def check(self):
        if (self.side1()==self.side3() and ((self.x4-self.x1)/self.side4()==(self.x3-self.x2)/self.side2())) or (self.side2()==self.side4() and ((self.x3-self.x4)/self.side3()==(self.x2-self.x1)/self.side1())) or((self.side1()==self.side3())and(self.side2()==self.side4()))or((self.side2()==self.side4())and(self.side1()==self.side3())):
            print('Точки обрауют равнобедренную трапецию')
        else:
            print('Точки не образуют равнобедренную трапецию')
        
        
trapezium1=Trapezium(0,0,2,8,9,8,11,0)
print('длины сторон:{},{},{},{}'.format(trapezium1.side1(), trapezium1.side2(), trapezium1.side3(), trapezium1.side4()))
print('периметр трапеции:',trapezium1.perimeter())
print('площадь трапеции',trapezium1.square())
trapezium1.check()

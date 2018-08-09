#
# class Person:
#     role = 'chinese'
#     def walk(self):
#         print('i am walking ...')
#
# print(Person.role)
# print(Person.walk)
#####################################################################
#
# class Person:
#     role = 'chinese'
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#     def walk(self):
#         print('walking ......')
#
#
# print(Person.__name__,type(Person.__name__))
# han = Person('hanlei','boy')
# print(han.role)
# print(han.name)
# print(han.sex)
# print(han)
# han.walk()
##########################################################################
#
#
# class Person:
#     def __init__(self,name,aggr,lv):
#         self.name = name
#         self.aggr = aggr
#         self.lv = lv
#     def attack(self,dog):
#         dog.lv = dog.lv - self.lv
#
# class Dog:
#     def __init__(self,name,aggr,lv):
#         self.name = name
#         self.aggr = aggr
#         self.lv = lv
#     def attack(self,egg):
#         egg.lv = egg.lv - self.aggr
#
# egg = Person('egon',100,100)
# dog = Dog('ll',90,90)
#
# print('dog.lv  ',dog.lv)
# egg.attack(dog)
# print('dog.lv  ',dog.lv)
#
#
# print('egg.lv',egg.lv)
# dog.attack(egg)
# print('egg.lv',egg.lv)
#
#####################################################################################

#圆和环
# from math import pi
#
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def perimater(self):
#         return 2*pi*self.r
#     def area(self):
#         return pi*self.r*self.r
#
# class Circle_ring:
#     def __init__(self,r1,r2):
#         outr = max(r1,r2)
#         inr = min(r1,r2)
#         self.outc = Circle(outr)
#         self.inc = Circle(inr)
#     def area(self):
#         return self.outc.area() - self.inc.area()
#     def perimater(self):
#         return self.outc.perimater() + self.inc.perimater()
#
#
# cr = Circle_ring(1,10)
# print(cr.area())
# print(cr.perimater())
#
# c1 = Circle(1)
# c2 = Circle(10)
# print(c1.area())
# print(c2.area())
# print(c1.perimater())
# print(c2.perimater())
# ###################################################################################
#
# class Birthday:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#
# class Course :
#     def __init__(self,name,price,period):
#         self.name = name
#         self.price = price
#         self.period = period
#
# class Teacher:
#     def __init__(self,name,salary,year,month,day,price,period):
#         self.brith = Birthday(year,month,day)
#         self.course = Course(name,price,period)
#         self.name = name
#         self.salary = salary
#
# l = Teacher('li',2000,1990,9,10,3000,'20week')
# print(l.brith.month)
# print(l.course.period)
#
# l.brith = Birthday(1988,4,22)
# print(l.brith.month)
#
##########################################################################################
#
# class Birthday:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#
# class Course:
#     def __init__(self,name,price,period):
#         self.name = name
#         self.price = price
#         self.period = period
#
# class Teacher:
#     def __init__(self,name,salary,course):
#         self.name = name
#         self.salary = salary
#         self.course = course
#
#
# test = Teacher('test',2000,'linux')
# test.brith = Birthday(1999,9,20)
# print(test.brith)
# print(test.brith.year)
#
# test.course = Course('py',998,'30week')
# print(test.course)
# print(test.course.period)
#
####################################################################################

#继承

































































































# class Teacher:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#
#     def teach(self):
#         print('im a teacher %s,teaching..' % self.name)
#
#
# class Student:
#     def __init__(self, name, age, group):
#         self.name = name
#         self.age = age
#         self.group = group
#
#     def study(self):
#         print('im a student %s ,studying....' % self.name)
#
#
# t1 = Teacher('han', 24, 'python')
# s1 = Student('lei', 24, 'sre')
#
# print(t1.name, t1.course, t1.age)
# print(s1.name, s1.group, s1.age)
#
# print(t1.__dict__)
# t1.teach()
# s1.study()
#
##############################################################################################
#
# class Teacher:
#     def __init__(self, name, age, course):
#         self.__name = name
#         self.__age = age
#         self.__course = course
#
#     def teach(self):
#         print('im a teacher %s,teaching..' % self.__name)
#
#
# class Student:
#     def __init__(self, name, age, group):
#         self.__name = name
#         self.__age = age
#         self.__group = group
#
#     def study(self):
#         print('im a student %s ,studying....' % self.__name)
#
#
#
# t1 = Teacher('han', 24, 'python')
# s1 = Student('lei', 24, 'sre')
#
# t1.teach()
# s1.study()
#
# print(t1.__dict__)
# print(s1.__dict__)
#
# print(t1._Teacher__name)
# print(t1._Teacher__age)
# print(t1._Teacher__course)
#
######################################################################################################
#
# class Goods:
#     __discount = 0.8
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def goods_price(self):
#         return self.price * Goods.__discount
#
# apple = Goods('apple',100)
# print(apple.price)
# print(Goods.__dict__)
# print(apple._Goods__discount)
#
#########################################################################################
class Teacher:
    __school = 'ifeng'
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def foo(self):
        print('====================')

t  = Teacher('han',100)
print(t.__dict__)
print(t._Teacher__salary)
print(t._Teacher__school)
t.foo()








































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
# class Teacher:
#     __school = 'ifeng'
#     def __init__(self,name,salary):
#         self.name = name
#         self.__salary = salary
#
#     def foo(self):
#         print('====================')
#
# t  = Teacher('han',100)
# print(t.__dict__)
# print(t._Teacher__salary)
# print(t._Teacher__school)
# t.foo()
##############################################################################################
# class Person:
#     def __init__(self, name, heigth, weigth, sex):
#         self.__nam = name
#         self.__heigth = heigth
#         self.__weigth = weigth
#         self.__sex = sex
#
#     def tell_bmi(self):
#         return self.__weigth / self.__heigth ** 2
#
#     def tell_heigth(self):
#         print(self.__heigth)
#
#     def tell_weigth(self):
#         print(self.__weigth)
#
#     def set_weigth(self, new_weigth):
#         if new_weigth > 20 and new_weigth < 200:
#             self.__weigth = new_weigth
#         else:
#             raise TypeError('error')
#
# te = Person('te',170,65,'boy')
# print(te.tell_bmi())
# print(te.__dict__)
# te.set_weigth(63)
# print(te.tell_weigth())

##############################################################################################
#
# class People:
#     def __init__(self, name, age, sex, h):
#         self.__name = name
#         self.__age = age
#         self.__sex = sex
#         self.__h = h
#
#     def tell_name(self):
#         print(self.name)
#
#     def set_name(self, rename):
#         if not isinstance(rename, str):
#             raise TypeError('error')
#         self.__name = rename
#
#     def tell_info(self):
#         print('''
#         name :%s
#         age:%s
#         sex:%s
#         h: %s
#         ''' % (self.__name, self.__age, self.__sex, self.__h))
#
#
# p1 = People('han', 21, 'boy', 170)
# p1.tell_info()
# p1.set_name('haha')
# p1.tell_info()
#
#









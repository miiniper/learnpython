# 类方法和静态方法
#
# class Student:
#     f = open('test', encoding='utf-8')
#
#     def __init__(self):
#         pass
#
#     @classmethod
#     def show_student_class(cls):
#         for line in cls.f:
#             name, sex = line.strip().split(',')
#             print(name, sex)
#
#     @staticmethod
#     def show_student_static():
#         f = open('test', encoding='utf-8')
#         for line in f:
#             name, sex = line.strip().split(',')
#             print(name, sex)
#
# han = Student()
#
# han.show_student_class()
# print('2============================')
# han.show_student_static()
# print('3============================')
#
# Student.show_student_static()
# print('4============================')
# Student.show_student_class()
# print("======================================")
#
#isinstance(obj,cls)：检查obj是不是cls的对象（传两个参数，一个是对象，一个是类）
#issubclass(sub,super)：检查sub是不是super的子类（传两个参数，一个是子类，一个是父类）
#
# class Foo:
#     pass
# class Son(Foo):
#     pass
#
# s = Son()
# print(isinstance(s,Son))
# print(type(s) is Son)
# print(isinstance(s,Foo))
# print(type(s) is Foo)
#
# print(issubclass(Son,Foo))
# print(issubclass(Son,object))
# print(issubclass(Foo,object))
# print(issubclass(int,object))
#

class Foo:
    def __init__(self):
        self.name = 'test'
        self.age = 24

    def func(self):
        print('hello')


lei = Foo()
setattr(lei,'sex','男')    #给对象的属性赋值，若属性不存在，先创建后赋值
print(lei.sex)

























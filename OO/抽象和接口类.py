# import abc
#
# class File(metaclass = abc.ABCMeta):
#     @abc.abstractmethod
#     def read(self):
#         pass
#     @abc.abstractmethod
#     def write(self):
#         pass
#
#
# class Txt(File):
#     def read(self):
#         print('read data')
#     def write(self):
#         print('write data')
#
# class Stat(File):
#     def read(self):
#         print('read status')
#
#     def write(self):
#         print('write status')
#
#
# t = Txt()
# t.read()
# t.write()
#
# s = Stat()
# s.read()
# s.write()
#
##########################################################################################
#接口
#
# class File:
#     def read(self):
#         pass
#     def write(self):
#         pass
#
#
# class Txt(File):
#     def du(self):
#         print('du data')
#     def xie(self):
#         print('xie data')
#
# class Stat(File):
#     def read(self):
#         print('read status')
#
#     def write(self):
#         print('write status')
#
#
#
# t  = Txt()
# t.du()
#
##############################################################################################
# from  abc  import ABCMeta,abstractmethod
#
# class Pay(metaclass=ABCMeta):
#     @abstractmethod
#     def pay(self):
#         pass
#
#
# class Wechatpay(Pay):
#     def zhifu(self,money):
#         print('wwchat %s' %money)
#
# class Alipay(Pay):
#     def pay(self,money):
#         print('alipay %s' %money)
#
#
# a = Alipay()
# a.pay(32)
# # w = Wechatpay()
# # w.pay(3)
#
##############################################################################################
#多继承
# class A:
#     def test(self):
#         print('im A')
#
# class B(A):
#     def test(self):
#         print('im B')
#
# class C(A):
#     def test(self):
#         print('im C')
#
# class D(B):
#     def test(self):
#         print('im D')
# #
# # class E(B,D,C):
# #     def test(self):
# #         print('im E')
#
#
#
# e = D()
# e.test()
#
# print(D.mro())
#
#############################################################################################
#多态
#
#
# from abc import ABCMeta,abstractmethod
#
# class Animal(metaclass=ABCMeta):
#     @abstractmethod
#     def eat(self):
#         pass
#
# class Cat(Animal):
#     def eat(self):
#         print('cat is  eating...')
#
# class Dog(Animal):
#     def eat(self):
#         print('dog is eating...')
#
#
# def eat_fun(an):
#     an.eat()
#
# cat = Cat()
# eat_fun(cat)
#
#



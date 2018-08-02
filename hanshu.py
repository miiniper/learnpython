# def max2(x, y):
#     m = x if x > y else y
#     return m
#
#
# def max4(a, b, c, d):
#     res1 = max2(a, b)
#     res2 = max2(res1, c)
#     res3 = max2(res2, d)
#     return res3
#
#
# num = max4(-23,24,56,76)
#
# print(num)
# #
#
# def animal():
#     def tiger():
#         print('---tiger---')
#
#     tiger()
#     print('**animal**')
#
#
# animal()
#
# import time
# def timer(func):
#     def inner():
#         start = time.time()
#         print(time.time() - start)
#
#     return inner
#
# @timer
# def func1():
#     print('in func1')
#
# func1()
#
# def han():
#     s = input('input>>')
#     return s[::-1]
#
#
# obj = han()
# print(obj)

#
# def length():
#     s = 'hello world'
#     length = 0
#     for i in s:
#         length += 1
#     return length
#
#
# print(length())

#
# def func():
#     a = 111
#     b = [1, 2, 3, 4]
#     c = {'a': 123, 'b': 7834}
#     return a, b, c
#
#
# print(func())

#
# def han(a, l=[]):
#     l.append(a)
#     print(l)
#
#
# han('hhehe')
# han('niubi')

#
# def fun(a,b,**kwargs):
#     print(a,b,kwargs)
#
#
# fun(a=10,b=22,c=54,d=25,e=4,f=64)
#

#
#
# def f(a,b,*args,default=6,**kwargs):
#     #print(a,b,default,kwargs)
#     return a,b,default,kwargs
#
# print(f(1,2,cc=33,dd=34))
#
#

#
# x = 1
# def f1():
#     x=2
#     def f2():
#         x=3
#         def f3():
#             nonlocal x
#             x = 100000
#         f3()
#         print('in f2 x=',x)
#     f2()
#     print('in f1 x =',x)
#
#
# f1()
#
# def animal():
#     def tiger():
#         print('hello')
#         print('world')
#     tiger()
#
#
# animal()

#
# x = 1
#
#
# def f():
#     x = 'h'
#
#     def f1():
#         x = 'l'
#
#         def f2():
#             print(x)
#
#         f2()
#
#     f1()
#
#
# f()

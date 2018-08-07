# def func():
#     def func2():
#         print('this is func2')
#     return func2
#
#
# f = func()
# f()
#
# def f1(x):
#     print(x)
#     return 123
#
#
# def f2():
#     ret = f1('s')
#     print(ret)
#
#
# f2()
#
# def func():
#     def func2():
#         return 'a'
#     return func2
#
# func2 = func()
# print(func2)

#闭包
#
# def func():
#     x=20
#     def inner():
#         print(x)
#     return inner
#
#
# he = func()
# he()
#
#输出的__closure__为None ：不是闭包函数
# 输出的__closure__有cell元素 ：是闭包函数
# def func():
#     name = 'hanlei'
#     def inner():
#         print(name)
#     print(inner.__closure__)
#     return inner
#
# f = func()
# f()
#
# name = 'hanlei3'
# def func1():
#     def inner1():
#         print(name)
#     print(inner1.__closure__)
#     return inner1()
#
# f1 = func1()
#

from urllib.request import urlopen

def index(url):
    def inner():
        return urlopen(url).read()
    return inner()

u = 'http://www.cnblogs.com/Eva-J/articles/7156261.html#_label1'

get = index(u)
print(get)















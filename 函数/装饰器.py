# 装饰器  高阶函数+嵌套函数===>装饰器

import time

#原函数
def yuan():
    time.sleep(0.5)
    print('ffff')

#装饰器函数
def timer(func):
    def deco():
        start=time.time()
        func()
        end = time.time()
        print(end - start)
    return deco
@timer
def test():
    time.sleep(0.2)
    print('test unknow timer')


test()


# def test1(func):
#     start = time.time()
#     func()
#     end = time.time()
#     print(end - start)
#
#
# test1(yuan)


###################################################
# def test2(func):
#     print(func)
#     return func
#
#
# yuan = test2(yuan)
# yuan()


#######################################################

# def foo():
#     print('in the foo')
#
#     def bar():
#         print('in the inner')
#
#     bar()
#
#
# foo()

# def timer(func):
#     def deco(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#
#     return deco
#
#
# @timer
# def test2():
#     time.sleep(0.3)
#     print('test2')
#
#
# test2()








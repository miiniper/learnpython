# l = [1,2,3,4,56,67,89].__iter__()
#
# print(l.__length_hint__())#获取迭代器中元素的长度
# print(l.__next__())
# print(l.__next__())#一个一个的取值
# print(l.__next__())
# print(l.__next__())
# print(next(l))
# print(next(l))
# print(next(l))#一个一个的取值
#
#
# while True:
#     try:
#         item = l.__next__()
#         print(item)
#     except StopIteration:
#         break

#
# def make_c():
#     for i in range(1, 100):
#         yield i
#
# ret = make_c()
#
# print(next(ret))
# print(next(ret))
# print(next(ret))
# print(next(ret))
# print(next(ret))
#
# for i in range(10):
#     print(next(ret))

##############################################################################
# import time
#
#
# def taif(filename, keyword):
#     f = open(filename)
#     f.seek(0, 1)
#     while True:
#         line = f.readline()
#         if not line:
#             time.sleep(0.1)
#             continue
#         if keyword in line:
#             print('error')
#         yield line
#
#
# gg = taif('test', 'han')
# for line in gg:
#     print(line)


####################################################################################

def func():
    yield from 'hello'

gg = func()
print(list(gg))





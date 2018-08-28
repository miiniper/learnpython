# #join  等待子进程结束，相当于异步变同步
#
# import time
# from multiprocessing import Process
#
# def foo(a,b):
#     print('#'*a)
#     time.sleep(1)
#     print('#'*b)
#
# if __name__ == '__main__':
#     p = Process(target=foo,args=(10,20))
#     p.start()
#     print('hahhahhahhhhhhhhhhhhhhhh')
#     p.join()
#     print('\n==============over===========')
#

# 进程的开启方式2

from multiprocessing import Process
import time
import os


class Myp(Process):
    def __init__(self,a,b):
        super().__init__()   #加参数，必须继承父类
        self.a = a
        self.b = b


    def run(self):
        print('process', os.getpid())
        print(self.b)
        print(self.a)


if __name__ == '__main__':
    p1 = Myp(1,2)
    p1.start()
    p2 = Myp(2,4)
    p2.start()
    print('main', os.getpid())


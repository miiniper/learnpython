#GIL   全局解释器锁,CPYTHON解释器得原因
#python 解释性语言，

#
# import time
# from threading import Thread
# from multiprocessing import Process
#
# #
# def func(n):
#     time.sleep(0.5)
#     print(n)
#
#
# for i in range(10):
#     t= Thread(target=func,args=(i,))
#     t.start()
#
#
# def foo(n):
#     s= n +1
#
# if __name__ =='__main__':
#     start =time.time()
#     for i in range(100):
#         p = Process(target=foo,args=(i,))
#         p.start()
#
#     end = time.time()
#     t1 = end - start
#     print(t1)
#
#     l = []
#     s = time.time()
#     for i in range(100):
#         t = Thread(target=foo,args=(i,))
#         t.start()
#         l.append(t)
#     for i in l :t.join()
#
#     e = time.time()
#     t2 = e - s
#     print(t2)
#

import threading
import time

def ha(n):
    time.sleep(0.2)
    print(threading.current_thread(),threading.get_ident())

for i in range(10):
    threading.Thread(target=ha,args=(i,)).start()

print(threading.active_count())
print(threading.current_thread())
print(threading.enumerate())












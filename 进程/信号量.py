#信号量可以有几个进程读取代码
#信号量相当于多钥匙的进程锁
#

from multiprocessing import Process
from multiprocessing import Semaphore
import time
import random

def foo(i,sem):
    sem.acquire()
    print('进程%s 占用代码' %i)
    time.sleep(random.randint(3,10))
    print('进程%s 释放代码' %i)
    sem.release()

if __name__ =='__main__':
    sem = Semaphore(5)
    for i in range(20):
        p = Process(target=foo,args=(i,sem))
        p.start()






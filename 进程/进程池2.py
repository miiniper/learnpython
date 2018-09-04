import os
import time
from multiprocessing import Pool

def func(n):
    print('start %s' %n, os.getpid())
    time.sleep(0.2)
    print('end %s' % n, os.getpid())


if __name__ == '__main__':
    p = Pool()
    for i in range(10):
        p.apply_async(func,args=(i,))
    p.close()   #结束进程池接受任务
    p.join()


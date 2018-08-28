from multiprocessing import Process
from multiprocessing import Lock
import json
import time


def showt(i):
    with open('t') as f:
        dic = json.load(f)
        print('进程%s查看剩余%s张票' %(i,dic['t']))


def buyt(i,lock):
    lock.acquire()
    with open('t') as f:
        dic = json.load(f)
        time.sleep(0.1)
    if dic['t'] > 0:
        dic['t']-=1
        print('进程%s buy is ok ......................' %i)
    else:
        print('进程%s buy is error' %i)
    time.sleep(0.1)
    with open('t','w') as f:
        json.dump(dic,f)
    lock.release()

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=showt, args=(i,))
        p.start()
    lock = Lock()
    #lock.acquire()
    #lock.release()
    for i in range(10):
        p = Process(target=buyt,args=(i,lock))
        p.start()










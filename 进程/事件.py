from multiprocessing import Event, Process
import time
import random


# 进程锁，信号量，事件 ：一对一，，一对多，多对多
#
# e = Event()
# print(e.is_set())  查看状态  ，false阻塞。
# e.wait()           让进程等待
# e.set()            设置为true
# e.clear()          改为false

# 红绿灯


def le(e):
    while True:
        if e.is_set():
            print('绿灯亮')
            time.sleep(1)
            e.clear()
        else:
            print('红灯亮。。。。。。。')
            time.sleep(1)
            e.set()


def cars(e, i):
    if not e.is_set():
        e.wait()
        print('cat%i is wating...' % i)
        e.set()
        print('car %i is over ********' % i)
        e.clear()


if __name__ == '__main__':
    e = Event()
    l = Process(target=le, args=(e,))
    l.start()
    for i in range(20):
        car = Process(target=cars, args=(e, i))
        car.start()
        time.sleep(random.random())

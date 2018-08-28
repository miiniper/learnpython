from multiprocessing import Process
import time
import random


def piao(name):
    print('%s is in piaoing' % name)
    time.sleep(random.randint(1, 3))
    print('%s is end ' % name)


if __name__ == '__main__':
    p1 = Process(target=piao, kwargs={'name': 'han1'})
    p2 = Process(target=piao, kwargs={'name': 'han2'})
    p3 = Process(target=piao, kwargs={'name': 'han3'})
    p1.start()
    p2.start()
    p3.start()

    print('main is runnning...... ')







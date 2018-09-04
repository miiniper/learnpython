from multiprocessing import Process
from multiprocessing import Queue
import time
import random


def consumer(q, name, ):
    while True:
        f = q.get()
        if f is None:break
        print('%s consume %s' %(name, f))
        time.sleep(0.5)


def producer(q, name, thing):
    for i in range(5):
        f = ' %s produce %s%i' % (name, thing, i)
        q.put(f)
        print(f)
        time.sleep(0.5)


if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=producer, args=(q, 'p1', 'apple'))
    c1 = Process(target=consumer, args=(q, 'c1'))
    p1.start()
    c1.start()
    p1.join()
    q.put(None)
    c1.join()




#队列 先进先出
#
from multiprocessing import Process
from multiprocessing import Queue

# q = Queue()
# q.put('hhaha')
# q.put('eee')
# print(q.get())
# q.get()
# print(q.full())
# print(q.empty())

def produce(q):
    q.put('hahah')

def consume(q):
    print(q.get())


if __name__ =="__main__":
    q = Queue()
    p = Process(target=produce,args=(q,))
    c = Process(target=consume,args=(q,))
    p.start()
    c.start()





import time
from multiprocessing import Process
import random
import os


class Piao(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s is running' %self.name)
        time.sleep(random.randint(1,3))
        print('%s end' %self.name)

    

if __name__ =='__main__':
    p1 = Piao('han1')
    p2 = Piao('han2')
    p3 = Piao('han3')
    p1.start()
    p2.start()
    p3.start()

    print('main is running..........')






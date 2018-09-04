from multiprocessing import Process
from multiprocessing import Pipe

c1,c2  = Pipe()

c1.send('sdfsdfs')
print(c2.recv())







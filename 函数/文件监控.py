import time
import json

# def taif(filename, keyword):
#     f = open(filename)
#     f.seek(0, 1)
#     while True:
#         line = f.readline()
#         if not line:
#             time.sleep(0.1)
#             continue
#         if keyword in line:
#             print('error')
#         yield line

timestamp = int(time.time())

dic = {'name':'logmonitor','time':timestamp,'value':'key'}
data = json.dumps(dic)
print(data)


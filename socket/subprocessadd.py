# import subprocess
#
# res = subprocess.Popen(r'dir',shell=True,
#                        stdout=subprocess.PIPE,
#                        stderr=subprocess.PIPE)
#
# print(res.stdout.read().decode('gbk'))
# print('===============')
# print(res.stdout.read().decode('gbk'))
# print(res.stderr.read().decode('gbk'))
#
#
import struct

res = struct.pack('i',123)
print(res,len(res),type(res))

res2 = struct.pack('i',12345111)
print(res2,len(res2),type(res2))

unpack_res =struct.unpack('i',res2)
print(unpack_res)


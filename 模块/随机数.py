import random

# # 1.随机小数
# print(random.random())
# print(random.uniform(1, 3))
#
# # 2.随机整数
# print(random.randint(1, 5))
# print(random.randrange(1, 5, 2))
#
# # 3.随机选择一个返回
# print(random.choice([1, '23', [4, 5]]))

# # 5.打乱列表顺序
# item = [1,2,5,8,4,3]
# random.shuffle(item)
# print(item)

# l=[]
# for i in range(5):
#     l.append(str(random.randint(0,9)))
#
# print(''.join(l))
# print(l)
#
# print(random.randint(1000,9999))


# chr(65-90)#a-z
# chr(97-122)#A-Z

num_list = list(range(10))
new_num_l=list(map(str,num_list))
l =[]
for i in range(65,93):
    zifu=chr(i)
    l.append(zifu)

new_num_l.extend(l)
print(new_num_l)
ret_l=[]
for i in range(4):
    ret_l.append(random.choice(new_num_l))
print(''.join(ret_l))






















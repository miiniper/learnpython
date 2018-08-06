#
# def foo(n):
#     if n%2==0:
#         n=n/2
#         return foo(n)
#     else:
#         return n
#
# print(foo(32))
#
#
#

l = [2, 3, 5, 10, 15, 16, 18, 22, 26, 30, 32, 35, 41, 42, 43, 55, 56, 66, 67, 69, 72, 76, 82, 83, 88]


def ss(l, key):
    mid = len(l) // 2
    if l[mid] > key:
        nl = l[:mid]
        return ss(nl, key)
    elif l[mid] < key:
        nl = l[mid + 1:]
        return ss(nl, key)
    else:
        return l[mid]


print(ss(l, 69))

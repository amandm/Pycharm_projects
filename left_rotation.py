#!/bin/python3

import sys


# l1 = [int(k) for k in input().strip().split(' ')]
# l2 = [int(k) for k in input().strip().split(' ')]

l1 = [5,4]
l2 = [1,2,3,4,5]
p = l1[0]
q = l1[1]
print(l1)
print(l2)

def lrotn(l , k):
    for i in range(k):
        temp = l.pop(0)
        l.append(temp)

lrotn(l2,4)

for i in range(p):
    print(l2[i],end = " ")

# for i in range(len(l2)):
#     if i == (len(l2) - 1):
#         print(l2[i])
#     else:
#         print(i,end = " ")


#!/bin/python3

# import sys
#
#
# l1 = [int(k) for k in input().strip().split(' ')]
# l2 = [int(k) for k in input().strip().split(' ')]
#
# # l1 = [5,4]
# # l2 = [1,2,3,4,5]
# #
# # print(l1)
# # print(l2)
#
# def lrotn(l , k):
#     for i in range(k):
#         temp = l.pop(0)
#         l.append(temp)
#
# lrotn(l2,4)
#
# for i in len(l2):
#     if i == (len(l2) - 1):
#         print(i)
#     else print(i,end = " ")
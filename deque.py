# from collections import deque
# dq=deque()
# dq.append(10)
# dq.append(20)
# dq.append(30)
# dq.append(40)
# print(dq)
# dq.appendleft(50)
# print(dq)
# dq.pop()
# print(dq)
# dq.popleft()
# print(dq)
# dq.extend([40,50])
# print(dq)
# dq.extendleft([60,70])
# print(dq)
# dq.rotate(2)
# print(dq)
# dq.rotate(-1)
# print(dq)
# dq.remove(10)
# print(dq)
# print(dq.count(30))
# print(dq.index(30))
# dq.reverse()
# print(dq)
# dq.clear()
# print(dq)

# sample input
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

# code
# from collections import deque
# dq=deque()
# n=int(input())
# for i in range(n):
#     x=input().split()
#     if x[0]=='append':
#         dq.append(int(x[1]))
#     elif x[0]=='appendleft':
#         dq.appendleft(int(x[1]))
#     elif x[0]=='pop':
#         dq.pop(int(x[1]))
#     elif x[0]=='poleft':
#         dq.popleft(int(x[1]))
# print(*dq)
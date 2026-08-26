#collections in queue:
# 1)deque
# 2)counter
# 3)default dict
# 4)ordered dict
# 5)chain map
# 6)named tuple

#deque
# from collections import deque
# q=deque()
# q.append(10)
# q.append(20)
# q.append(30)
# print(q)
# q.popleft()
# print(q)

#counter
# from collections import Counter
# data=[1,2,2,2,2,2,3,3,3,4,4,4,6]
# c=Counter(data)
# print(c)

#defaultidct
# from collections import defaultdict
# d=defaultdict(int)
# d["apple"]+=1
# d["apple"]+=1
# d["apple"]+=1
# print(d)

#orderdict
# from collections import OrderedDict
# d=OrderedDict()
# d['A']=10
# d['B']=20
# d['C']=30
# d['D']=5
# print(d)

#chain map
# from collections import ChainMap
# d1={"name":"Bhanu"}
# d2={"age":21}
# d=ChainMap(d1,d2)
# print(d["name"])
# print(d["age"])

#namedtupel
# from collections import namedtuple
# student=namedtuple("Student",["name","age"])
# s=student("bhanu",21)
# print(s.name)
# print(s.age)

#queue operations using stack
# stack1=[]
# stack2=[]
# def enqueue(value):
#     stack1.append(value)
# def dequeue():    
#     if not stack1 and not stack2:
#         print("Queue is empty")
#         return
#     if not stack2:
#         while stack1:
#             stack2.append(stack1.pop())
#     return stack2.pop()
# def display():
#     print("Queue:",list(reversed(stack1))+list(stack2))    
# enqueue(10)
# enqueue(20)
# enqueue(30)
# enqueue(40)
# enqueue(50)
# display()
# print("removed:",dequeue())
# display()
# print("removed:",dequeue())
# display()
#PRIORITY QUEUE
#Ranking base on Priority
'''import heapq
pq =[]
heapq.heappush(pq, (1, "Emergency"))
heapq.heappush(pq, (3, "Emergency" ))
heapq.heappush(pq, (2, "Consultation"))
while pq:
    print(heapq.heappop(pq))  '''


#Manual for take name with priority
'''from queue import PriorityQueue
pq = PriorityQueue()
n = int(input("Enter the number of element: "))
for i in range(n):
    value = input("ENter the Value: ")
    priority = int(input("Enter the Priority: "))
    pq.put((priority, value))
print("\n Priority Queue: ")
while not pq.empty():
    priority, value = pq.get()
    print("Value: ", value, "Priority: ", priority)   '''


'''import heapq
arr = list(map(int,(input("Enter elements: ").split())))
n = int(input("Enter n: "))
largest = heapq.nlargest(n, arr)
print(largest[-1])  '''


#Manual
'''arr = list(map(int,(input("Enter elements: ").split())))
n = int(input("Enter n: "))
for i in range(n):
    largest = arr[0]
    for j in range(1, len(arr)):
        if arr[j]>largest:
            largest-arr[j]
    arr.remove(largest)
print(largest)'''
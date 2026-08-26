# push
# heap = list(map(int, input('Enter elements: ').split()))
# value = int(input('Enter value to push: '))
# # Build min heap manually
# for i in range(1, len(heap)):
#     l = i
#     while l > 0:
#         root = (l - 1) // 2
#         if heap[root] <= heap[l]:
#             break
#         heap[root], heap[l] = heap[l], heap[root]
#         l = root
# # Insert new value
# heap.append(value)
# l = len(heap) - 1
# # Heapify up
# while l > 0:
#     root = (l - 1) // 2
#     if heap[root] <= heap[l]:
#         break
#     heap[root], heap[l] = heap[l], heap[root]
#     l = root
# print(heap)

# pop
# heap = list(map(int, input('Enter elements: ').split()))
# # Build min heap manually
# for i in range(1, len(heap)):
#     l = i
#     while l > 0:
#         root = (l - 1) // 2
#         if heap[root] <= heap[l]:
#             break
#         heap[root], heap[l] = heap[l], heap[root]
#         l = root
# print('Min heap:', heap)
# # Pop root
# popped = heap[0]
# # Move last element to root
# heap[0] = heap[-1]
# # Remove last element
# heap.pop()
# # Heapify down
# i = 0
# while True:
#     left = 2 * i + 1
#     right = 2 * i + 2
#     smallest = i
#     if left < len(heap) and heap[left] < heap[smallest]:
#         smallest = left
#     if right < len(heap) and heap[right] < heap[smallest]:
#         smallest = right
#     if smallest == i:
#         break
#     heap[i], heap[smallest] = heap[smallest], heap[i]
#     i = smallest
# print('Popped element:', popped)
# print('Heap after pop:', heap)

#replace
heap = list(map(int, input('Enter elements: ').split()))
# Build min heap manually
for i in range(1, len(heap)):
    l = i
    while l > 0:
        root = (l - 1) // 2
        if heap[root] <= heap[l]:
            break
        heap[root], heap[l] = heap[l], heap[root]
        l = root
print('Min heap:', heap)
n=int(input('Enter element to replace: '))
# Pop root
heap[0]=n
# Build min heap manually
for i in range(1, len(heap)):
    l = i
    while l > 0:
        root = (l - 1) // 2
        if heap[root] <= heap[l]:
            break
        heap[root], heap[l] = heap[l], heap[root]
        l = root
print('Heap:', heap)
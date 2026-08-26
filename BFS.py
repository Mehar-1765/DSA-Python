#BFS-It works like FIFO
vertices=["A","B","C","D"]
graph={}
for vertex in vertices:
    graph[vertex]=[]
n=int(input("Enter no.of edges:"))
for i in range(n):
    e,v=input("Enter edge(e,v):").split()
    graph[e].append(v)
    graph[v].append(e)
start=input("Enter starting vertex:")
visited=set()
queue=[]
visited.add(start)
queue.append(start)
print("\nBFS Traversal")
while queue:
    vertex=queue.pop(0)
    print(vertex,end=' ')
    for adj in graph[vertex]:
        if adj not in visited:
            visited.add(adj)
            queue.append(adj)
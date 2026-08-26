#graph DFS
# vertices=["A","B","C","D"]
# graph={}
# for vertex in vertices:
#     graph[vertex]=[]
# n=int(input("Enter no.of edges:"))
# for i in range(n):
#     e,v=input("Enter edge(e,v):").split()
#     graph[e].append(v)
#     graph[v].append(e)
# start=input("Enter starting vertex:")
# visited=set()
# def dfs(vertex):
#     print("Visit:",vertex)
#     visited.add(vertex)
#     for adj in graph[vertex]:
#         if adj not in visited:
#             print(vertex,'->',adj)
#             dfs(adj)
#             print("Backtracking to",vertex)
# print("\nDFS with BT")
# dfs(start)
# print("\n Graph")
# for vertex in graph:
#     print(vertex,'->',graph[vertex])
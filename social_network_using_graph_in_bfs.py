people=input('Enter people: ').split()
graph={}
for person in people:
    graph[person]=[]
n=int(input('Enter no of friendships: '))
for i in range(n):
    p1,p2=input('Enter 2 names: ').split()
    graph[p1].append(p2)
    graph[p2].append(p1)
start=input('Enter person to find connections: ')
visited=set()
queue=[]
queue.append(start)
visited.add(start)
print('\nPeople connected to',start,':')
while queue:
    current=queue.pop(0)
    for friend in graph[current]:
        if friend not in visited:
            visited.add(friend)
            queue.append(friend)
            print(friend, end=' ')

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, p = map(int, input().split())
    graph[s].append((e, p))
start, end = map(int, input().split())

distance = [float("inf")] * (n+1)
distance[start] = 0
queue = []
parent = [0] * (n+1)
heappush(queue, (0, start))

while queue:
    dist, now = heappop(queue)
    if distance[now] < dist:
        continue
    for nn, pp in graph[now]:
        cost = distance[now] + pp
        if cost < distance[nn]:
            distance[nn] = cost
            parent[nn] = now
            heappush(queue, (cost, nn))

print(distance[end])
path = []
curr = end
while curr:
    path.append(curr)
    curr = parent[curr]
print(len(path))
for i in path[::-1]:
    print(i, end=" ")
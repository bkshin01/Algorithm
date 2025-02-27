from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(start, target, graph):
    distance = [float("inf")]*(len(graph)+1)
    distance[start] = 0
    queue = []
    heappush(queue, (0, start))
    while queue:
        dist, node = heappop(queue)
        if dist > distance[node]:
            continue
        for vv, ww in graph[node]:
            cost = distance[node] + ww
            if cost < distance[vv]:
                distance[vv] = cost
                heappush(queue, (cost, vv))
    return distance[target]

n, m, x = map(int, input().split())
graph = {}
for _ in range(m):
    s, e, t = map(int, input().split())
    if s in graph:
        graph[s].append((e, t))
    else:
        graph[s] = [(e, t)]

result = [0] * (n+1)
for i in range(1, n+1):
    result[i] = dijkstra(i, x, graph) # go_party
    result[i] += dijkstra(x, i, graph) # return_home
print(max(result))
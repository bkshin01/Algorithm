# 반드시 거쳐야 하는 정점에 대한 최단 경로들을 구해서 더하자
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(start, target, graph):
    distance = [float("inf")] * (n+1)
    distance[start] = 0
    queue = []
    heappush(queue, (0, start))
    while queue:
        dist, now = heappop(queue)
        if dist > distance[now]:
            continue
        for vv, ww in graph[now]:
            cost = distance[now] + ww
            if cost < distance[vv]:
                distance[vv] = cost
                heappush(queue, (cost, vv))
    return distance[target]

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

path1 = dijkstra(1, v1, graph) + dijkstra(v1, v2, graph) + dijkstra(v2, n, graph)
path2 = dijkstra(1, v2, graph) + dijkstra(v2, v1, graph) + dijkstra(v1, n, graph)
answer = min(path1, path2)
if answer == float("inf"):
    print(-1)
else:
    print(answer)